from functools import lru_cache

with open("input.txt") as f:
    lines = f.read().splitlines()
    adapters = sorted([int(x) for x in lines])

def part1(l = adapters):
    s = [0, 0, 0]
    s[l[0] - 1] += 1
    for i in range(1, len(l)):
        d = l[i] - l[i - 1]
        s[d - 1] += 1
    return s[0] * (s[2] + 1)

@lru_cache
def dp(n):
    if n <= 2:
        return 1
    elif n == 3:
        return 2
    return dp(n - 1) + dp(n - 2) + dp(n - 3)

def part2(l = adapters):
    n = len(l)
    res = 1
    cons = 1 if l[0] > 3 else 2
    for i in range(n - 1):
        if l[i + 1] == l[i] + 1:
            cons += 1
        else:
            res *= dp(cons)
            cons = 1
    return res * dp(cons)
