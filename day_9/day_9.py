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
        new_coords.append((coord[1], coord[0]))

    return new_coords

def coords_to_lines(coords):
    lines = []
    for i in range(len(coords) - 1):
        lines.append((coords[i], coords[i + 1]))
    lines.append((coords[-1], coords[0]))

    return lines

def get_directional_lines(lines):
    def get_direction(line):
        y1, x1 = line[0]
        y2, x2 = line[1]
        if x1 == x2 :
            if y2 > y1:
                return Direction.DOWN
            return Direction.UP
        if x2 > x1:
            return Direction.RIGHT
        return Direction.LEFT
        
    def rotates_clockwise(line1, line2):
        dir1 = get_direction(line1)
        dir2 = get_direction(line2)
        if dir2.value > dir1.value or (dir1 == Direction.RIGHT and dir2 == Direction.UP):
            return True
        return False
    
    # gets the topmost horizontal line to begin
    topmost = 0
    for i, line in enumerate(lines):
        # is it horizontal
        if line[0][0] == line[1][0]:
            if line[0][0] <  lines[topmost][0]:
                topmost = i
                
    # topmost points in, compute directions sequentially    
    directional_lines = [DirectionalLine(lines[topmost][0], lines[topmost][1], Direction.DOWN)]
    for i in range(1, len(lines)):
        prev = lines[(topmost + i - 1) % len(lines)]
        next = lines[(topmost + i) % len(lines)]
        prev_direction = directional_lines[i - 1].direction
        if rotates_clockwise(prev, next):
            new_direction = Direction((prev_direction.value + 1) % 4)
        else:
            new_direction = Direction((prev_direction.value - 1) % 4)
        directional_lines.append(DirectionalLine(next[0], next[1], new_direction))
        
    return directional_lines

def area(coord1, coord2):
    return (1 + abs(coord1[0]-coord2[0])) * (1 + abs(coord1[1] - coord2[1]))

def is_valid(coord1, coord2, h_ranges, v_ranges):
    def range_list_contains(range_list, start, end):
        # Could optimize using bisect
        for range in range_list:
            if start >= range[0] and end <=range[1]:
                return True
        return False
    
    def vertical_boundary_is_valid(coord1, coord2, v_ranges):
        x = coord1[1]
        y1 = min(coord1[0], coord2[0])
        y2 = max(coord1[0], coord2[0])
        # x coordinate is not in map
        if x not in v_ranges:
            return False
        if not range_list_contains(v_ranges[x], y1, y2 + 1):
            return False
    
    def horizontal_boundary_is_valid(coord1, coord2, h_ranges):
        y = coord1[0]
        x1 = min(coord1[1], coord2[1])
        x2 = max(coord1[1], coord2[1])
        # x coordinate is not in map
        if y not in h_ranges:
            return False
        if not range_list_contains(h_ranges[y], x1, x2 + 1):
            return False
        
    # check if all 4 boundary lines are valid
    if not vertical_boundary_is_valid(coord1, coord2, v_ranges):
        return False
    if not vertical_boundary_is_valid(coord2, coord1, v_ranges):
        return False
    if not horizontal_boundary_is_valid(coord1, coord1, h_ranges):
        return False
    if not horizontal_boundary_is_valid(coord2, coord1, h_ranges):
        return False
    return True
if __name__ == "__main__":
    main()