from operator import add, mul

with open("input.txt") as f:
    exprs = f.read().splitlines()

def tokenize(s):
    n = None
    for c in s:
        if c.isdigit() and n is not None:
            n = n * 10 + int(c)
        elif c.isdigit():
            n = int(c)
        elif c in "*+":
            yield c
        elif c == "(":
            yield c
        elif c == ")" and n is not None:
            yield n
            n = None
            yield c
        elif c == ")":
            yield c
        elif c == " " and n is not None:
            yield n
            n = None
    if n is not None:
        yield n

# consume values s[-1] 'o[-1]' s[-2]'
def consume(s, o):
    d = {'+':add, '*':mul}
    op = o.pop()
    r = s.pop()
    l = s.pop()
    r = d[op](l, r)
    s.append(r) 

# shunting yard algorithm
def evaluate(expr, prec = {'+':0, '*':1}):
    s, o = [], []
    for t in tokenize(expr):
        if type(t) == int: 
            s.append(t)
        elif t == "(":
            o.append(t)
        elif t == ")":
            while o and o[-1] != "(":
                consume(s, o)
            o.pop() # remove (
        else:
            while o and o[-1] not in "()" and prec[o[-1]] >= prec[t]:
                consume(s, o)
            o.append(t)
    while o and o[-1]: 
        consume(s, o)
    return s.pop()

def part1(l = exprs):
    prec = {'+':0, '*':0}
    return sum(map(lambda x: evaluate(x, prec), l))

def part2(l = exprs):
    prec = {'+':1, '*':0}
    return sum(map(lambda x: evaluate(x, prec), l))
