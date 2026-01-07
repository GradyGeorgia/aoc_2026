from enum import Enum, auto
import unittest

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
    
    # t_lines = coords_to_lines(transpose_coords(coords))
    # t_directional_lines = get_directional_lines(t_lines)
    # v_ranges = get_h_ranges(t_directional_lines)

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
            if y_coord not in h_directional_points:
                    h_directional_points[y_coord] = []
            h_directional_points[y_coord].append((min(coord1[1], coord2[1]), Direction.RIGHT))
            h_directional_points[y_coord].append((max(coord1[1], coord2[1]), Direction.LEFT))
            
    # create ranges
    h_ranges = {} # h_ranges[y]->[(x1,x2)...]
    for y_coord in h_directional_points:
        directional_points = h_directional_points[y_coord]
        directional_points.sort(key=lambda p: (p[0]))
        print(directional_points)

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
        if dir2.value > dir1.value or (dir1 == Direction.LEFT and dir2 == Direction.UP):
            return True
        return False
    
    # gets the topmost horizontal line to begin
    topmost = 0
    for i, line in enumerate(lines):
        # is it horizontal
        if line[0][0] == line[1][0]:
            if line[0][0] <  lines[topmost][0][0]:
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

        print(prev, next, new_direction)
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
class Test(unittest.TestCase):
    def test_directional_lines(self):
        pass

    def test_example_input(self):
        input = '''7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3'''.strip()
        coords = [[int(x) for x in line.split(",")] for line in input.split("\n")]
        lines = coords_to_lines(coords)
        directional_lines = get_directional_lines(lines)
        h_ranges = get_h_ranges(directional_lines)
        assert(0 not in h_ranges)
        assert(h_ranges[1][0] == (7,11))
        assert(h_ranges[2][0] == (7,11))
        assert(h_ranges[3][0] == (2,11))
        assert(h_ranges[4][0] == (2,11))
        assert(h_ranges[5][0] == (2,11))
        assert(h_ranges[6][0] == (9,11))
        assert(h_ranges[7][0] == (9,11))
        assert(8 not in h_ranges)

    def test_example_input_vertical(self):
        input = '''7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3'''.strip()
        coords = [[int(x) for x in line.split(",")] for line in input.split("\n")]
        t_lines = coords_to_lines(transpose_coords(coords))
        t_directional_lines = get_directional_lines(t_lines)
        v_ranges = get_h_ranges(t_directional_lines)
        assert(0 not in v_ranges)
        assert(1 not in v_ranges)
        assert(v_ranges[2][0] == (3,5))
        assert(v_ranges[3][0] == (3,5))
        assert(v_ranges[4][0] == (3,5))
        assert(v_ranges[5][0] == (3,5))
        assert(v_ranges[6][0] == (3,5))
        assert(v_ranges[7][0] == (1,5))
        assert(v_ranges[8][0] == (1,5))
        assert(v_ranges[9][0] == (1,7))
        assert(v_ranges[10][0] == (1,7))
        assert(v_ranges[11][0] == (1,7))
        assert(12 not in v_ranges)

if __name__ == "__main__":
    # main()
    unittest.main()