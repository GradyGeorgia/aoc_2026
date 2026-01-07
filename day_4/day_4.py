def main():
    with open("./input.txt") as f:
        input = f.read().strip().split("\n")
    grid = [list(line) for line in input]
    # print(input)
    total = 0
    while True:
        numRemoved = remove_tp(grid)
        if not numRemoved:
            break
        total += numRemoved
    
    print(total)

def remove_tp(grid):
    def isValidIndex(cell):
        row, col = cell
        if not (0 <= row < len(grid)):
            return False
        if not (0 <= col < len(grid[0])):
            return False
        return True
    

    total = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "@":
                neighbors = getNeighbors(i,j)
                neighbors = filter(isValidIndex, neighbors)
                # print(list(neighbors))
                if len([n for n in neighbors if grid[n[0]][n[1]]=="@"]) < 4:
                    total += 1
                    grid[i][j] = "."
    return total

def getNeighbors(row, col):
    return [
        [row - 1, col - 1],
        [row + 0, col - 1],
        [row + 1, col - 1],
        [row - 1, col + 0],
        [row + 1, col + 0],
        [row - 1, col + 1],
        [row + 0, col + 1],
        [row + 1, col + 1],
    ]


    

if __name__ == "__main__":
    main()
    # x = 3
    # print(5 > x > 1)

