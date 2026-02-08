import numpy as np
from skimage import measure
from stl import mesh

def gyroid(x, y, z):
    return np.sin(x)*np.cos(y) + np.sin(y)*np.cos(z) + np.sin(z)*np.cos(x)

def generate_lampshade(
    out_path,
    height=120.0,
    radius=55.0,
    shell=2.2,
    cells_around=6,
    cells_height=7,
    level=0.35,
    grid=180
):
    pad = 2.0
    xs = np.linspace(-(radius+pad), radius+pad, grid)
    ys = np.linspace(-(radius+pad), radius+pad, grid)
    zs = np.linspace(0, height, grid)
    X,Y,Z = np.meshgrid(xs,ys,zs,indexing="ij")
    R = np.sqrt(X*X+Y*Y)

    inner = radius-shell
    inside = (R<=radius)&(R>=inner)

    kxy = cells_around/radius
    kz = 2*np.pi*cells_height/height
    g = gyroid(X*kxy, Y*kxy, Z*kz)

    solid = inside & (np.abs(g)<=level)
    vol = solid.astype(np.float32)

    spacing = (
        (xs[-1]-xs[0])/(grid-1),
        (ys[-1]-ys[0])/(grid-1),
        (zs[-1]-zs[0])/(grid-1)
    )
    verts, faces, _, _ = measure.marching_cubes(vol, 0.5, spacing=spacing)
    verts[:,0]+=xs[0]; verts[:,1]+=ys[0]; verts[:,2]+=zs[0]

    m = mesh.Mesh(np.zeros(len(faces), dtype=mesh.Mesh.dtype))
    m.vectors[:] = verts[faces]
    m.save(out_path)
