from collections import Counter

def parse(lines):
    c = Counter()
    size = 0
    for l in lines:
        if l == "":
            yield c, size
            c, size = Counter(), 0
            continue
        c.update(l)
        size += 1
    yield c, size

with open("input.txt") as f:
    lines = f.read()
    groups = list(parse(lines.splitlines()))
    
def part1(l = groups):
    res = 0
    for gc, _ in l:
        res += len(gc)
    return res


def part2(l = groups):
    res = 0
    for gc, gs in l:
        res += len([o for o in gc if gc[o] == gs])
    return res

