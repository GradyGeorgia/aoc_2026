import unittest
with open("./input.txt") as f:
    input = f.read().strip()

steps = input.split("\n")

current = 50
zero_count = 0

class testRotation(unittest.TestCase):
    def test_past_100(self):
        current, num_zeroes = rotation(50, "R52")

        self.assertEqual(current, 2)
        self.assertEqual(num_zeroes, 1)
    
    def test_rotate_to_100(self):
        current, num_zeroes = rotation(50, "R50")

        self.assertEqual(current, 0)
        self.assertEqual(num_zeroes, 1)
    
    def test_rotate_past_and_land_100(self):
        current, num_zeroes = rotation(50, "R150")

        self.assertEqual(current, 0)
        self.assertEqual(num_zeroes, 2)

    def test_past_0(self):
        current, num_zeroes = rotation(50, "L52")

        self.assertEqual(current, 98)
        self.assertEqual(num_zeroes, 1)
    
    def test_rotate_to_0(self):
        current, num_zeroes = rotation(50, "L50")

        self.assertEqual(current, 0)
        self.assertEqual(num_zeroes, 1)
    
    def test_rotate_past_and_land_0(self):
        current, num_zeroes = rotation(50, "L150")

        self.assertEqual(current, 0)
        self.assertEqual(num_zeroes, 2)
    
    def test_normal_rotation(self):
        current, num_zeroes = rotation(50, "L20")

        self.assertEqual(current, 30)
        self.assertEqual(num_zeroes, 0)
    
    def test_normal_rotation2(self):
        current, num_zeroes = rotation(50, "R20")

        self.assertEqual(current, 70)
        self.assertEqual(num_zeroes, 0)
    
    def test_start_at_zero_right(self):
        current, num_zeroes = rotation(0, "R1")

        self.assertEqual(current, 1)
        self.assertEqual(num_zeroes, 0)
    
    def test_start_at_zero_left(self):
        current, num_zeroes = rotation(0, "L1")

        self.assertEqual(current, 99)
        self.assertEqual(num_zeroes, 0)

def rotation(initial_value, step):
    rotation = int(step[1:])
    
    num_zeroes = 0
    #normalizes rotation
    num_zeroes += abs(rotation) // 100
    rotation = rotation % 100

    if step[0] == "L":
        rotation *= -1

    value = initial_value + rotation
    if (value <= 0 or value >= 100) and initial_value != 0:
        num_zeroes += 1

    value = value % 100

    return (value,num_zeroes)

def main():
    current = 50
    zero_count = 0
    
    for step in steps:
        current, new_zeroes = rotation(current, step)
        zero_count += new_zeroes
        print(step, current, new_zeroes)
    
    print(zero_count)
    

if __name__ == '__main__':
    #unittest.main()
    main()


