import sys
import pygfx as gfx
from pygfx.utils.cube_camera import CubeCamera
import pylinalg as la

sys.path.append(".")
import common.helper as hp

scene = gfx.Scene()

env_static, env_dynamic = hp.create_cubemap()
cube_camera = CubeCamera(env_dynamic)

background = gfx.Background(None, gfx.BackgroundSkyboxMaterial(map=env_static))
scene.add(background)

material = gfx.MeshStandardMaterial(roughness=0.05, metalness=1)
material.side = "Front"
material.env_map = env_static
#material.env_mapping_mode = "CUBE-REFRACTION"

obj = gfx.Mesh(gfx.torus_knot_geometry(15, 2.5, 300, 16, 5, 3), material)
#obj = gfx.Mesh(gfx.box_geometry(15, 15, 15), material)

scene.add(obj)
cube_camera.render(scene)

def animate():    
    #rot = la.quat_from_euler((0.005, 0.01, 0.01))
    rot = la.quat_from_euler(0.005, order="Y")
    obj.local.rotation = la.quat_mul(rot, obj.local.rotation)
    rot1 = la.quat_from_euler(0.002, order="Y")
    background.local.rotation = la.quat_mul(rot1, background.local.rotation)

if __name__ == "__main__":
    gfx.show(scene, before_render=animate)
  
         