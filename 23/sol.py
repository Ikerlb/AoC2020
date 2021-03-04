from fileinput import input as finput

class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

    def format(self, separator = "", highlight = False):
        n = self
        s = [f"({n.val})" if highlight else f"{n.val}"]
        used = {n.val} 
        while n.next and n.next.val not in used:
            used.add(n.next.val)
            s.append(f"{n.next.val}")
            n = n.next
        return separator.join(s)

    def __repr__(self):
        return self.format(" ", True)

def linkify(order):
    head = n = Node("dummy")
    m = {}
    for d in order:
        n.next = Node(int(d))
        m[n.next.val] = n.next
        n = n.next
    # dummy head, tail and nodes!
    return head, n, m 

def parse_part1(order):
    head, n, m = linkify(order)
    n.next = head.next 
    return head.next, m

def parse_part2(order, upto):
    head, n, m = linkify(order)
    for i in range(max(m.keys()) + 1, upto + 1):
        n.next = Node(i)
        m[n.next.val] = n.next
        n = n.next
    n.next = head.next
    return head.next, m

lines = "".join(finput())
labeling = "".join(lines.splitlines())

def remove_k_nodes(node, k):
    head = node    
    nodes = set()
    for _ in range(k):
        node = node.next
        nodes.add(node.val)
    detached = head.next 
    head.next, node.next = node.next, None
    return detached, nodes

def append_after(node, l):
    last = l
    while last.next:
        last = last.next
    last.next, node.next = node.next, l

def wrapped_decrement(n, around):
    if n == 1:
        return around        
    return n - 1

def choose_target(n, picked, around):
    target = wrapped_decrement(n, around)       
    while target in picked:
        target = wrapped_decrement(target, around)
    return target

def play(current, nodes, rounds, largest = 9):
    for i in range(rounds):                            
        pick, pnodes = remove_k_nodes(current, 3)    
        target = choose_target(current.val, pnodes, largest)
        append_after(nodes[target], pick)
        current = current.next
    return current

def part1(labeling):
    current, nodes = parse_part1(labeling)
    play(current, nodes, 100, 9)    
    return f"{nodes[1].format('', False)}"[1:] 

def part2(labeling):
    current, nodes = parse_part2(labeling, 1000000)
    play(current, nodes, 10000000, 1000000)
    fst = nodes[1].next.val
    snd = nodes[1].next.next.val
    return fst, snd
