# part 1
def p1():
    out = 0
    with open("input.txt") as f:
        lines = f.readlines()
        for line in lines:
            report = [int(x) for x in line.split()]
            if report != sorted(report) and report != sorted(report, reverse=True):
                continue
            else:
                valid = True
                for i in range(len(report) - 1):
                    if not (0 < abs(report[i + 1] - report[i]) <= 3):
                        valid = False
                out += valid

    print(out)


def isvalid(nums):
    report = nums
    if report != sorted(report) and report != sorted(report, reverse=True):
        return False
    else:
        valid = True
        for i in range(len(report) - 1):
            if not (0 < abs(report[i + 1] - report[i]) <= 3):
                valid = False
                break
        return valid


# part 2
def p2():
    out = 0
    with open("input.txt") as f:
        lines = f.readlines()
        for line in lines:
            report = [int(x) for x in line.split()]
            if isvalid(report):
                out += 1
            else:
                for i in range(len(report)):
                    temp = report[:i] + report[i + 1 :]
                    if isvalid(temp):
                        out += 1
                        break
    print(out)


p1()
p2()
