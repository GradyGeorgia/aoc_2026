import numpy as np

def main():
    with open("./input.txt") as f:
        input = f.read().strip()
    pairs = [[int(x) for x in line.split(",")] for line in input.split("\n")]

    res = 0
    for i in range(len(pairs)):
        for j in range(i + 1, len(pairs)):
            if is_valid(pairs[i], pairs[j], pairs):
                res = max(res, area(pairs[i], pairs[j]))
    print(res)

def area(coord1, coord2):
    return (1 + abs(coord1[0]-coord2[0])) * (1 + abs(coord1[1] - coord2[1]))

def is_valid(coord1, coord2, coords):
    y1, x1 = coord1
    y2, x2 = coord2
    
    for coord in coords:
        current_y, current_x = coord
        if min(x1, x2) <= current_x <= max(x1, x2):
            if min(y1, y2) <= current_y <= max(y1, y2):
                if coord != coord1 and coord != coord2:
                    return False
            
    return True

if __name__ == "__main__":
    main()