import re
import fileinput
from collections import defaultdict
from heapq import heappush, heappop, heapify

def parse_food(line):
    r = re.search(r'(.+) \(contains (.+)\)', line)
    ing, aller = r.groups()
    return ing.split(" "), aller.split(", ")

food_list = [parse_food(l) for l in fileinput.input()]

def get_all_allergens(food_list):
    allergens = set()
    for ing, aller in food_list:
        allergens |= aller
    return allergens

def get_all_ingredients(food_list):
    ingredients = set()
    for ing, aller in food_list:
        ingredients |= ing
    return ingredients

def group_allergens(food_list):
    d = defaultdict(list) 
    for ings, aller in food_list:
        for a in aller:
            d[a].append(ings)    
    return d

def union(*sets):
    us = set()
    for s in sets:
        us |= s
    return us

def intersection(*sets):
    i = union(*sets)
    for s in sets:
        i &= s
    return i    

def simplify(guesses):
    simp = {}
    h = [(len(v), v, k) for k, v in guesses.items()]
    heapify(h)
    while h and h[0][0] == 1:
        c, s, a = heappop(h)
        ing = s.pop()
        simp[ing] = a
        for i in range(len(h)):
            c, s, a = h[i]
            h[i] = (c - (ing in s), s - {ing}, a)
        heapify(h)
    return simp


def guesses(grouped):
    g = defaultdict(set)
    for aler, ings in grouped.items():
        g[aler] = intersection(*map(set, ings))
    return g

def part1(food_list):
    grouped = group_allergens(food_list)
    guess_dict = guesses(grouped) 
    simp = simplify(guess_dict)
    s = 0
    for ings, _ in food_list:
        l = [ing for ing in ings if ing not in simp]
        s += sum(1 for ing in ings if ing not in simp)
    return s 

def part2(food_list):
    grouped = group_allergens(food_list)
    guess_dict = guesses(grouped)
    simp = simplify(guess_dict)
    canonical = []
    for i, a in sorted(simp.items(), key = lambda x:x[1]):
        canonical.append(i)                        
    return ",".join(canonical)
