from mlx import Mlx

m = Mlx()

mlx_ptr = m.mlx_init()
win_ptr = m.mlx_new_window(mlx_ptr, 500, 500, "haha")
img_ptr = m.mlx_new_image(mlx_ptr, 100, 100)

def close_x(data):
    m.mlx_loop_exit(mlx_ptr)

data, bpp, line_len, endian = m.mlx_get_data_addr(img_ptr)
print(m.mlx_get_data_addr(img_ptr))

def put_pixel(x , y, color):
    offset = x * (bpp // 8) + y * line_len
    data[offset: offset + (bpp // 8)] = color.to_bytes((bpp // 8), "little")

for i in range(100):
    for j in range(100):
        put_pixel(i, j, 0xFFFFFFFF)

m.mlx_put_image_to_window(mlx_ptr, win_ptr, img_ptr, 20, 20)
m.mlx_hook(win_ptr, 33, 0, close_x, None)
m.mlx_loop(mlx_ptr)
