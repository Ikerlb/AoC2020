from fileinput import input as finput
from collections import deque
from itertools import islice

def parse(deck):
    q = deque()
    for line in deck.splitlines():
        try:
            i = int(line)
            q.append(int(line))
        except:
            k = line[:-1]    
    return k, q

fi = "".join(finput())
decks = dict([parse(deck) for deck in fi.split("\n\n")])

def combat(decks):
    p1 = decks["Player 1"]
    p2 = decks["Player 2"]
    while p1 and p2:
        p1c = p1.popleft()    
        p2c = p2.popleft()
        if p1c > p2c:
            p1.append(p1c)    
            p1.append(p2c)
        else:
            p2.append(p2c)
            p2.append(p1c)
    return ("Player 1", p1) if p1 else ("Player 2", p2)

def score(deck):
    s = 0
    for i, n in enumerate(reversed(deck), 1):
        s += n * i
    return s

def part1(decks):
    _, deck = combat(decks)
    return score(deck)

def tuplify(p1, p2):
    return tuple(p1) + ("_",) + tuple(p2)

def qslice(q, start, end):
    return deque(islice(q, start, end))

def recursive_combat(p1, p2):
    used = set()
    while p1 and p2:
        t = tuplify(p1, p2)
        if t in used:
            return 1, p1
        used.add(t)
        p1c = p1.popleft()
        p2c = p2.popleft()
        if len(p1) >= p1c and len(p2) >= p2c:
            p1s = qslice(p1, 0, p1c)
            p2s = qslice(p2, 0, p2c)
            winner, _ = recursive_combat(p1s, p2s)
        else:
            winner = 1 if p1c > p2c else 2 
        if winner == 1: 
            p1.append(p1c)
            p1.append(p2c)
        else:
            p2.append(p2c)
            p2.append(p1c)
    if len(p1) > 0:
        return 1, p1
    return 2, p2
    
def part2(decks):
    p1 = decks["Player 1"]
    p2 = decks["Player 2"]
    _, deck = recursive_combat(p1, p2)
    return score(deck)



