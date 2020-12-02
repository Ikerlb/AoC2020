def parse(s):
    rules, pw = s.split(": ")
    freqs, c = rules.split(" ")
    mn, mx = [int(n) for n in freqs.split("-")]
    return (mn, mx, c, pw)

with open("input.txt") as f:
    lines = f.read().splitlines()
    passwords = [parse(line) for line in lines]

def part1(l = passwords):
    res = 0 
    for mn, mx, c, pw in l:
        res += int(mn <= pw.count(c) <= mx)
    return res

def part2(l = passwords):
    res = 0
    for mn, mx, c, pw in l:
        res += int((pw[mn - 1] == c) ^ (pw[mx - 1] == c))
    return res
