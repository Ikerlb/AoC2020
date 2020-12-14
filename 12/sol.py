from math import cos, sin, radians

def parse(line):
    return (line[0], int(line[1:]))

with open("input.txt") as f:
    lines = f.read().splitlines()    
    instructions = [parse(line) for line in lines]

def rotate(px, py, rad):
    ca = cos(rad)
    sa = sin(rad)
    return ca * px - sa * py, sa * px + ca * py

def part1(l = instructions):
    dx, dy = 1, 0
    px = py = 0
    for ins, n in l:
        if ins == "E":
            px += n
        elif ins == "W":
            px -= n
        elif ins == "N":
            py += n
        elif ins == "S":
            py -= n
        elif ins == "L":
            dx, dy = rotate(dx, dy, radians(n))
        elif ins == "R":
            dx, dy = rotate(dx, dy, -radians(n))
        else:
            px += n * dx 
            py += n * dy
    return abs(px) + abs(py)

def part2(l = instructions):
    dx, dy = 10, 1
    px = py = 0
    for ins, n in l:
        if ins == "N":
            dy += n
        elif ins == "S":
            dy -= n
        elif ins == "E":
            dx += n
        elif ins == "W":
            dx -= n
        elif ins == "L":
            dx, dy = rotate(dx, dy, radians(n))
        elif ins == "R":
            dx, dy = rotate(dx, dy, -radians(n))
        else:
            px += n * dx
            py += n * dy
    return abs(px) + abs(py)
