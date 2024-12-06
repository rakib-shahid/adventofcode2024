input_file = "input.txt"


# part 1
def p1():
    with open(input_file) as f:
        lines = f.read().splitlines()
        obstacles = set()
        curr = None
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        curr_dir = 0
        rows = len(lines)
        cols = len(lines[0])

        for row, line in enumerate(lines):
            for col, char in enumerate(line):
                if char == "^":
                    curr = (row, col)
                if char == "#":
                    obstacles.add((row, col))
        visited = set({curr})
        # simulate the walking
        while True:

            next_pos = (
                curr[0] + directions[curr_dir][0],
                curr[1] + directions[curr_dir][1],
            )
            if not (0 <= next_pos[0] < rows and 0 <= next_pos[1] < cols):
                break
            if next_pos in obstacles:
                curr_dir = (curr_dir + 1) % 4
                continue
            else:
                curr = next_pos
                visited.add(curr)

        print(len(visited))


# part 2
def p2():
    with open(input_file) as f:
        lines = f.read().splitlines()
        obstacles = set()
        start = None
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        rows = len(lines)
        cols = len(lines[0])

        for row, line in enumerate(lines):
            for col, char in enumerate(line):
                if char == "^":
                    start = (row, col)
                if char == "#":
                    obstacles.add((row, col))
        # LOL brute force
        possible_obstacles = set()
        for row, line in enumerate(lines):
            for col, char in enumerate(line):
                if char != "#" and (row, col) != start:
                    possible_obstacles.add((row, col))
        out = 0
        # simulate the walking
        for obstacle in possible_obstacles:
            obstacles.add(obstacle)
            curr = start
            curr_dir = 0
            visited = set()

            while True:
                state = (curr, curr_dir)
                if state in visited:
                    out += 1
                    break
                visited.add(state)

                next_pos = (
                    curr[0] + directions[curr_dir][0],
                    curr[1] + directions[curr_dir][1],
                )

                if not (0 <= next_pos[0] < rows and 0 <= next_pos[1] < cols):
                    break

                if next_pos in obstacles:
                    curr_dir = (curr_dir + 1) % 4
                else:
                    curr = next_pos

            obstacles.remove(obstacle)
        print(out)
        # print(len(visited))


p1()
p2()
