def main():
    with open("./input.txt") as f:
        input = f.read().strip()
    pairs = [[int(x) for x in line.split(",")] for line in input.split("\n")]

    # lines = []
    # for i in range(len(pairs) - 1):
    #     lines.append((pairs[i], pairs[i + 1]))
    # lines.append((pairs[0], pairs[-1]))
    # print(lines)

    res = 0
    for i in range(len(pairs)):
        for j in range(i + 1, len(pairs)):
            if is_valid(pairs[i], pairs[j], pairs):
                res = max(res, area(pairs[i], pairs[j]))
    print(res)

def area(coord1, coord2):
    return (1 + abs(coord1[0]-coord2[0])) * (1 + abs(coord1[1] - coord2[1]))

def intersect(lineA, lineB):
    a1, a2 = lineA
    b1, b2 = lineB

    horizontala = a1[0] == a2[0]
    horizontalb = b1[0] == b2[0]

    # parallel lines NEVER intersect (or always)
    if horizontala == horizontalb:
        return False
    
    h1, h2 = lineA if horizontala else lineB
    v1, v2 = lineB if horizontala else lineA
    
    h1y, h1x = h1
    h2y, h2x = h2

    v1y, v1x = v1
    v2y, v2x = v2
    if  (min(v1y, v2y) < h1y < max(v1y, v2y)) and (min(h1x, h2x) < v1x <  max(h1x, h2x)):
        return True
    
    return False


def is_valid(coord1, coord2, coords):
    y1, x1 = coord1
    y2, x2 = coord2
    
    for coord in coords:
        current_y, current_x = coord
        if min(x1, x2) < current_x < max(x1, x2):
            if min(y1, y2) < current_y < max(y1, y2):
                return False
            
    return True

if __name__ == "__main__":
    #same line
    l1 = [(0,0), (0,1)]
    l2 = [(0,0), (0,1)]
    assert not intersect(l1,l2)

    #vertical, horizontal cross
    l1 = [(1,0), (1,2)]
    l2 = [(0,1), (2,1)]
    assert intersect(l1,l2)

    #endpoints touch
    l1 = [(1,0), (1,2)]
    l2 = [(1,0), (2,0)]
    assert not intersect(l1,l2)

    #parallel
    l1 = [(0,0), (0,2)]
    l2 = [(2,0), (2,2)]
    assert not intersect(l1,l2)

    l1 = [(0,0), (2,0)]
    l2 = [(0,2), (2,2)]
    assert not intersect(l1,l2)

    #not intersect
    l1 = [(0,0), (2,0)]
    l2 = [(1,1), (1,4)]
    assert not intersect(l1,l2)

    main()