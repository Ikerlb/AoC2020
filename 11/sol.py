from itertools import product

with open("input.txt") as f:
    txt = f.read()
    grid = [list(line) for line in txt.splitlines()]

def adjacent(m, r, c):
    nns = [-1, 0, 1]
    rs, cs = len(m), len(m[0]) 
    for dr, dc in product(nns, nns):
        if dr == dc == 0:
            continue
        if 0 <= r+dr < rs and 0 <= c+dc < cs:
            yield m[r+dr][c+dc]

def visible_dir(m, r, c, dr, dc):
    rws, cls = len(m), len(m[0])
    cr, cc = r + dr, c + dc
    while 0 <= cr < rws and 0 <= cc < cls and m[cr][cc] == '.':
        cr += dr
        cc += dc
    if 0 <= cr < rws and 0 <= cc < cls and m[cr][cc] != '.':
        return m[cr][cc]
    return None

def visible(m, r, c):
    nns = [-1, 0, 1]        
    for dr, dc in product(nns, nns):
        if dr == dc == 0:
            continue
        if v := visible_dir(m, r, c, dr, dc):
            yield v

def step(m, tolerance, neighbors):
    changes = {}
    rs, cs = len(m), len(m[0])
    for r, c in product(range(rs), range(cs)):
        if m[r][c] == '.':
            continue
        occ = list(neighbors(m, r, c)).count("#")
        if m[r][c] == "L" and occ == 0:
            changes[r, c] = "#"
        elif m[r][c] == "#" and occ  >= tolerance:
            changes[r, c] = "L"
    for r, c in changes:
        m[r][c] = changes[r, c]
    return len(changes)

def part1(m = grid):
    m = m[:] #don't change passed matrix
    while step(m, 4, adjacent):
        pass
    return sum(map(lambda l: l.count("#"), m))
    
def part2(m = grid):
    m = m[:]
    n = step(m, 5, visible)
    while step(m, 5, visible) > 0:
        pass
    return sum(map(lambda l: l.count("#"), m))
