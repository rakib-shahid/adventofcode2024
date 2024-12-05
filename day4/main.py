# part 1
def p1():
    with open("input.txt") as f:
        lines = f.read().splitlines()
        grid = [list(line) for line in lines]

        rows, cols = len(grid), len(grid[0])
        target = "XMAS"
        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1),
            (-1, -1),
            (-1, 1),
            (1, -1),
            (1, 1),
        ]

        def is_valid(x, y):
            return 0 <= x < rows and 0 <= y < cols

        def dfs(x, y, index, direction):
            if index == len(target):
                return True
            if not is_valid(x, y) or grid[x][y] != target[index]:
                return False

            dx, dy = direction
            return dfs(x + dx, y + dy, index + 1, direction)

        out = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == target[0]:
                    for dx, dy in directions:
                        if dfs(i, j, 0, (dx, dy)):
                            out += 1

        print(out)


# part 2
def p2():
    with open("input.txt") as f:
        lines = f.read().splitlines()

        grid = [list(line) for line in lines]
        rows, cols = len(grid), len(grid[0])

        def checkX(x, y):
            if x - 1 < 0 or x + 1 >= rows or y - 1 < 0 or y + 1 >= cols:
                return False
            else:
                if (
                    grid[x - 1][y - 1] == "M"
                    and grid[x - 1][y + 1] == "M"
                    and grid[x + 1][y - 1] == "S"
                    and grid[x + 1][y + 1] == "S"
                ):
                    return True

                if (
                    grid[x - 1][y - 1] == "M"
                    and grid[x + 1][y - 1] == "M"
                    and grid[x - 1][y + 1] == "S"
                    and grid[x + 1][y + 1] == "S"
                ):
                    return True

                if (
                    grid[x + 1][y - 1] == "M"
                    and grid[x + 1][y + 1] == "M"
                    and grid[x - 1][y - 1] == "S"
                    and grid[x - 1][y + 1] == "S"
                ):
                    return True

                if (
                    grid[x + 1][y + 1] == "M"
                    and grid[x - 1][y + 1] == "M"
                    and grid[x - 1][y - 1] == "S"
                    and grid[x + 1][y - 1] == "S"
                ):
                    return True

            return False

        out = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "A":
                    if checkX(i, j):
                        out += 1
        print(out)


p1()
p2()
