import fileinput
import sys
from collections import defaultdict
from itertools import chain, product

def parse(tile):
    i, tile = tile.split(":\n")
    t = [list(r) for r in tile.splitlines()]
    return int(i.replace("Tile ", "")), t


pattern = """                  # 
#    ##    ##    ###
 #  #  #  #  #  #   """.splitlines()

file_name = sys.argv[1] if len(sys.argv) >= 2 else "input.txt"
with open(file_name) as f:
    tiles = dict([parse(t) for t in f.read().split("\n\n")])

def rotate(m):
    nm = [r[:] for r in m]
    n = len(nm)
    for l in range(n // 2):
        s, e = l, n - l - 1
        for i in range(e - s):
            nm[s][s + i], aux = nm[e - i][s], nm[s][s + i]
            nm[s + i][e], aux = aux, nm[s + i][e]
            nm[e][e - i], aux = aux, nm[e][e - i]
            nm[e - i][s] = aux
    return nm

def rotations(tile):
    for _ in range(4):
        yield tile
        yield [r for r in reversed(tile)]
        tile = rotate(tile)

def hash_list(l):
    return sum(1 << i for i,v in enumerate(l) if v == "#")

def hash_tile(tile):
    up = hash_list(tile[0])
    down = hash_list(tile[-1])
    left = hash_list([tile[i][0] for i in range(len(tile))])
    right = hash_list([tile[i][-1] for i in range(len(tile))])
    return (up, right, down, left)

def adjacent_to(tile, hashes):
    sh = set(chain(*hashes[tile]))
    for other,v in hashes.items():
        if tile == other:
            continue
        if set(chain(*v)) & sh:
            yield other    

# hash all rotations of 
# all tiles and group them
# by id
def hashes(tiles):
    h = defaultdict(dict)
    for k,t in tiles.items():
        for r in rotations(t):
            h[k][hash_tile(r)] = r
    return h

def adjacencies(tiles, hashes):
    adj = defaultdict(list) 
    for k in tiles:
        adj[k] = list(adjacent_to(k, hashes))
    return adj

def rights(t, h, adj, hashes):
    _, r, _, _ = h
    return [(a, h) for a in adj[t] for h in hashes[a] if h[-1] == r]

def downs(t, h, adj, hashes):
    _, _, d, _ = h
    return [(a, h) for a in adj[t] for h in hashes[a] if h[0] == d]

# get correct start configuration
def start_tile_rotation(t, adj, hashes):
    for h in hashes[t]:
        rs = rights(t, h, adj, hashes)
        ds = downs(t, h, adj, hashes)
        if rs and ds:
            return (t, h)

# heavily relies on there being
# no equal (straight or backwards)
# 'hashes' between tiles
def reconstruct(tiles, h):
    adj = adjacencies(tiles, h)
    # get *any* corner and make
    # it the top left
    tl = [k for k, v in adj.items() if len(v) == 2][0]
    tl, p = start_tile_rotation(tl, adj, h)
    n = int(len(tiles) ** 0.5)
    grid = {(0,0): (tl, p)}
    for r in range(1, n):
        tl, p = grid[r - 1, 0]
        ds = downs(tl, p, adj, h)
        grid[r, 0] = ds.pop()
    for r in range(0, n):
        for c in range(1, n):
            tl, p = grid[r, c - 1]
            rs = rights(tl, p, adj, h)
            grid[r, c] = rs.pop()
    return grid

def merge_grid_row(gr):
    s = []
    for r in range(1, len(gr[0]) - 1):
        row = []
        for gc in gr:
            row.extend(gc[r][1:-1])
        s.append(row)
    return s

def merge(g, h):
    n = int(len(g) ** 0.5)
    m = []
    for c in range(n):
        l = [h[i][t] for i,t in [g[c, r] for r in range(n)]]        
        m.extend(merge_grid_row(l))
    return m

def fmt(tile):
    s = []
    for r in tile:
        s.append("".join(r))
    return "\n".join(s)

def part1(t = tiles):
    n = int(len(t) ** 0.5)
    h = hashes(t)
    g = reconstruct(t, h)
    tl, _ = g[0, 0]
    tr, _ = g[0, n - 1]
    bl, _ = g[n - 1, 0]
    br, _ = g[n - 1, n - 1]
    return tl * tr * bl * br

def pattern_to_offsets(m):
    for r in range(len(m)):
        for c in range(len(m[0])):
            if m[r][c] == "#":
                yield r, c

def replace(m, coords, targ):
    for r, c in coords:
        m[r][c] = targ

def count_patterns(m, p, off):
    rows, cols = len(m), len(m[0])
    for r in range(rows - len(p)):
        for c in range(cols - len(p[0])):
            if all(m[r+dr][c+dc] == "#" for dr,dc in off):
                replace(m, [(r+dr,c+dc) for dr,dc in off], "O")
    return sum(map(lambda r: r.count("#"), m))

def part2(t = tiles, p = pattern):
    h = hashes(t)
    g = reconstruct(t, h)
    m = merge(g, h)    
    off = [o for o in pattern_to_offsets(p)]
    return min(count_patterns(r, p, off) for r in rotations(m))

