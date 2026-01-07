
#123123
def is_invalid(id: int):
    id = str(id)
    for l in range(1, (len(id) // 2)+1):
        if len(id) % l == 0:
            if is_invalid_l(id, l):
                return True
    return False

def is_invalid_l(id: str, l: int):
    for i in range(l, len(id), l):
        pattern = id[:l]
        if id[i:i+l] != pattern:
            return False
    return True

def main():
    with open("./input.txt") as f:
        input = f.read().strip()

    res = 0
    ranges = input.split(',')
    for range_text in ranges:
        start, stop = range_text.split('-')
        for i in range(int(start), int(stop)+1):
            if is_invalid(i):
                res += i
                print("invalid:", i)

    print(res)
        
if __name__ == "__main__":
    #1227775554
    main()

    