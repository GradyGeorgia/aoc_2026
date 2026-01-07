def main():
    with open("./input.txt") as f:
        input = f.read().strip()

    ranges, ingredients = input.split("\n\n")
    # ingredients = [int(x) for x in ingredients.split("\n")]
    ranges = ranges.split("\n")
    ranges = [[int(x) for x in range.split("-")] for range in ranges]

    # total = 0
    # # for ingredient in ingredients:
    # #     if is_fresh(ingredient, ranges):
    # #         total += 1

    ranges.sort()
    # print(ranges)
    
    total = 0
    for i in range(1, len(ranges)):
        start1, end1 = ranges[i-1]
        start2, end2 = ranges[i]
        if start2 <= start1  <= end2 or start2 <= end1 <= end2 or start1 <= start2  <= end1 or start1 <= end2 <= end1:
           ranges[i] = (min(start1, start2), max(end1, end2))
        else:
            total += end1 - start1 + 1

    total += ranges[-1][1] - ranges[-1][0] + 1
    print(total)

def is_fresh(ingredient, ranges):
    for lower, upper in ranges:
        if lower <= ingredient <= upper:
            return True
    
    return False

if __name__ == "__main__":
    main()
