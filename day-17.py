from itertools import product
from collections import defaultdict

f = open('./day-17-problem.txt')
start = [list(line) for line in f.read().splitlines()]


def count_activated_around(a, pos, directions):
    x, y, z = pos

    return sum([
        1 for d in directions
        if a[(x + d[0], y + d[1], z + d[2])] == '#'
    ])


def show(a, dx, dy, dz):
    for z in range(-dz, dz + 1):
        print('\n\n', z)
        for y in range(-dy, dy + 1):
            line = []
            for x in range(-dx, dx + 1):
                pos = (x, y, z)
                line += [a[pos]]
            print(''.join(line))


def iterate(start, to, dx, dy, dz, directions):
    for z in range(-dz, dz + 1):
        for y in range(-dy, dy + 1):
            for x in range(-dx, dx + 1):
                pos = (x, y, z)
                activated = count_activated_around(start, pos, directions)

                if activated == 3:
                    to[pos] = '#'
                elif activated == 2 and start[pos] == '#':
                    to[pos] = '#'
                else:
                    to[pos] = '.'


def count_activated_around_4(a, pos, directions):
    x, y, z, w = pos

    return sum([
        1 for d in directions
        if a[(x + d[0], y + d[1], z + d[2], w + d[3])] == '#'
    ])


def iterate_4(start, to, dx, dy, dz, dw, directions):
    for w in range(-dw, dw + 1):
        for z in range(-dz, dz + 1):
            for y in range(-dy, dy + 1):
                for x in range(-dx, dx + 1):
                    pos = (x, y, z, w)
                    activated = count_activated_around_4(start, pos, directions)

                    if activated == 3:
                        to[pos] = '#'
                    elif activated == 2 and start[pos] == '#':
                        to[pos] = '#'
                    else:
                        to[pos] = '.'


def part_1(start):
    directions = list(product([0, -1, 1], repeat=3))[1:]

    a = defaultdict(lambda: '.')
    b = defaultdict(lambda: '.')

    for y, line in enumerate(start):
        for x, char in enumerate(line):
            a[(x, y, 0)] = char

    dx, dy, dz = len(start[0]), len(start), 1

    for _ in range(6):

        iterate(a, b, dx, dy, dz, directions)

        a, b = b, a

        dx += 1
        dy += 1
        dz += 1

    return len(list(filter(lambda v: v == '#', a.values())))


def part_2(start):
    directions = list(product([0, -1, 1], repeat=4))[1:]

    a = defaultdict(lambda: '.')
    b = defaultdict(lambda: '.')

    for y, line in enumerate(start):
        for x, char in enumerate(line):
            a[(x, y, 0, 0)] = char

    dx, dy, dz, dw = len(start[0]), len(start), 1, 1

    for _ in range(6):
        iterate_4(a, b, dx, dy, dz, dw, directions)

        a, b = b, a

        dx += 1
        dy += 1
        dz += 1
        dw += 1

    return len(list(filter(lambda v: v == '#', a.values())))


print(part_1(start))
print(part_2(start))
