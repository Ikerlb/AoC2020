with open("input.txt") as f:
    lines = f.read().splitlines()
    start = [int(n) for n in lines.pop().split(",")] 

def play(l, k):
    d = {n:i for i, n in enumerate(l, 1)}
    p = l[-1]
    for i in range(len(l), k):
        if p in d:
            np = i - d[p]
        else:
            np = 0
        d[p], p = i, np
    return p

def part1(l = start):
    return play(l, 2020)

def part2(l = start):
    return play(l, 30000000)
