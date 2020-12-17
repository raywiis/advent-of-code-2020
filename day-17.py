from itertools import product
from collections import defaultdict

f = open('./day-17-problem.txt')
start = [list(line) for line in f.read().splitlines()]

a = defaultdict(lambda: '.')
b = defaultdict(lambda: '.')

a_4 = defaultdict(lambda: '.')
b_4 = defaultdict(lambda: '.')

debug = defaultdict(lambda: '0')

for y, line in enumerate(start):
    for x, char in enumerate(line):
        a[(x, y, 0)] = char
        a_4[(x, y, 0, 0)] = char


directions = list(product([0, -1, 1], repeat=3))[1:]
directions_4 = list(product([0, -1, 1], repeat=4))[1:]

def count_activated_around(a, pos):

    total = 0
    for d in directions:
        x, y, z = pos
        x += d[0]
        y += d[1]
        z += d[2]
        if a[(x, y, z)] == '#':
            total += 1

    return total

def show(a, dx, dy, dz):
    for z in range(-dz, dz + 1):
        print('\n\n', z)
        for y in range(-dy, dy + 1):
            line = []
            for x in range(-dx, dx + 1):
                pos = (x, y, z)
                line += [a[pos]]
            print(''.join(line))



def iterate(start, to, dx, dy, dz):
    for z in range(-dz, dz + 1):
        for y in range(-dy, dy + 1):
            for x in range(-dx, dx + 1):
                pos = (x, y, z)
                activated = count_activated_around(start, pos)
                
                debug[(pos)] = str(activated)
                if activated == 3:
                    to[pos] = '#'
                elif activated == 2 and start[pos] == '#':
                    to[pos] = '#'
                else:
                    to[pos] = '.'


def count_activated_around_4(a, pos):

    total = 0
    for d in directions_4:
        x, y, z, w = pos
        x += d[0]
        y += d[1]
        z += d[2]
        w += d[3]
        if a[(x, y, z, w)] == '#':
            total += 1

    return total

def iterate_4(start, to, dx, dy, dz, dw):
    for w in range(-dw, dw + 1):
        for z in range(-dz, dz + 1):
            for y in range(-dy, dy + 1):
                for x in range(-dx, dx + 1):
                    pos = (x, y, z, w)
                    activated = count_activated_around_4(start, pos)
                    
                    debug[(pos)] = str(activated)
                    if activated == 3:
                        to[pos] = '#'
                    elif activated == 2 and start[pos] == '#':
                        to[pos] = '#'
                    else:
                        to[pos] = '.'




def part_1(a, b):
    dx, dy, dz = len(start[0]), len(start), 1
    #show(a, dx, dy, dz)

    for i in range(6):

        iterate(a, b, dx, dy, dz)
        #show(debug, dx, dy, dz)

        a, b = b, a

        dx += 1
        dy += 1
        dz += 1

    #show(a, dx, dy, dz)
    return len(list(filter(lambda v: v == '#', a.values())))
        
def part_2(a_4, b_4):
    dx, dy, dz, dw = len(start[0]), len(start), 1, 1

    for i in range(6):
        #print('gen', i)

        iterate_4(a_4, b_4, dx, dy, dz, dw)

        a_4, b_4 = b_4, a_4

        dx += 1
        dy += 1
        dz += 1
        dw += 1

    return len(list(filter(lambda v: v == '#', a_4.values())))

print(part_1(a, b))
print(part_2(a_4, b_4))
