with open("input.txt") as f:
    trees = f.read().splitlines()

def count_trees(matrix, drow, dcol):
    n, m = len(matrix), len(matrix[0])
    col = res = 0
    for row in range(0, n, drow):
        res += int(matrix[row][col] == '#')
        col = (col + dcol) % m
    return res

def part1(matrix = trees):
    return count_trees(matrix, 1, 3)

def part2(matrix = trees):
    l = [(1,1),(1,3), (1,5),(1,7),(2,1)]
    res = 1
    for drow, dcol in l:
        res *= count_trees(matrix, drow, dcol)
    return res
