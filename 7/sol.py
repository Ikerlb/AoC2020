def parse(rule):
    left, right = rule.split(" bags contain ")         
    prods = {}
    if right == "no other bags.":
        return (left, prods)
    for prod in right.split(", "):
        n, rest = prod.split(" ", 1)
        bag, _ = rest.rsplit(" ", 1)
        prods[bag] = int(n)
    return (left, prods)

def generate_graph(lines):
    res = {}
    for l in lines:
        k, v = parse(l)
        res[k] = v
    return res

with open("input.txt") as f:
    lines = f.read().splitlines()
    rules = generate_graph(lines)

def count_bags(graph, bag):
    res = 1
    for bb, nn in graph[bag].items():
        res += nn * count_bags(graph, bb)
    return res

def contains(graph, c, target):
    res = False
    for k, _ in graph[c].items():
        res = res or contains(graph, k, target) or k == target 
        if res:
            return True
    return False

def part1(graph = rules):
    return sum(contains(graph, c, "shiny gold") for c in graph)    

def part2(graph = rules):
    return count_bags(graph, "shiny gold") - 1
