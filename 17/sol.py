from itertools import product
from collections import defaultdict
import operator

def parse(txt, dim):
    g = set()
    ext = dim - 2
    lines = txt.splitlines()
    for y in range(len(lines)):
        for x, v in enumerate(lines[y]): 
            if v == "#":
                g.add((x, y) + (0,) * ext)
    return g

with open("input.txt") as f:
    txt = f.read()

def sum(p1, p2):
    return tuple(map(operator.add, p1, p2))        

def neighbors(p):
    m = [(0, -1, 1) for i in range(len(p))]
    gen = product(*m)
    next(gen) #drop (0, 0, ..., 0)
    for np in gen:
        yield sum(p, np)

def step(grid):
    counts, ngrid = defaultdict(int), set()
    for p in grid:
        for np in neighbors(p):
            counts[np] += 1  
    for p, v in counts.items():
        if p in grid and v in [2, 3]:
            ngrid.add(p)  
        elif v == 3:
            ngrid.add(p)
    return ngrid
            
def part1(t = txt):
    g = parse(t, 3)
    for _ in range(6):
        g = step(g)
    return len(g)

def part2(t = txt):
    g = parse(t, 4)
    for _ in range(6):
        g = step(g)
    return len(g)

