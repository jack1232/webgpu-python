import pygfx as gfx
import imageio.v3 as iio

def create_cubemap():
    img = iio.imread("imageio:meadow_cube.jpg")
    cube_size = img.shape[1]
    img.shape = 6, cube_size, cube_size, img.shape[-1]
    env_static = gfx.Texture(
        img, dim=2, size=(cube_size, cube_size, 6), generate_mipmaps=True
    )
    env_dynamic = gfx.Texture(
        dim=2, size=(512, 512, 6), format="rgba8unorm", generate_mipmaps=True
    )
    return env_static, env_dynamic