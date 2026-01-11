def main():
    with open("./input.txt") as f:
        input = f.read().strip()

    input = input.split("\n")
    machines = []
    for line in input:
        line = line.split(" ")
        line = [x[1:-1] for x in line]

        diagram = list(line[0])[::-1]
        diagram = "".join(["0" if x == "." else "1" for x in diagram])
        diagram = int(diagram, 2)
        
        buttons = line[1:-1]
        buttons = [[int(x) for x in button.split(",")] for button in buttons]

        joltages = tuple([int(x) for x in line[-1].split(",")])

        machine = (diagram, buttons, joltages)
        machines.append(machine)

    total = 0
    for machine in machines:
        # total += solve_machine_part_1(machine[0], machine[1])
        total += solve_machine_part_2(machine[2], machine[1])
    print(total)

def press_button(state, button):
    for pos in button:
        state = state ^ (1 << pos)
    return state

def solve_machine_part_1(goal, buttons):
    seen = {0}
    states = {0}
    steps = 0
    while True:
        steps += 1
        new_states = set()
        for state in states:
            for button in buttons:
                result = press_button(state, button)
                if result == goal:
                    return steps
                new_states.add(result)
        states = new_states - seen
        seen.update(new_states)

def solve_machine_part_2(goal, buttons):
    pass

if __name__ == "__main__":
    main()
