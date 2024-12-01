# part 1
left = []
right = []
with open("input.txt") as f:
    
    lines = f.readlines()
    for line in lines:
        nums = line.split()
        left.append(int(nums[0]))
        right.append(int(nums[1]))
    left.sort()
    right.sort()

    out = 0
    for x, y in zip(left, right):
        out += abs(x - y)
    print(out)

# part 2
l = []
rfreq = {}
with open("input.txt") as f:
    lines = f.readlines()
    for line in lines:
        nums = line.split()
        nums[0] = int(nums[0])
        nums[1] = int(nums[1])
        l.append(nums[0])
        rfreq[nums[1]] = rfreq.get(nums[1], 0) + 1
    out = 0
    for v in l:
        out += v * rfreq.get(v, 0)
    print(out)


