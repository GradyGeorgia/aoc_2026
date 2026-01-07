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
    h_directional_points = {} # h_directional_points[y] -> [(x1, RIGHT),...]

    # populate h_directional_points
    for directional_line in directional_lines:
        coord1, coord2, direction = directional_line.coord1, directional_line.coord2, directional_line.direction

        # populate vertical lines
        if direction == Direction.RIGHT or direction == Direction.LEFT:
            x_coord = coord1[1]
            for y in range(min(coord1[0], coord2[0]), max(coord1[0], coord2[0])):
                if y not in h_directional_points:
                    h_directional_points[y] = []
                h_directional_points[y].append((x_coord, direction))

        # populate horizontal lines
        if direction == Direction.UP or direction == Direction.DOWN:
            y_coord = coord1[0]
            h_directional_points[y_coord].append((min(coord1[1], coord2[1]), Direction.RIGHT))
            h_directional_points[y_coord].append((max(coord1[1], coord2[1]), Direction.LEFT))
            
    # create ranges
    h_ranges = {} # h_ranges[y]->[(x1,x2)...]
    for y_coord in h_directional_points:
        directional_points = h_directional_points[y_coord]
        directional_points.sort()

        # create initial ranges
        ranges = []
        for i in range(len(directional_points)):
            current_directional_point = directional_points[i]
            if current_directional_point[1] == Direction.RIGHT:
                ranges.append((current_directional_point[0], directional_points[i + 1][0]))
            elif current_directional_point[1] == Direction.LEFT:
                ranges.append((directional_points[i - 1][0], current_directional_point[0]))

        # merge ranges
        merged_ranges = []
        for i in range(1, len(ranges)):
            start1, end1 = ranges[i-1]
            start2, end2 = ranges[i]
            range_1_within_range_2 = (start2 - 1 <= start1 <= end2 + 1) or (start2 - 1 <= end1 <= end2 + 1)
            range_2_within_range_1 = (start1 - 1 <= start2 <= end1 + 1) or (start1 - 1 <= end2 <= end1 + 1)
            if range_1_within_range_2 or range_2_within_range_1:
                ranges[i] = (min(start1, start2), max(end1, end2))
            else:
                merged_ranges.append(ranges[i-1])
        merged_ranges.append(ranges[-1])

        h_ranges[y_coord] = merged_ranges

    return h_ranges

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
    pass

def area(coord1, coord2):
    return (1 + abs(coord1[0]-coord2[0])) * (1 + abs(coord1[1] - coord2[1]))

def is_valid(coord1, coord2, h_ranges, v_ranges):
    # check if all 4 boundary lines are valid
    pass

if __name__ == "__main__":
    main()