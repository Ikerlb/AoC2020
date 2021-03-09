from collections import defaultdict
from fileinput import input

def parse(line):
    dirs, i = [], 0
    while i < len(line):
        if line[i] in 'we':
            dirs.append(line[i])
            i += 1
        else:
            dirs.append(line[i] + line[i + 1])
            i += 2
    return dirs

lines = "".join(input()).splitlines()
tiles = [parse(l) for l in lines]

def walk(dirs):
    r = c = 0
    for d in dirs:
        if d == "e":
            c += 1
        elif d == "w":
            c -= 1
        elif d == "ne":
            r += 1
        elif d == "nw":
            r += 1
            c -= 1
        elif d == "se":
            r -= 1
            c += 1
        else:
            r -= 1
    return r, c

def neighbors(r, c):
    yield r + 1, c - 1    
    yield r + 1, c 
    yield r, c - 1
    yield r - 1, c
    yield r - 1, c + 1
    yield r, c + 1

def step(state):
    counter = defaultdict(int)
    for r, c in state:
        for nr, nc in neighbors(r, c):
            counter[nr, nc] += 1             
    nstate = set()
    for tile in state:
        # 0 or > 2 black
        # neighbors flip!
        # which means, 
        # do not add to state
        if counter[tile] in [1, 2]:
            nstate.add(tile)
    for tile, count in counter.items():
        if tile in state:
            continue # we've already handled it
        elif count == 2:
            nstate.add(tile)
    return nstate

def init_state(tiles):
    s = set()
    for t in tiles:
        res = walk(t)
        if res in s:
            s.remove(res)
        else:
            s.add(res)
    return s

def part1(tiles):
    s = init_state(tiles)
    return len(s)

def part2(tiles, days = 100):
    s = init_state(tiles)
    for _ in range(days):
        s = step(s)
    return len(s)
