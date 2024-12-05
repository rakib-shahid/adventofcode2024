# part 1
from functools import cmp_to_key


def p1():
    with open("input.txt") as f:
        lines = f.read().splitlines()
        section1 = [line for line in lines if "|" in line]
        section2 = [line for line in lines if "|" not in line][1:]
        pmap = {}
        for line in section1:
            key, value = [int(num) for num in line.split("|")]
            if key not in pmap:
                pmap[key] = []
            pmap[key].append(value)

        out = 0
        for line in section2:
            nums = [int(num) for num in line.split(",")]
            valid = True
            for i in range(len(nums)):
                num = nums[i]
                if num in pmap:
                    # get subarray to the left of num
                    subarray_set = set(nums[:i])
                    map_set = set(pmap[num])
                    if len(map_set.intersection(subarray_set)) > 0:
                        valid = False
            if valid:
                # add middle element to out
                out += nums[len(nums) // 2]

        print(out)
        return out


# part 2
def p2():
    with open("input.txt") as f:
        lines = f.read().splitlines()

        section1 = [line for line in lines if "|" in line]
        section2 = [line for line in lines if "|" not in line][1:]

        pmap = {}
        for line in section1:
            key, value = [int(num) for num in line.split("|")]
            if value not in pmap:
                pmap[value] = set()
            pmap[value].add(key)

        def compare(x, y):
            if x in pmap[y]:
                return -1
            if y in pmap[x]:
                return 1
            return 0

        out = 0
        for line in section2:
            nums = [int(num) for num in line.split(",")]

            sorted_nums = sorted(nums, key=cmp_to_key(compare))

            valid = True
            for i, num in enumerate(nums):
                if num in pmap:
                    before = set(nums[:i])
                    if any(x in before for x in pmap[num]):
                        valid = False
                        break
            if not valid:
                out += sorted_nums[len(sorted_nums) // 2]

        return out


p1_res = p1()
p2_res = p2()
print(p2_res - p1_res)
