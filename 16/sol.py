from itertools import chain
from math import prod

def parse_rules(rules):
    d = {}
    for rule in rules.splitlines():
        k, rest = rule.split(": ")
        opt = rest.split(" or ")
        d[k] = [tuple(map(int, o.split("-"))) for o in opt]
    return d

def parse_ticket(ticket):
    return [int(i) for i in ticket.split(",")]

with open("input.txt") as f:
    rules, ticket, nearby = f.read().split("\n\n")
    rules = parse_rules(rules)     
    ticket = parse_ticket(ticket.splitlines()[-1])
    nearby = [parse_ticket(t) for t in nearby.splitlines()[1:]]

def valid_num(x, rule):
    return any(s <= x <= e for s, e in rule)

def valid_fields(x, rules):
    fields = []    
    for k, r in rules.items():
        if valid_num(x, r):
            fields.append(k)
    return fields

def valid(ticket, rules):
    return all(valid_fields(n, rules) for n in ticket)

# initially 'optimized' a bit
# by merging all rules intervals 
# into a sorted disjoint list of intervals
# but meh, this is simpler for both parts
def part1(rs = rules, nt = nearby):    
    return sum(n for n in chain(*nt) if not len(valid_fields(n, rs)))

def fields_by_columns(valid, rules):
    fxc = []    
    for i in range(len(rules)):
        fields = set(rules.keys())
        for t in valid:
            fields &= set(valid_fields(t[i], rules))
        fxc.append(fields)
    return fxc


# i think sudoku like elimination
def part2(rs = rules, t = ticket, nt = nearby):
    vt = [tt for tt in nt if valid(tt, rs)]
    fxc = fields_by_columns(vt, rs)
    res, cur = [0] * len(rules), set()
    for i, fs in sorted(enumerate(fxc), key = lambda x:x[1]):
        res[i] = (fs - cur).pop()              
        cur |= fs
    return prod(t[i] for i,f in enumerate(res) if f.startswith("departure"))
      
