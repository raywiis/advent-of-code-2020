from functools import reduce

f = open('./day-3-problem.txt')
area = f.read().splitlines()


def count_trees(right, down):
    count = 0
    x_pos = right
    for i in range(down, len(area), down):
        if area[i][x_pos] == '#':
            count += 1

        x_pos = (x_pos + right) % len(area[0])

    return count

print(count_trees(3, 1))

# Right 1, down 1.
# Right 3, down 1. (This is the slope you already checked.)
# Right 5, down 1.
# Right 7, down 1.
# Right 1, down 2.

slope_trees = [
    count_trees(1, 1),
    count_trees(3, 1),
    count_trees(5, 1),
    count_trees(7, 1),
    count_trees(1, 2)
]

prod = reduce((lambda x, y: x * y), slope_trees)
print(prod)
