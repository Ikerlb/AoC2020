from functools import reduce

with open("input.txt") as f:
    ss, rest = f.read().splitlines()
    start = int(ss)
    buses = [int(b) if b != "x" else None for b in rest.split(",")]

def part1(s = start, l = buses):
    m, i = min([(b - (s % b), b) for b in l if b])
    return m * i 

# https://www.youtube.com/watch?v=zIFehsBHB8o&ab_channel=MathswithJay
def solve(equations):
    _, mods = zip(*equations)
    p, s = reduce(lambda x,y: x * y, mods), 0    
    for r, m in equations:
        pi = p // m
        _, inv, _ = inverse(pi, m)
        s += r * pi * inv
    return s % p

# mult inverse a: a*x = 1 mod m
# a and m must (and are in this case)
# coprimes
# https://cp-algorithms.com/algebra/extended-euclid-algorithm.html
def inverse(a, m):
    if m == 0:
        return a, 1, 0
    d, x1, y1 = inverse(m, a % m)
    return d, y1, x1 - y1 * (a // m)

# ki are all primes afaik
# particularly coprime with e/o so:
# t = 0 % k0
# t = -1 % k1
# t = -2 % k2
# ...
# solve for t with crt
def part2(l = buses):
    return solve([(-i, n) for i,n in enumerate(l) if n])        
