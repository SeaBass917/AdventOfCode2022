import enum
import os
from time import sleep

class Mats(enum.Enum):
    air = 0
    rock = 1
    sand = 2

def visualize_grid(grid, filename_out=None):
    os.system('cls')
    str_out = "="*(len(grid[0])+4) + "\n"
    for row in grid:
        str_out += "| "
        for ele in row:
            if ele == Mats.sand:
                str_out += "o"
            elif ele == Mats.rock:
                str_out += "#"
            elif ele == Mats.air:
                str_out += " "
        str_out+=" |\n"
    
    str_out += "="*(len(grid[0])+4)
    
    if filename_out:
        with open(filename_out, mode='w') as fp_out:
            fp_out.write(str_out)
    else:
        for line in str_out.split("\n"):
            print(line)

def part_1():
    with open("data/data_14") as fp_in:
        buffer = fp_in.read()
        data = [[[int(num) for num in pair.split(",")] for pair in line.split(" -> ")] for line in buffer.split("\n")]
        
        # determine the boundaries necessary for simulation space
        pair0 = data[0][0]
        xmin, ymin, xmax, ymax = pair0[0], pair0[1], pair0[0], pair0[1]

        for path in data:
            for x, y in path:
                xmin = min(xmin, x)
                ymin = min(ymin, y)
                xmax = max(xmax, x)
                ymax = max(ymax, y)
        
        dx = xmax-xmin
        dy = ymax

        grid = [[Mats.air for _ in range(dx+1)] for _ in range(dy+1)]

        # Set up the rocks for the sim.
        for path in data:
            for (x1, y1), (x2, y2) in zip(path[:-1], path[1:]):
                if x2 < x1: x2,x1 = x1,x2
                if y2 < y1: y2,y1 = y1,y2
                if x1 == x2:
                    for y in range(y1, y2+1):
                        grid[y][x1-xmin] = Mats.rock
                elif y1 == y2:
                    for x in range(x1, x2+1):
                        grid[y1][x-xmin] = Mats.rock
                else:
                    raise RuntimeError("YOU DIDN'T TELL ME THERE'D BE DIAGONALS!")

        def time_step(row, col, grid):
            # Below
            if grid[row+1][col] == Mats.air:
                time_step(row+1, col, grid)
            #      below_left
            elif grid[row+1][col-1] == Mats.air:
                time_step(row+1, col-1, grid)
            #      below_right
            elif grid[row+1][col+1] == Mats.air:
                time_step(row+1, col+1, grid)
            else:
                grid[row][col] = Mats.sand
                return

        col_enter = 500 - xmin
        while True:
            try:
                # sleep(0.01)
                # visualize_grid(grid)
                time_step(-1, col_enter, grid)
            except IndexError:
                break

        sand_cnt = 0
        for row in grid:
            for ele in row:
                if ele == Mats.sand:
                    sand_cnt += 1

        print( "Part 1:", sand_cnt )

def part_2():
    with open("data/data_14") as fp_in:
        buffer = fp_in.read()
        data = [[[int(num) for num in pair.split(",")] for pair in line.split(" -> ")] for line in buffer.split("\n")]
        
        # determine the boundaries necessary for simulation space
        pair0 = data[0][0]
        xmin, ymin, xmax, ymax = pair0[0], pair0[1], pair0[0], pair0[1]

        for path in data:
            for x, y in path:
                xmin = min(xmin, x)
                ymin = min(ymin, y)
                xmax = max(xmax, x)
                ymax = max(ymax, y)
        
        dx = xmax-xmin
        dy = ymax

        grid = [[Mats.air for _ in range((dx*4)+1)] for _ in range(dy+3)]

        # Set up the rocks for the sim.
        for path in data:
            for (x1, y1), (x2, y2) in zip(path[:-1], path[1:]):
                if x2 < x1: x2,x1 = x1,x2
                if y2 < y1: y2,y1 = y1,y2
                if x1 == x2:
                    for y in range(y1, y2+1):
                        grid[y][x1-xmin+int(3*dx/2)+1] = Mats.rock
                elif y1 == y2:
                    for x in range(x1, x2+1):
                        grid[y1][x-xmin+int(3*dx/2)+1] = Mats.rock
                else:
                    raise RuntimeError("YOU DIDN'T TELL ME THERE'D BE DIAGONALS!")

        grid[-1] = [Mats.rock for _ in grid[-1]]

        def time_step(row, col, grid):
            # Below
            if grid[row+1][col] == Mats.air:
                time_step(row+1, col, grid)
            #      below_left
            elif grid[row+1][col-1] == Mats.air:
                time_step(row+1, col-1, grid)
            #      below_right
            elif grid[row+1][col+1] == Mats.air:
                time_step(row+1, col+1, grid)
            else:
                grid[row][col] = Mats.sand
                if row == 0: 
                    raise IndexError("Solution")
                return

        col_enter = (500 - xmin)+int(3*dx/2)+1
        while True:
            try:
                # sleep(0.01)
                # visualize_grid(grid)
                time_step(-1, col_enter, grid)
            except IndexError:
                break

        sand_cnt = 0
        for row in grid:
            for ele in row:
                if ele == Mats.sand:
                    sand_cnt += 1

        print( "Part 2:", sand_cnt )

def main():
    part_1()
    part_2()

if __name__ == "__main__":
    main()