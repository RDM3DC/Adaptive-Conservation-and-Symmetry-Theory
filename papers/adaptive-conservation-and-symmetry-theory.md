# Adaptive Conservation and Symmetry Theory (ACST)

**Standalone White Paper**  
**Canonical Core Arm:** 09  
**Date:** 2026-05-25  
**Status:** Draft scaffold

---

## Abstract

Adaptive Conservation and Symmetry Theory (ACST) studies conservation-like quantities in systems that adapt, store memory, relax, and change geometry. Classical conservation laws often assume closed systems and exact symmetries. ACST generalizes this into adaptive accounting laws where invariants may leak, store, return, or persist only on specific time scales.

The central question is:

```text
what survives when everything adapts?
```

---

## 1. Motivation

In many physical and computational systems, exact conservation is not the most useful description. Adaptive systems may have:

- external input
- relaxation
- memory storage
- delayed memory return
- symmetry breaking
- history-dependent state variables

Instead of writing:

```text
dC/dt = 0
```

ACST begins with:

```text
dC_A/dt = input − decay + memory feedback
```

---

## 2. Core Adaptive Conservation Law

A prototype adaptive invariant law is:

```text
dC_A/dt = P_A − μC_A + σM
```

where:

- `C_A` is an adaptive conserved-like quantity
- `P_A` is production or input
- `μC_A` is decay, relaxation, or leakage
- `σM` is memory return
- `M` is memory density or stored history

Exact conservation is recovered when:

```text
P_A = 0
μ = 0
σ = 0
```

---

## 3. Adaptive Noether Form

A schematic adaptive Noether-like equation is:

```text
∂_μ J^μ = S_adapt − L_decay + R_memory
```

where:

- `J^μ` is a current
- `S_adapt` is an adaptive source
- `L_decay` is loss or relaxation
- `R_memory` is memory return

Classical conservation is the limiting case:

```text
∂_μ J^μ = 0
```

---

## 4. Adaptive Invariants

Possible ACST quantities include:

### Memory Charge

```text
Q_M = ∫ M dx
```

### Adaptive Conductance Mass

```text
Q_G = ∫ G dx
```

### Phase Winding

```text
W = (1/2πₐ)∮∇θ_R · dl
```

### Emergent Object Identity

```text
ID_EPM = (W, Q_M, localization, phase signature)
```

---

## 5. Leakage, Storage, and Return

ACST separates three effects:

```text
leakage  = loss from active state
storage  = transfer into memory
return   = memory feeding back later
```

A two-reservoir model is:

```text
dC_active/dt = P − μC_active − sC_active + rC_memory
```

```text
dC_memory/dt = sC_active − rC_memory − ρC_memory
```

---

## 6. Symmetry Classes

ACST may track adaptive versions of:

- time-translation symmetry
- spatial-translation symmetry
- phase-rotation symmetry
- scale symmetry
- topology-preserving symmetry

Each can generate an exact invariant in special limits and an adaptive invariant in more realistic settings.

---

## 7. Diagnostics

Given simulation data, track:

```text
Q_G = ∫G dx
Q_M = ∫M dx
W = loop winding
E_A = adaptive energy functional
```

A useful diagnostic is:

```text
leakage_error = |dC_A/dt − (input − decay + memory_return)|
```

Small leakage error means the adaptive conservation accounting is internally consistent.

---

## 8. Canonical Claim

ACST does not replace classical conservation laws.

The canonical claim is:

```text
ACST defines adaptive conservation laws for systems with memory, relaxation, phase structure, and geometry feedback.
```

Exact conservation appears as a limiting case.

---

## 9. Next Work

- Build minimal accounting examples
- Couple diagnostics to PMT simulations
- Couple diagnostics to EPM persistence metrics
- Define adaptive Noether examples
- Classify exact, quasi, and broken invariants
