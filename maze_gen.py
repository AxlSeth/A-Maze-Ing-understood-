import random
import vars


class Cell():
    def __init__(self) -> None:
        self.walls = {"n": 1,
                      "s": 1,
                      "e": 1,
                      "w": 1}
        self.is_checked: int = 0
        self.is_pattern: int = 0


class MazeGenerator():
    def __init__(self) -> None:
        self.width = vars.WIDTH
        self.height = vars.HEIGHT

    def apply_pattern(self,
                      maze: list[list[Cell]]) -> None:
        oy: int = (len(maze) - len(vars.PATTERN)) // 2
        ox: int = (len(maze[0]) - len(vars.PATTERN[0])) // 2
        for py in range(len(vars.PATTERN)):
            for px in range(len(vars.PATTERN[0])):
                if vars.PATTERN[py][px] == 1:
                    maze[oy + py][ox + px].is_pattern = 1

    def get_neighbors(self,
                      maze: list[list[Cell]],
                      y: int,
                      x: int) -> list[tuple[str, int, int]]:
        valid_directions: list[tuple[str, int, int]] = []
        if ((y + 1) < vars.HEIGHT and
            maze[y + 1][x].is_checked == 0 and
                maze[y + 1][x].is_pattern == 0):
            valid_directions.append(("s", y + 1, x))
        if ((y - 1) >= 0 and
            maze[y - 1][x].is_checked == 0 and
                maze[y - 1][x].is_pattern == 0):
            valid_directions.append(("n", y - 1, x))
        if ((x + 1) < vars.WIDTH and
            maze[y][x + 1].is_checked == 0 and
                maze[y][x + 1].is_pattern == 0):
            valid_directions.append(("e", y, x + 1))
        if ((x - 1) >= 0 and
            maze[y][x - 1].is_checked == 0 and
                maze[y][x - 1].is_pattern == 0):
            valid_directions.append(("w", y, x - 1))
        return (valid_directions)

    def create_paths(self, maze: list[list[Cell]], on_carve=None) -> None:
        maze[0][0].is_checked = 1
        stack: list[tuple[int, int]] = [(0, 0)]

        while stack:
            y, x = stack[-1]
            valid_directions = self.get_neighbors(maze, y, x)
            if len(valid_directions) == 0:
                stack.pop()
            else:
                direction, ny, nx = random.choice(valid_directions)
                maze[ny][nx].is_checked = 1
                maze[y][x].walls[direction] = 0
                maze[ny][nx].walls[vars.OPPOSITES[direction]] = 0
                if on_carve:
                    on_carve(y, x, direction)
                stack.append((ny, nx))

    def generate(self, width: int, height: int, on_carve=None) -> list[list[Cell]]:
        maze: list[list[Cell]] = []
        for y in range(height):
            row: list[Cell] = []
            for x in range(width):
                row.append(Cell())
            maze.append(row)
        if vars.HEIGHT > len(vars.PATTERN) and vars.WIDTH > len(vars.PATTERN[0]):
            self.apply_pattern(maze)
        self.create_paths(maze, on_carve)
        return maze
