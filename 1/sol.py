with open("input.txt", "r") as f:
    txt = f.read()
    entries = [int(e) for e in txt.split()]

#naive O(n^2) ew
def find_two_entries_naive(l, k):
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            if l[i] + l[j] == k:
                return l[i] * l[j]
    return None

#better O(nlogn) time, O(n) space
#can sort in place though
def find_two_entries_two_pointers(l, k):
    l = sorted(l)
    left, right = 0, len(l) - 1
    while left < right:
        sm = l[left] + l[right]
        if sm == k:
            return l[left] * l[right]
        elif sm > k: #overshoot, reduce right!
            right -= 1
        else:
            left += 1
    return None

#O(n) time and space
def find_two_entries_set(l, k):
    s = {n for n in l}
    for n in l:
        if k - n in s:
            return n * (k - n)
    return None

#ew ew ew ew 
def find_three_entries_naive(l, k):
    n = len(l)
    for i in range(n):
        for j in range(i + 1, n):
            for m in range(j + 1, n):
                if l[i] + l[j] + l[m] == k:
                    return l[i] * l[j] * l[m]
    return None            

#O(n^2) time O(n) space
def find_three_entries_two_pointers(l, k):
    l = sorted(l)
    for i in range(len(l) - 1):
        left, right = i + 1, len(l) - 1
        while left < right:
            sm = l[left] + l[right]
            if sm == k - l[i]:
                return l[left] * l[right] * l[i]
            elif sm > k - l[i]:
                right -= 1
            else:
                left += 1
    return None    

def part1(l = entries):
    return find_two_entries_two_pointers(l, 2020)

def part2(l = entries):
    return find_three_entries_two_pointers(l, 2020)
