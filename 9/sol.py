from collections import Counter

with open("input.txt") as f:
    lines = f.read().splitlines()
    nums = [int(x) for x in lines]

def find_pair(c, n):
    for nn in c:
        if n - nn in c and n - nn != n:
            return True
    return False

def part1(cap, l = nums):
    c = Counter(l[:cap])
    for i in range(cap, len(nums)):
        n, last = l[i], l[i - cap]
        if not find_pair(c, n):
            return n        
        if c[last] == 1:
            del c[last]
        else:
            c[last] -= 1
        c[n] += 1
    return None

#stinks of sliding window
#but i've not proven its correctness
def part2(cap, l = nums):
    n = part1(cap, l)
    s = start = 0
    for end in range(len(l)):
        s += l[end]
        while s > n:
            s -= l[start]
            start += 1
        if s == n:
            sub = l[start:end + 1]
            return max(sub) + min(sub)
    return None
