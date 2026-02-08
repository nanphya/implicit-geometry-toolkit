# Implicit Geometry Toolkit

Practical implicit-geometry (SDF) toolkit for **3D printing & lattice design**.
Focus: **SDF → meshing → STL**, with parametric TPMS / Gyroid demos.

## Features
- SDF primitives & smooth boolean
- TPMS (Gyroid)
- Marching Cubes meshing
- Printable parametric **Gyroid Lampshade**

## Quickstart
```bash
pip install -e .
python examples/04_lampshade_generate.py
```
This generates `assets/stl/lampshade_gyroid.stl`.

## Roadmap
- Mesh repair & simplification
- Adaptive sampling
- C++ geometry kernel (CGAL / Eigen)
