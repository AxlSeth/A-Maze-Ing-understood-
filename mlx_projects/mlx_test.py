from mlx import Mlx

m = Mlx()

mlx_ptr = m.mlx_init()
win_ptr = m.mlx_new_window(mlx_ptr, 1500, 800, "haha")


img = m.mlx_new_image(mlx_ptr, 500, 200)
data, bpp, line_len, endian = m.mlx_get_data_addr(img)


def exit(data):
    m.mlx_loop_exit(mlx_ptr)


def put_pixel(x, y, color):
    data[(x * 4 + y * line_len):(x * 4 + y * line_len) + 4] = color.to_bytes(4, "little")


m.mlx_sync(mlx_ptr, Mlx.SYNC_IMAGE_WRITABLE, img)
for y in range(0, 200):
    for x in range(0, 500):
        put_pixel(x, y, 0xFFFF0000)
m.mlx_put_image_to_window(mlx_ptr, win_ptr, img, 0, 0)
m.mlx_put_image_to_window(mlx_ptr, win_ptr, img, 0, 0)
m.mlx_hook(win_ptr, 33, 0, exit, None)
m.mlx_loop(mlx_ptr)
