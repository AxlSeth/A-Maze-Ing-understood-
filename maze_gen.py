import random

WIDTH: int = 21
HEIGHT: int = 12


OPPOSITES: dict[str, str] = {"n":"s",
                             "s":"n",
                             "e":"w",
                             "w":"e"}


PATTERN: list[list[int]] = [[0,1,0,0,0,1,1,1],
                            [0,1,0,0,0,0,0,1],
                            [0,1,0,1,0,1,1,1],
                            [0,1,1,1,0,1,0,0],
                            [0,0,0,1,0,1,1,1]]
#center of the 42 pattern is [y=2, x=4]


MIN_WIDTH: int = len(PATTERN[0]) + 2
MIN_HEIGHT: int = len(PATTERN) + 2

#-------------------

class Cell():
    def __init__(self) -> None:
        self.walls = {"n" : 1,
                      "s" : 1,
                      "e" : 1,
                      "w" : 1}
        self.is_checked: int = 0
        self.is_pattern: int = 0

#------------------

def display_maze(maze: list[list[Cell]]):
    height: int = len(maze)
    width: int = len(maze[0])

    for y in range(height):
        for x in range(width):
            print("+", end="")
            if maze[y][x].walls["n"] == 1:
                print("---", end="")
            else:
                print("   ", end="")
        print("+")

        for x in range(width):
            if maze[y][x].walls["w"] == 1:
                if maze[y][x].is_pattern == 1:
                    print("| # ", end="")
                else:
                    print("|   ", end="")
            else:
                print("    ", end="")
        print("|")

    for x in range(width):
        print("+", end="")
        if maze[height - 1][x].walls["s"] == 1:
            print("---", end="")
        else:
            print("   ", end="")
    print("+")

#--------------------

class MazeGenerator():
    def __init__ (self) -> None:
        self.width = WIDTH
        self.height = HEIGHT


    def apply_pattern(self,
                      maze: list[list[Cell]]) -> None:
        oy: int = (len(maze) - len(PATTERN)) // 2
        ox: int = (len(maze[0]) - len(PATTERN[0])) // 2
        for py in range(len(PATTERN)):
            for px in range(len(PATTERN[0])):
                if PATTERN[py][px] == 1:
                    maze[oy + py][ox + px].is_pattern = 1 


    def get_neighbors(self,
                      maze: list[list[Cell]],
                      y: int,
                      x: int) -> list[tuple[str ,int , int]]:
        valid_directions: list[tuple[str, int, int]] = []
        if ((y + 1) < HEIGHT and
            maze[y + 1][x].is_checked == 0 and
            maze[y + 1][x].is_pattern == 0):
            valid_directions.append(("s" ,y + 1 , x))
        if ((y - 1) >= 0 and
            maze[y - 1][x].is_checked == 0 and
            maze[y - 1][x].is_pattern == 0):
            valid_directions.append(("n" ,y - 1 , x))
        if ((x + 1) < WIDTH and
            maze[y][x + 1].is_checked == 0 and
            maze[y][x + 1].is_pattern == 0):
            valid_directions.append(("e", y, x + 1))
        if ((x - 1) >= 0 and
            maze[y][x - 1].is_checked == 0 and
            maze[y][x - 1].is_pattern == 0):
            valid_directions.append(("w", y, x - 1))
        return (valid_directions)

#for every cell,
#look for every valid direction(s) i can to go to
#choose one random direction to go to
#remove the wall going to that direction
#update the coordinates according to the new directions and repeat the loop
#
#What you have vs what you need
#Right now create_paths loops over every cell in order and marks it visited. That's just a nested loop — no stack, no backtracking, no random carving. The maze would have all cells visited but no walls opened, so nothing would be connected.
#The actual structure of create_paths
#It needs these ingredients in this order:
#First, pick a starting cell — (y=0, x=0) is fine. Mark it visited. Create a stack as an empty list and push (0, 0) onto it.
#Then enter a while loop that runs while the stack is not empty.
#Inside the loop: peek at the top with stack[-1] and unpack it into y, x. Call get_neighbors with those coordinates. Shuffle the result with random.shuffle().
#If the neighbors list is not empty: take the first tuple, unpack it into direction, ny, nx. Open the wall on the current cell using maze[y][x].walls[direction] = 0. Open the opposite wall on the neighbor using maze[ny][nx].walls[OPPOSITES[direction]] = 0. Mark the neighbor visited with maze[ny][nx].is_checked = 1. Push (ny, nx) onto the stack.
#If the neighbors list is empty: just call stack.pop().
#That's the complete DFS. Notice Cell no longer needs row and col stored on it — the coordinates come from the stack, not from the cell itself. You can remove those attributes from Cell.__init__ and go back to Cell(y, x) just being Cell() with no parameters.
#Try writing it now — it's about 12 lines of actual logic inside the while loop.


    def create_paths(self,
                     maze: list[list[Cell]]) -> None:
        ...
        

    def generate(self,
                 width: int,
                 height: int) -> list[list[Cell]]:
        maze: list[list[Cell]] = []

        for y in range(height):
            row: list[Cell] = []
            for x in range(width):
                cell: Cell = Cell()
                row.append(cell)
            maze.append(row)
        self.apply_pattern(maze)
        display_maze(maze)
        return (maze)
            
#----------------------
def main() -> None:
    maze_gen: MazeGenerator = MazeGenerator()
    maze_gen.generate(WIDTH, HEIGHT)

if __name__ == "__main__":
    main()
