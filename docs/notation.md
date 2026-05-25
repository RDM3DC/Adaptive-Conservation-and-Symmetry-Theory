# ACST Notation

Canonical notation for Adaptive Conservation and Symmetry Theory.

---

## Core Quantities

| Symbol | Meaning |
|---|---|
| `C_A` | adaptive conserved-like quantity |
| `P_A` | production / input |
| `μC_A` | relaxation / leakage |
| `M` | memory density |
| `σM` | memory return |
| `J^μ` | current |
| `S_adapt` | adaptive source |
| `L_decay` | decay / loss term |
| `R_memory` | memory return term |

---

## Prototype Adaptive Conservation Law

```text
dC_A/dt = P_A − μC_A + σM
```

Exact conservation appears when:

```text
P_A = 0, μ = 0, σ = 0
```

---

## Adaptive Noether Form

```text
∂_μ J^μ = S_adapt − L_decay + R_memory
```

Exact conservation appears when:

```text
∂_μ J^μ = 0
```

---

## Reservoir Model

```text
dC_active/dt = P − μC_active − sC_active + rC_memory
```

```text
dC_memory/dt = sC_active − rC_memory − ρC_memory
```

---

## Example Adaptive Invariants

```text
Q_M = ∫ M dx
```

```text
Q_G = ∫ G dx
```

```text
W = (1/2πₐ)∮∇θ_R · dl
```

---

## Diagnostic

```text
leakage_error = |dC_A/dt − (input − decay + memory_return)|
```
