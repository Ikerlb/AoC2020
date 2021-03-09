from fileinput import input

lines = "".join(input()).splitlines()
card_pub, door_pub = map(int, lines)

def step(value, subject = 7):
    return (value * subject) % 20201227

def loop_size(public):
    v, i = 1, 0
    while v != public:
        i += 1
        v = step(v)
    return i

def encryption_key(public, other_loop_size):
    v = 1
    for _ in range(other_loop_size):
        v = step(v, public)
    return v

def part1(card_pub, door_pub):
    card_lz = loop_size(card_pub)
    door_lz = loop_size(door_pub)
    return encryption_key(card_pub, door_lz)
