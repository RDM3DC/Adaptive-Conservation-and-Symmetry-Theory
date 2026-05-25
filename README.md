# Adaptive Conservation and Symmetry Theory (ACST)

**Standalone repository for Arm 9 of the expanded Canonical Core framework.**

ACST studies what remains conserved when a system is adaptive, memory-bearing, phase-structured, and geometry-changing.

Core question:

```text
what survives when everything adapts?
```

ACST does **not** replace classical conservation laws. It generalizes conservation accounting for systems with:

- input
- decay
- memory storage
- memory return
- adaptive leakage
- symmetry breaking
- quasi-invariants

---

## Place in Canonical Core

```text
1. ARP/AIN                               → adaptation engine
2. Adaptive-π Geometry                   → adaptive phase-period geometry
3. Curve Memory / CMA                    → path and derivative memory
4. Phase-Lift / PR-Root / PROs           → branch-aware phase operators
5. QPS-GR Mapping                        → strain / clock / visibility engineering layer
6. Adaptive Curvature Flow Networks      → dynamic geometry
7. Phase-Memory Transport Theory         → adaptive phase-memory transport
8. Emergent Phase Matter                 → stable phase-memory structures
9. Adaptive Conservation and Symmetry    → adaptive invariants and laws
```

ACST is the **laws-and-invariants arm**.

---

## Core Idea

Classical conservation often has the form:

```text
dC/dt = 0
```

Adaptive systems often require:

```text
dC_A/dt = input − decay + memory feedback
```

A prototype adaptive invariant law is:

```text
dC_A/dt = P_A − μC_A + σM
```

where:

| Symbol | Meaning |
|---|---|
| `C_A` | adaptive conserved-like quantity |
| `P_A` | production / input |
| `μC_A` | relaxation / leakage |
| `σM` | memory return |
| `M` | memory field |

Exact conservation is recovered when:

```text
P_A = 0, μ = 0, σ = 0
```

---

## Adaptive Noether Form

A schematic adaptive Noether-like form is:

```text
∂_μ J^μ = S_adapt − L_decay + R_memory
```

where:

- `J^μ` is a current
- `S_adapt` is adaptive source
- `L_decay` is loss / relaxation
- `R_memory` is memory return

Exact conservation is the special case:

```text
∂_μ J^μ = 0
```

---

## Repository Structure

```text
Adaptive-Conservation-and-Symmetry-Theory/
├── README.md
├── papers/
│   └── adaptive-conservation-and-symmetry-theory.md
├── docs/
│   ├── notation.md
│   └── roadmap.md
└── examples/
    └── minimal_acst_accounting.py
```

---

## Canonical Relationship

ACST is Paper 09 in the expanded Canonical Core framework:

- Canonical Core website: https://rdm3dc.github.io/canonical-core/
- Canonical Core repo: https://github.com/RDM3DC/canonical-core

This standalone repository develops ACST into:

- adaptive conservation equations
- quasi-invariant diagnostics
- symmetry-breaking examples
- memory-leakage accounting
- simulation metrics
- links to ACFN, PMT, and EPM

---

## Status

**Version:** 0.1.0-draft  
**Status:** Early standalone scaffold  
**Canonical role:** Arm 9 — adaptive laws and quasi-invariants

---

## License

Text and theory notes: CC BY 4.0 unless otherwise stated.  
Code examples: MIT-style permissive use unless otherwise stated.
