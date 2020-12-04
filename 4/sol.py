from re import match

def parse(text):
    doc = {}
    for line in text.splitlines():
        if line == "":
            yield doc
            doc = {}
            continue
        for field in line.split(" "):
            k, v = field.split(":")
            doc[k] = v
    yield doc

with open("input.txt") as f:
    txt = f.read()
    documents = list(parse(txt))

def part1(d = documents):
    res = 0
    fields = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]
    for doc in d:
        res += all([f in doc for f in fields])
    return res

def val_byr(s):
    return len(s) == 4 and 1920 <= int(s) <= 2002

def val_iyr(s):
    return len(s) == 4 and 2010 <= int(s) <= 2020

def val_eyr(s):
    return len(s) == 4 and 2020 <= int(s) <= 2030

def val_hgt(s):
    if s[-2:] == "cm":
        return 150 <= int(s[:-2]) <= 193
    elif s[-2:] == "in":
        return 59 <= int(s[:-2]) <= 76
    return False

def val_hcl(s):
    return match(r"#[0-9a-f]{6}$", s)

def val_ecl(s):
    return s in ["amb","blu","brn","gry","grn","hzl","oth"]

def val_pid(s):
    return match(r'[0-9]{9}$', s)

def part2(d = documents):
    res = 0
    fields = {
            "byr": val_byr,
            "iyr": val_iyr,
            "eyr": val_eyr,
            "hgt": val_hgt,
            "hcl": val_hcl,
            "ecl": val_ecl,
            "pid": val_pid
            }
    for doc in d:
        res += all([f in doc and fields[f](doc[f]) for f in fields])
    return res

    
