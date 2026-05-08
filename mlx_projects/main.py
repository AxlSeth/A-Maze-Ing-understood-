from mlx import Mlx

m = Mlx()
mlx_ptr = m.mlx_init()
window = m.mlx_new_window(mlx_ptr, 1200, 800, "fory")

def exit_on_x(data):
    m.mlx_loop_exit(mlx_ptr)

def exit_on_esc(esc, data):
    if esc == 65307:
        m.mlx_loop_exit(mlx_ptr)

for row in range(200, 500):
    for col in range(200, 300):
        m.mlx_pixel_put(mlx_ptr, window, col, row, 0xFF0000)


m.mlx_hook(window, 33, 0, exit_on_x, None)
m.mlx_key_hook(window, exit_on_esc, None)

m.mlx_loop(mlx_ptr)
