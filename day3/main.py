import re


# part 1
def p1():
    with open("input.txt") as f:
        lines = f.read()
        out = 0
        # find all occurences of mul(
        idx = [i for i in range(len(lines)) if lines.startswith("mul(", i)]
        for i in idx:
            # find the closing bracket
            j = lines.index(")", i)
            # substr
            curr = lines[i : j + 1]
            curr = curr[4:-1].split(",")
            if len(curr) != 2:
                continue
            else:
                try:
                    a = int(curr[0])
                    b = int(curr[1])
                    out += a * b
                except:
                    continue
        print(out)


# part 2
def p2():
    with open("input.txt") as f:
        lines = f.read()
        out = 0
        # find all occurences of mul(
        idx = [i for i in range(len(lines)) if lines.startswith("mul(", i)]
        dos = [i for i in range(len(lines)) if lines.startswith("do()", i)]
        donts = [i for i in range(len(lines)) if lines.startswith("don't()", i)]
        fuckthis = []
        for i in idx:
            fuckthis.append((i, "mul"))
        for i in dos:
            fuckthis.append((i, "do"))
        for i in donts:
            fuckthis.append((i, "dont"))
        fuckthis.sort()

        toggle = True
        for thing in fuckthis:
            if thing[1] == "mul":
                if toggle:
                    substr = lines[thing[0] + 4 : lines.index(")", thing[0])]
                    substr = substr.split(",")
                    if len(substr) != 2:
                        continue
                    else:
                        try:
                            a = int(substr[0])
                            b = int(substr[1])
                            out += a * b
                        except:
                            continue
            elif thing[1] == "do":
                toggle = True
            else:
                toggle = False
        print(out)


def p2_regex():
    with open("input.txt") as f:
        lines = f.readlines()
        total = 0
        state = 1
        for line in lines:
            # list = re.findall(r'mul\((\d+),(\d+)\)|', line)
            list = re.findall(r"mul\((\d+),(\d+)\)|(do\(\))|(don\'t\(\))", line)
            # find order of do's and don'ts
            for item in list:
                if state == 1 and item[0] and item[1]:
                    total += int(item[0]) * int(item[1])
                if item[3] == "don't()":
                    state = 0
                if item[2] == "do()":
                    state = 1

        print(total)


p1()
p2()
p2_regex()
