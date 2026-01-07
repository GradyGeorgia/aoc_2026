import numpy as np

def main():
    # part 1
    # array = np.loadtxt("./input.txt", dtype = str)
    # array = array.T

    # total = 0
    # for problem in array:
    #     nums = problem[:-1].astype(int)
    #     op = problem[-1]
        
    #     if op == "+":
    #         total += np.sum(nums)
    #     else:
    #         total += np.prod(nums)

    # print(total)

    with open("./input.txt") as f:
        input = f.read()
    
    input = input.split("\n")
    nums = input[:-1]
    ops = input[-1].split()
    print(ops)
    nums = [list(line) for line in nums]
    array = np.array(nums).T
    total = 0

    op_idx = 0
    i = 0
    cur_nums = []

    while i < array.shape[0]:
        num = "".join(array[i])
        if not num.strip():
            if ops[op_idx] == "*":
                total += np.prod(cur_nums)
            else:
                total += np.sum(cur_nums)
            cur_nums = []
            op_idx += 1
        else:
            cur_nums.append(int(num.strip()))
        i += 1
    
    if ops[op_idx] == "*":
        total += np.prod(cur_nums)
    else:
        total += np.sum(cur_nums)
    print(total)

if __name__ == "__main__":
    main()
