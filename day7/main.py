from functools import lru_cache

input_file = "input.txt"


@lru_cache(None)  # Memoization to cache intermediate results
def bt(total, values, value_index, target):
    if total == target and value_index == len(values):
        return True
    if value_index >= len(values):  # Stop if all values are used and target not reached
        return False

    # Explore the next value with operations
    current_value = values[value_index]
    if bt(total * current_value, values, value_index + 1, target):
        return True
    if bt(total + current_value, values, value_index + 1, target):
        return True

    return False


@lru_cache(None)
def bt2(total, values, value_index, target):
    if total == target and value_index == len(values):
        return True
    if value_index >= len(values):  # Stop if all values are used and target not reached
        return False

    # Explore the next value with operations
    current_value = values[value_index]
    if bt2(total * current_value, values, value_index + 1, target):
        return True
    if bt2(total + current_value, values, value_index + 1, target):
        return True
    new_total = total * (10 ** len(str(current_value))) + current_value
    if bt2(new_total, values, value_index + 1, target):
        return True

    return False


# part 1
def p1():
    with open(input_file) as f:
        out = 0
        lines = f.read().splitlines()
        for line in lines:
            contents = line.split()
            target = int(contents[0][:-1])

            values = tuple(int(x) for x in contents[1:])  # Convert to tuple

            # Use backtracking to check if any are valid
            if bt(values[0], values, 1, target):
                out += target
        print(out)


# part 2
def p2():
    with open(input_file) as f:
        out = 0
        lines = f.read().splitlines()
        for line in lines:
            contents = line.split()
            target = int(contents[0][:-1])

            values = tuple(int(x) for x in contents[1:])  # Convert to tuple

            # Use backtracking to check if any are valid
            if bt2(values[0], values, 1, target):
                out += target
        print(out)


p1()
p2()
