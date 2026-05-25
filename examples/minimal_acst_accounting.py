"""
Minimal Adaptive Conservation and Symmetry Theory (ACST) accounting example.

This toy model tracks an adaptive conserved-like quantity C_A and a memory
reservoir C_memory:

    dC_active/dt = P - mu*C_active - s*C_active + r*C_memory
    dC_memory/dt = s*C_active - r*C_memory - rho*C_memory

It demonstrates leakage, storage, return, and diagnostic accounting error.

Run:
    python examples/minimal_acst_accounting.py
"""

from __future__ import annotations

import math
from dataclasses import dataclass


@dataclass(frozen=True)
class ACSTParameters:
    steps: int = 5000
    dt: float = 0.002
    production_base: float = 0.25
    production_amp: float = 0.15
    production_frequency: float = 2.0
    active_decay: float = 0.04
    storage_rate: float = 0.08
    return_rate: float = 0.03
    memory_decay: float = 0.015
    initial_active: float = 1.0
    initial_memory: float = 0.0


def production(t: float, p: ACSTParameters) -> float:
    """Bounded adaptive input source."""
    return p.production_base + p.production_amp * (0.5 + 0.5 * math.sin(p.production_frequency * t))


def run_accounting(params: ACSTParameters | None = None) -> dict[str, float]:
    p = params or ACSTParameters()

    c_active = p.initial_active
    c_memory = p.initial_memory

    total_input = 0.0
    total_active_decay = 0.0
    total_memory_decay = 0.0
    total_storage = 0.0
    total_return = 0.0
    max_balance_error = 0.0

    initial_total = c_active + c_memory

    for step in range(p.steps):
        t = step * p.dt
        source = production(t, p)

        active_decay = p.active_decay * c_active
        storage = p.storage_rate * c_active
        memory_return = p.return_rate * c_memory
        memory_decay = p.memory_decay * c_memory

        dc_active = source - active_decay - storage + memory_return
        dc_memory = storage - memory_return - memory_decay

        old_total = c_active + c_memory

        c_active += p.dt * dc_active
        c_memory += p.dt * dc_memory

        # Keep the toy reservoirs nonnegative.
        c_active = max(0.0, c_active)
        c_memory = max(0.0, c_memory)

        total_input += p.dt * source
        total_active_decay += p.dt * active_decay
        total_memory_decay += p.dt * memory_decay
        total_storage += p.dt * storage
        total_return += p.dt * memory_return

        new_total = c_active + c_memory
        predicted_total_change = p.dt * (source - active_decay - memory_decay)
        measured_total_change = new_total - old_total
        balance_error = abs(measured_total_change - predicted_total_change)
        max_balance_error = max(max_balance_error, balance_error)

    final_total = c_active + c_memory

    # Global conservation-style ledger:
    # final = initial + input - active_decay - memory_decay, up to numerical error.
    ledger_prediction = initial_total + total_input - total_active_decay - total_memory_decay
    ledger_error = abs(final_total - ledger_prediction)

    adaptive_retention = final_total / max(initial_total + total_input, 1e-12)
    memory_fraction = c_memory / max(final_total, 1e-12)

    return {
        "final_active": c_active,
        "final_memory": c_memory,
        "final_total": final_total,
        "total_input": total_input,
        "total_active_decay": total_active_decay,
        "total_memory_decay": total_memory_decay,
        "total_storage": total_storage,
        "total_return": total_return,
        "ledger_prediction": ledger_prediction,
        "ledger_error": ledger_error,
        "max_step_balance_error": max_balance_error,
        "adaptive_retention": adaptive_retention,
        "memory_fraction": memory_fraction,
    }


if __name__ == "__main__":
    metrics = run_accounting()
    print("Minimal ACST accounting example complete")
    for key, value in metrics.items():
        print(f"{key}: {value:.8f}")
