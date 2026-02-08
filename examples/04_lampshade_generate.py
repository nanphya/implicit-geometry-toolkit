from implicitgeo.models.lampshade import generate_lampshade
import os

os.makedirs("assets/stl", exist_ok=True)
generate_lampshade("assets/stl/lampshade_gyroid.stl")
print("STL generated.")
