def main():
    with open("./input.txt") as f:
        input = f.read().strip().split("\n")
    
    beams = [0] * len(input[0])
    beams[input[0].index("S")] = 1

    for line in input[1:]:
        newBeams = [0] * len(input[0])
        for i in range(len(beams)):
            if line[i] == "^":
                newBeams[i-1] += beams[i]
                newBeams[i+1] += beams[i]
            else:
                newBeams[i] += beams[i]
        beams = newBeams
    
    print(sum(beams))

if __name__ == "__main__":
    main()
