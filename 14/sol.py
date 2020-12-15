from re import match

with open("input.txt") as f:
    lines = f.read().splitlines()
    instructions = [l.split(" = ") for l in lines]

def enable(n, i):
    return n | (1 << i)

def disable(n, i):
    b = n << i
    return n & ~(1 << i)

def get(n, i):
    return n & (1 << i) != 0

def apply(n, mask):
    for i, c in enumerate(reversed(mask)):
        if c == "0":
            n = disable(n, i)
        elif c == "1":
            n = enable(n, i)
    return n

def part1(l = instructions):
    d = {}
    for s1, s2 in l:
        if s1 == "mask":
            mask = s2
        else:
            n = int(match('mem\[(\d+)\]',s1).groups()[0])
            d[n] = apply(int(s2), mask)
    return sum(d.values())


def inmap(f, l): 
    for i, v in enumerate(l):
        l[i] = f(v) 

#needs masking to remove trailing one!
def addresses(n, mask):
    res = [1]
    for i,c in enumerate(mask):
        if c == '0':
            inmap(lambda a: (a << 1) | (get(n, 35 - i)), res)
        elif c == '1':
            inmap(lambda a: (a << 1) | 1, res)
        else:
            inmap(lambda a: (a << 1), res)
            for i in range(len(res)):
                res.append(res[i] | 1)
    return res

def part2(l = instructions):
    d = {}
    for s1, s2 in l:
        if s1 == "mask":
            mask = s2
        else:
            n = int(match('mem\[(\d+)\]',s1).groups()[0])
            for a in addresses(n, mask):
                d[a & 0xfffffffff] = int(s2)
    return sum(d.values())
