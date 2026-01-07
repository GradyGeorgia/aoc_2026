import numpy as np
from enum import Enum, auto

class Direction(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

class DirectionalLine:
    def __init__(self, coord1, coord2, direction):
        self.coord1 = coord1
        self.coord2 = coord2
        self.direction = direction

def main():
    with open("./input.txt") as f:
        input = f.read().strip()
    coords = [[int(x) for x in line.split(",")] for line in input.split("\n")]

    lines = coords_to_lines(coords)
    directional_lines = get_directional_lines(lines)
    h_ranges = get_h_ranges(directional_lines)
    
    t_lines = coords_to_lines(transpose_coords(coords))
    t_directional_lines = get_directional_lines(t_lines)
    v_ranges = get_h_ranges(t_directional_lines)

    res = 0
    for i in range(len(coords)):
        for j in range(i + 1, len(coords)):
            if is_valid(coords[i], coords[j], h_ranges, v_ranges):
                res = max(res, area(coords[i], coords[j]))
    print(res)

#hranges[y]->[(x1,x2)...]
#vranges[x]->[(y1,y2)...]
def get_h_ranges(directional_lines):
    pass

def transpose_coords(coords):
    new_coords = []
    for coord in coords:
        new_coords.append(coord[1], coord[0])

    return new_coords

def coords_to_lines(coords):
    lines = []
    for i in range(len(coords) - 1):
        lines.append((coords[i], coords[i + 1]))
    lines.append(coords[-1], coords[0])

    return lines

def get_directional_lines(lines):
    pass

def area(coord1, coord2):
    return (1 + abs(coord1[0]-coord2[0])) * (1 + abs(coord1[1] - coord2[1]))

def is_valid(coord1, coord2, h_ranges, v_ranges):
    # check if all 4 boundary lines are valid
    pass

if __name__ == "__main__":
    main()