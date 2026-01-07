import numpy as np

def main():
    with open("./input.txt") as f:
        input = f.read().strip()
    input = input.split("\n")

    totalJoltage = 0
    for bank in input:
        totalJoltage += calculateMaxJoltage(bank)

    print(totalJoltage)

def calculateMaxJoltage(bank):
    bank = [int(x) for x in list(bank)]
    maxJoltage = ""

    for i in range(12):
        currentDigitIndex = np.argmax(bank[:(len(bank)+i-11)])
        currentDigit = bank[currentDigitIndex]
        maxJoltage += str(currentDigit)
        bank = bank[currentDigitIndex+1:]
    
    return int(maxJoltage)

if __name__ == "__main__":
    main()