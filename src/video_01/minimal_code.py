import pygfx as gfx

obj = gfx.Mesh(
    gfx.torus_knot_geometry(15, 2.5, 400, 16, 5, 3), 
    gfx.MeshPhongMaterial(color="red")
)

if __name__ == "__main__":
    gfx.show(obj)