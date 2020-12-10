def parse(s):
    return (s[:7], s[7:])

def bisect(s):
    l, r = 0, 2**len(s) - 1
    for c in s:
        mid = (l + r) // 2
        if c in ['B', 'R']:
            l = mid + 1
        else:
            r = mid
    return r

with open("input.txt") as f:
    lines = f.read().splitlines()
    f = lambda bp: bisect(bp[0]) * 8 + bisect(bp[1])
    ids = [f(parse(l)) for l in lines]

def part1(l = ids):
    return max(l)

def part2(l = ids):
    s = sorted(l)
    # can be done in O(n), but meh
    for i in range(len(s) - 1): 
        if s[i] + 1 != s[i + 1]:
            return s[i] + 1
    
