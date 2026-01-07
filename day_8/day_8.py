import math
from disjoint_set import DisjointSet

NUM_CONNECTIONS = 1000

def main():
    with open("./input.txt") as f:
        input = f.read().strip()

    coords = input.split("\n")
    coords = [[int(x) for x in coord.split(",")] for coord in coords]
    
    distances = []
    for i in range(len(coords)):
        for j in range(i+1, len(coords)):
            coord1, coord2 = coords[i], coords[j]
            distance = get_distance(coord1, coord2)
            distances.append((distance, i, j))

    distances.sort()
    # distances = distances[:NUM_CONNECTIONS]
    distances = [(i, j) for _, i, j in distances]
    res = 0
    circuits = DisjointSet.from_iterable(range(0,len(coords)))
    for distance in distances:
        i, j = distance
        circuits.union(i, j)
        sizes = [len(group) for group in  circuits.itersets()]
        if len(sizes) == 1:
            res = coords[i][0] * coords[j][0]
            break


    # sizes = [len(group) for group in  circuits.itersets()]
    # sizes.sort()
    # res = sizes[-1] * sizes[-2] * sizes[-3]
    print(res)

def get_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2 + (coord1[2] - coord2[2])**2)

if __name__ == "__main__":
    main()
