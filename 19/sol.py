def parse(line):
    nt, rest = line.split(": ")
    if rest[0] == '"':
        return nt, rest.replace('"', "")
    prod = [o.split(" ") for o in rest.split(" | ")]
    return nt, prod

with open("input.txt") as f:
    rules, tests = f.read().split("\n\n")
    graph = dict(map(parse, rules.splitlines()))
    tests = tests.splitlines()

# verify solution with brute force
def gen(g, n):
    if n not in g:
        return [n]
    res = []
    for p in g[n]:
        tp = [""]
        for nn in p:
            tp = [a + b for a in tp for b in gen(g, nn)]
        res.extend(tp)
    return res

def dfs(g, n, targs):
    if n not in g:
        return [t[1:] for t in targs if t and t[0] == n]
    res = []
    for p in g[n]: # try the same targs!!
        x = targs
        for nn in p: # consume if matches and sequence!!
            x = dfs(g, nn, x)
            if not x:
                break
        else:
            res.extend(x)
    return res

def part1(g = graph, t = tests):
    return dfs(g, '0', tests).count("")

def part2(g = graph, t = tests):
    g['8'] = [['42'], ['42', '8']]
    g['11'] = [['42', '31'], ['42', '11', '31']]
    return dfs(g, '0', tests).count("")

