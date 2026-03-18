# PyRolL Rolling Simulation

Advanced rolling simulation work built on the open-source PyRolL framework,
developed alongside my M.Sc.

All notebooks include code, simulation outputs, plots, and engineering
interpretation — connecting classical metal forming theory to modern
simulation tools.

---

## Notebooks

| File | Topic | Key Concepts |
|------|-------|-------------|
| day01_pyroll_basics.ipynb | PyRolL setup & first simulation | Pass sequence, groove geometry, volume conservation |

> More notebooks added continuously as thesis work progresses.

---

## Engineering Context

- **Material:** C45 steel
- **Process:** IMF finishing sequence F1–F4
- **Models:** Hitchcock elastic roll deflection, slab analysis (disk elements),
  Freiberg flow stress model
- **Validation:** Le & Sutcliffe (2001) experimental foil rolling data
- **Framework:** PyRolL — open-source rolling simulation, TU Freiberg

---

## Topics Covered

- Pass sequence design — oval-round, groove geometry, pass design rules
- Thermomechanical analysis — roll force, strain rate, temperature evolution
- Hook architecture — 60 hooks, plugin system, tryfirst execution
- Elastic roll gap — Hitchcock model, influence function matrix (Eq. 23)
- Roll deflection profile — rigid vs elastic gap comparison
- Coupled solver — non-dimensional formulation, 4-iteration convergence
- Slab analysis — disk element method, neutral point location
- Newton-Raphson solver — neutral point convergence

---

## Stack

Python · PyRolL · Jupyter Notebooks · NumPy · Matplotlib

---

## Background

M.Sc. Metallic Materials Technology — TU Bergakademie Freiberg
Specialization: Metal Forming & Rolling Simulation
Tools: FEM (Abaqus), Siemens NX, PyRolL, Python
