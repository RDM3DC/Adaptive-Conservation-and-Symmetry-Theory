"""
Two-reservoir ACST solver.

This solves the finite-dimensional adaptive conservation model:

    dC/dt = P0 - mu*C - s*C + r*M
    dM/dt = s*C - r*M - rho*M

The exact constant-input equilibrium is:

    C* = P0 / (mu + s*rho/(r+rho))
    M* = s*C*/(r+rho)

The equilibrium is stable when:

    mu*(r+rho) + s*rho > 0

Run:
    python examples/two_reservoir_acst_solver.py
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ACSTReservoirParameters:
    p0: float = 0.35
    mu: float = 0.05
    storage_rate: float = 0.12
    return_rate: float = 0.04
    memory_decay: float = 0.02
    dt: float = 0.002
    steps: int = 10000
    initial_active: float = 0.2
    initial_memory: float = 0.0


def equilibrium(p: ACSTReservoirParameters) -> dict[str, float | bool]:
    denom = p.mu + p.storage_rate * p.memory_decay / (p.return_rate + p.memory_decay)
    if denom <= 0.0:
        return {"exists": False, "C_star": 0.0, "M_star": 0.0}

    c_star = p.p0 / denom
    m_star = p.storage_rate * c_star / (p.return_rate + p.memory_decay)
    return {"exists": True, "C_star": c_star, "M_star": m_star}


def stability_condition(p: ACSTReservoirParameters) -> dict[str, float | bool]:
    trace = -(p.mu + p.storage_rate + p.return_rate + p.memory_decay)
    determinant = p.mu * (p.return_rate + p.memory_decay) + p.storage_rate * p.memory_decay
    return {
        "trace": trace,
        "determinant": determinant,
        "stable": trace < 0.0 and determinant > 0.0,
    }


def run_solver(params: ACSTReservoirParameters | None = None) -> dict[str, float | bool]:
    p = params or ACSTReservoirParameters()

    c = max(0.0, p.initial_active)
    m = max(0.0, p.initial_memory)

    total_input = 0.0
    total_active_decay = 0.0
    total_memory_decay = 0.0
    total_storage = 0.0
    total_return = 0.0
    initial_total = c + m

    for _ in range(p.steps):
        active_decay = p.mu * c
        storage = p.storage_rate * c
        memory_return = p.return_rate * m
        memory_decay = p.memory_decay * m

        dc = p.p0 - active_decay - storage + memory_return
        dm = storage - memory_return - memory_decay

        c = max(0.0, c + p.dt * dc)
        m = max(0.0, m + p.dt * dm)

        total_input += p.dt * p.p0
        total_active_decay += p.dt * active_decay
        total_memory_decay += p.dt * memory_decay
        total_storage += p.dt * storage
        total_return += p.dt * memory_return

    eq = equilibrium(p)
    stable = stability_condition(p)

    c_star = float(eq["C_star"])
    m_star = float(eq["M_star"])
    distance_to_equilibrium = ((c - c_star) ** 2 + (m - m_star) ** 2) ** 0.5

    final_total = c + m
    ledger_prediction = initial_total + total_input - total_active_decay - total_memory_decay
    ledger_error = abs(final_total - ledger_prediction)

    return {
        **eq,
        **stable,
        "final_active": c,
        "final_memory": m,
        "distance_to_equilibrium": distance_to_equilibrium,
        "final_total": final_total,
        "ledger_prediction": ledger_prediction,
        "ledger_error": ledger_error,
        "total_input": total_input,
        "total_active_decay": total_active_decay,
        "total_memory_decay": total_memory_decay,
        "total_storage": total_storage,
        "total_return": total_return,
    }


if __name__ == "__main__":
    result = run_solver()
    print("Two-reservoir ACST solver complete")
    for key, value in result.items():
        if isinstance(value, bool):
            print(f"{key}: {value}")
        else:
            print(f"{key}: {value:.8f}")
