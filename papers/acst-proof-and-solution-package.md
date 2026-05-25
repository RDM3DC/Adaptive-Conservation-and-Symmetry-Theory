# ACST Proof and Solution Package

**Repository:** Adaptive-Conservation-and-Symmetry-Theory  
**Canonical Core Arm:** 09  
**Date:** 2026-05-25  
**Status:** Mathematical working draft

---

## 0. Purpose

Adaptive Conservation and Symmetry Theory (ACST) asks:

```text
what survives when everything adapts?
```

This document proves the first rigorous core of ACST.

The goal is not to replace classical conservation laws. The goal is to prove the conservation-accounting structure for adaptive systems with:

- input,
- decay,
- memory storage,
- memory return,
- leakage,
- quasi-invariants,
- symmetry residuals.

---

## 1. Minimal ACST Law

The basic adaptive conserved-like quantity is `C_A(t)`:

```text
dC_A/dt = P_A(t) − μ C_A + σ M.
```

Where:

- `C_A` is the active adaptive quantity,
- `P_A(t)` is production/input,
- `μC_A` is active decay/leakage,
- `σM` is memory return,
- `M` is a memory reservoir.

A two-reservoir model is more complete:

```text
dC/dt = P(t) − μC − sC + rM
```

```text
dM/dt = sC − rM − ρM
```

where:

- `C` = active quantity,
- `M` = memory-stored quantity,
- `s` = storage rate from active to memory,
- `r` = return rate from memory to active,
- `μ` = active decay,
- `ρ` = memory decay.

Assume throughout:

```text
P(t) ≥ 0,
μ,s,r,ρ ≥ 0,
C(0) ≥ 0,
M(0) ≥ 0.
```

---

## 2. Theorem: Positivity of Adaptive Reservoirs

### Statement

For the two-reservoir ACST model,

```text
dC/dt = P(t) − μC − sC + rM
```

```text
dM/dt = sC − rM − ρM,
```

if `P(t) ≥ 0`, all rates are nonnegative, and `C(0),M(0) ≥ 0`, then

```text
C(t) ≥ 0,
M(t) ≥ 0
```

for all `t ≥ 0`.

### Proof

At the boundary `C = 0`,

```text
dC/dt = P(t) + rM ≥ 0.
```

So the vector field points inward or tangent to the nonnegative quadrant.

At the boundary `M = 0`,

```text
dM/dt = sC ≥ 0.
```

So the vector field also points inward or tangent there.

Therefore trajectories starting in the nonnegative quadrant cannot leave it.

QED.

---

## 3. Theorem: Exact Ledger Conservation

### Statement

Define the total active-plus-memory quantity:

```text
Q(t) = C(t) + M(t).
```

Then

```text
dQ/dt = P(t) − μC(t) − ρM(t).
```

Therefore the ledger quantity

```text
L(t) = Q(t) − Q(0) − ∫0^t P(τ)dτ + ∫0^t μC(τ)dτ + ∫0^t ρM(τ)dτ
```

satisfies

```text
L(t) = 0
```

for all `t`.

### Proof

Add the two reservoir equations:

```text
dC/dt + dM/dt
= P − μC − sC + rM + sC − rM − ρM.
```

The storage and return terms cancel:

```text
−sC + sC = 0
```

```text
rM − rM = 0.
```

Thus

```text
dQ/dt = P − μC − ρM.
```

Integrating from `0` to `t` gives

```text
Q(t) − Q(0) = ∫0^t P(τ)dτ − ∫0^t μC(τ)dτ − ∫0^t ρM(τ)dτ.
```

Rearranging gives `L(t)=0`.

QED.

### Interpretation

Storage and return do not destroy conservation accounting. They only move quantity between active and memory reservoirs.

Loss occurs only through explicit decay terms or external boundary flux.

---

## 4. Exact Conservation as a Limit

### Statement

If

```text
P(t)=0,
μ=0,
ρ=0,
```

then

```text
C(t)+M(t)=C(0)+M(0).
```

### Proof

From the ledger equation:

```text
dQ/dt = P − μC − ρM.
```

Setting `P=μ=ρ=0` gives

```text
dQ/dt=0.
```

Therefore `Q(t)` is constant.

QED.

### Interpretation

Classical exact conservation is a special case of ACST where there is no input and no decay.

---

## 5. Constant-Input Equilibrium

Assume constant input:

```text
P(t)=P0 ≥ 0.
```

The equilibrium solves:

```text
0 = P0 − (μ+s)C* + rM*
```

```text
0 = sC* − (r+ρ)M*.
```

From the second equation:

```text
M* = sC*/(r+ρ).
```

Substitute into the first:

```text
0 = P0 − (μ+s)C* + r s C*/(r+ρ).
```

So

```text
C* = P0 / [ μ + sρ/(r+ρ) ].
```

and

```text
M* = sP0 / [(r+ρ)( μ + sρ/(r+ρ) )].
```

If the denominator is positive, the equilibrium is finite and nonnegative.

The effective loss rate is

```text
μ_eff = μ + sρ/(r+ρ).
```

Interpretation:

- active decay contributes `μ`,
- storage only becomes true loss through memory decay `ρ`,
- faster return `r` reduces effective memory loss.

---

## 6. Stability of the Two-Reservoir Equilibrium

The homogeneous linear system matrix is

```text
A = [[−(μ+s),  r     ],
     [ s,      −(r+ρ)]].
```

The trace is

```text
tr(A) = −(μ+s+r+ρ) ≤ 0.
```

The determinant is

```text
det(A) = (μ+s)(r+ρ) − rs
       = μ(r+ρ) + sρ.
```

If

```text
μ(r+ρ)+sρ > 0,
```

then

```text
tr(A)<0
```

and

```text
det(A)>0.
```

For a two-dimensional linear system, this implies both eigenvalues have negative real parts.

Therefore the equilibrium is linearly stable whenever there is any true loss through active decay or memory decay:

```text
μ(r+ρ)+sρ > 0.
```

QED.

---

## 7. Quasi-Invariant Bound

### Statement

Suppose an adaptive quantity satisfies

```text
|dC_A/dt| ≤ ε
```

for `0 ≤ t ≤ T`. Then

```text
|C_A(T) − C_A(0)| ≤ εT.
```

### Proof

By integration:

```text
C_A(T) − C_A(0) = ∫0^T dC_A/dt dt.
```

Taking absolute values:

```text
|C_A(T) − C_A(0)| ≤ ∫0^T |dC_A/dt| dt ≤ ∫0^T ε dt = εT.
```

QED.

### Interpretation

A quasi-invariant is useful when its drift is bounded over the time scale of interest.

---

## 8. Adaptive Noether Accounting Theorem

### Classical reference

A classical local conservation law has the form

```text
∂_μ J^μ = 0.
```

ACST generalizes this to

```text
∂_μ J^μ = S_adapt − L_decay + R_memory.
```

### Integrated form

Let `Ω` be a spatial domain with boundary `∂Ω`. Let `J^0` be density and `J_space` be flux. Then

```text
∂t J^0 + ∇·J_space = S_adapt − L_decay + R_memory.
```

Integrating over `Ω` gives

```text
d/dt ∫Ω J^0 dx
= ∫Ω (S_adapt − L_decay + R_memory) dx − ∮∂Ω J_space·n dS.
```

### Proof

Integrate the local equation over `Ω`:

```text
∫Ω ∂t J^0 dx + ∫Ω ∇·J_space dx
= ∫Ω (S_adapt − L_decay + R_memory) dx.
```

Use the divergence theorem:

```text
∫Ω ∇·J_space dx = ∮∂Ω J_space·n dS.
```

Move the boundary term to the right side:

```text
d/dt ∫Ω J^0 dx
= ∫Ω (S_adapt − L_decay + R_memory) dx − ∮∂Ω J_space·n dS.
```

QED.

### Interpretation

This is the first rigorous ACST Noether-like accounting equation.

The classical conservation law is recovered when:

```text
S_adapt = 0,
L_decay = 0,
R_memory = 0,
boundary flux = 0.
```

---

## 9. Discrete Ledger Error Bound for Euler Updates

Suppose the exact ledger derivative is

```text
dQ/dt = F(t).
```

Forward Euler updates:

```text
Q_{n+1} = Q_n + Δt F_n.
```

The discrete ledger is exact for the Euler model:

```text
Q_N − Q_0 − Δt Σ_{n=0}^{N-1} F_n = 0.
```

Compared with the continuous system, if `F` is differentiable and `|F'(t)|≤K`, the quadrature error satisfies

```text
| ∫0^T F(t)dt − ΔtΣF_n | ≤ (T K Δt)/2.
```

Therefore the continuous ledger error of a left-Riemann/Euler accounting scheme is first order:

```text
O(Δt).
```

This gives a testable numerical diagnostic.

---

## 10. ACST Applied to EPM Memory Charge

In EPM, memory obeys

```text
∂M/∂t = ξ|Φ|² − ρM.
```

Define memory charge:

```text
Q_M = ∫Ω M dx.
```

Then

```text
dQ_M/dt = ξ∫Ω |Φ|² dx − ρQ_M.
```

This is exactly ACST form:

```text
adaptive quantity = input from field amplitude − memory decay.
```

So EPM memory is not exactly conserved, but it is exactly accounted for.

---

## 11. ACST Applied to PMT Memory

In PMT, memory obeys

```text
∂M/∂t = ξ(∂θ/∂t)² − ρM.
```

Define

```text
Q_M = ∫Ω M dx.
```

Then

```text
dQ_M/dt = ξ∫Ω (∂θ/∂t)² dx − ρQ_M.
```

Thus PMT memory charge is produced by phase activity and decays at rate `ρ`.

This is a clean ACST law.

---

## 12. ACST Applied to ACFN Conductance Mass

For ACFN-style conductance

```text
dG/dt = α|I| − μG + λ|∇κ| + σM,
```

define conductance mass

```text
Q_G = ∫Ω G dx.
```

Then

```text
dQ_G/dt = α∫Ω |I| dx − μQ_G + λ∫Ω |∇κ| dx + σ∫Ω M dx.
```

This is another exact ACST accounting law.

---

## 13. Classification of ACST Quantities

### Exact invariant

```text
dC/dt = 0.
```

### Open balance law

```text
dC/dt = input − output.
```

### Adaptive conserved-like quantity

```text
dC_A/dt = input − decay + memory return.
```

### Quasi-invariant

```text
|dC_A/dt| ≤ ε
```

for the relevant time window.

### Topological invariant

Integer-valued quantity stable under continuous deformation, such as EPM winding:

```text
W = degree(exp(iψ)).
```

### Broken invariant

A formerly stable quantity whose drift is not bounded or whose topology changes.

---

## 14. What Is Solved So Far

### Proven

- positivity of active and memory reservoirs,
- exact ledger conservation,
- exact conservation as a limiting case,
- constant-input equilibrium,
- stability of the two-reservoir equilibrium,
- quasi-invariant drift bound,
- adaptive Noether integrated accounting law,
- discrete Euler ledger consistency,
- ACST accounting laws for EPM, PMT, and ACFN.

### Solved conditions

Reservoir equilibrium:

```text
C* = P0 / [ μ + sρ/(r+ρ) ]
```

```text
M* = sC*/(r+ρ)
```

Stability:

```text
μ(r+ρ)+sρ > 0.
```

Exact conservation limit:

```text
P=μ=ρ=0.
```

Quasi-invariant drift:

```text
|C_A(T)-C_A(0)| ≤ εT.
```

Adaptive Noether accounting:

```text
d/dt ∫Ω J^0 dx
= ∫Ω (S_adapt − L_decay + R_memory) dx − ∮∂Ω J_space·n dS.
```

---

## 15. What Is Still Open

1. A full variational derivation of ACST from generalized adaptive action principles.
2. A rigorous adaptive Noether theorem with memory kernels.
3. Classification of all invariant types across the nine-arm Canonical Core.
4. Best numerical diagnostics for quasi-invariant failure.
5. ACST laws for topology-changing events where winding changes.

---

## 16. Summary

The first solved core of ACST is:

```text
conservation does not disappear in adaptive systems;
it becomes ledgered through input, decay, storage, return, and boundary flux.
```

The flagship ACST equation is:

```text
∂_μ J^μ = S_adapt − L_decay + R_memory.
```

The most practical finite-dimensional equation is:

```text
dC/dt = P − μC − sC + rM
```

```text
dM/dt = sC − rM − ρM.
```

The core result is the exact ledger:

```text
C(t)+M(t) = C(0)+M(0) + input − true losses.
```

That is the first rigorous mathematical foundation of Adaptive Conservation and Symmetry Theory.
