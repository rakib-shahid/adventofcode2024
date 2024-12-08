def distance(p1, p2):
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2


def p1():
    with open(input_file) as f:
        lines = f.read().splitlines()
        points = {}
        antinodes = set()

        for row in range(len(lines)):
            for col in range(len(lines[row])):
                if lines[row][col].isalnum():
                    if lines[row][col] not in points:
                        points[lines[row][col]] = []
                    points[lines[row][col]].append((row, col))

        for node in points:
            positions = points[node]
            for i in range(len(positions)):
                for j in range(i + 1, len(positions)):
                    coord1, coord2 = positions[i], positions[j]

                    dx, dy = coord2[0] - coord1[0], coord2[1] - coord1[1]

                    antinode1 = (coord1[0] - dx, coord1[1] - dy)
                    antinode2 = (coord2[0] + dx, coord2[1] + dy)

                    for antinode in [antinode1, antinode2]:
                        if (
                            0 <= antinode[0] < len(lines)
                            and 0 <= antinode[1] < len(lines[0])
                            and antinode not in positions
                        ):
                            d1 = distance(coord1, antinode)
                            d2 = distance(coord2, antinode)

                            if d1 == 4 * d2 or d2 == 4 * d1:
                                antinodes.add(antinode)

        print(len(antinodes))


def is_inline(p1, p2, p3):
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) == (p3[0] - p1[0]) * (p2[1] - p1[1])


def p2():
    with open(input_file) as f:
        lines = f.read().splitlines()
        points = {}
        antinodes = set()

        for row in range(len(lines)):
            for col in range(len(lines[row])):
                if lines[row][col].isalnum():
                    if lines[row][col] not in points:
                        points[lines[row][col]] = []
                    points[lines[row][col]].append((row, col))

        rows, cols = len(lines), len(lines[0])
        for row in range(rows):
            for col in range(cols):
                current = (row, col)
                for node in points:
                    antennas = points[node]
                    for i in range(len(antennas)):
                        for j in range(i + 1, len(antennas)):
                            if is_inline(antennas[i], antennas[j], current):
                                antinodes.add(current)

        print(len(antinodes))


input_file = "input.txt"
p1()
p2()
