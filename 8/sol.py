with open("input.txt") as f:
    lines = f.read().splitlines()
    parse = lambda x: (x[0], int(x[1]))
    instructions = [parse(l.split(" ", 1)) for l in lines] 

def exec(l):
    a = pc = 0
    s = set()
    while pc < len(l) and pc not in s:
        ins, arg = l[pc]
        s.add(pc)
        if ins == "jmp":
            pc += arg
            continue
        elif ins == "acc":
            a += arg
        pc += 1
    return (a, "HALT" if pc >= len(l) else "LOOP")

def part1(l = instructions):
    return exec(l)[0]

def part2(l = instructions):
    d = {"jmp":"nop", "nop":"jmp"}
    for i in range(len(l)):
        ins, arg = l[i]
        if ins == "acc":
            continue
        l[i] = d[ins], arg 
        res, status = exec(l)
        l[i] = ins, arg
        if status == "HALT":
            return res 
    return None
    
    
