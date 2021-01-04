from collections import deque

data = open('./day-22-problem.txt').read().split('\n\n')

[p1, p2] = data

p1 = deque([int(c) for c in p1.splitlines()[1:]])
p2 = deque([int(c) for c in p2.splitlines()[1:]])


def calc_score(cards):
    winner = list(reversed(list(cards)))
    score = 0
    for mult, i in enumerate(winner):
        score += (mult + 1) * i
    return score


def part1(a, b):
    while len(a) > 0 and len(b) > 0:
        ca = a.popleft()
        cb = b.popleft()

        if ca > cb:
            a += [ca, cb]
        else:
            b += [cb, ca]

    winner = b if len(a) == 0 else a

    print(calc_score(winner))


def recursive_combat(a, b):
    a = deque(a.copy())
    b = deque(b.copy())

    snaps = set()
    while len(a) > 0 and len(b) > 0:
        snap = str(a) + ' ' + str(b)

        if snap in snaps:
            return 'a'
        snaps.add(snap)

        ca = a.popleft()
        cb = b.popleft()

        if ca <= len(a) and cb <= len(b):
            if recursive_combat(list(a)[:ca], list(b)[:cb]) == 'a':
                a += [ca, cb]
            else:
                b += [cb, ca]
        else:
            if ca > cb:
                a += [ca, cb]
            else:
                b += [cb, ca]

    if len(a) > 0:
        return 'a'
    else:
        return 'b'


def part2(a, b):
    snaps = set()
    while len(a) > 0 and len(b) > 0:

        snap = str(a) + ' ' + str(b)
        if snap in snaps:
            print(calc_score(a))
            return
        snaps.add(snap)

        ca = a.popleft()
        cb = b.popleft()

        if ca <= len(a) and cb <= len(b):
            if recursive_combat(list(a)[:ca], list(b)[:cb]) == 'a':
                a += [ca, cb]
            else:
                b += [cb, ca]
        else:
            if ca > cb:
                a += [ca, cb]
            else:
                b += [cb, ca]

    winner = b if len(a) == 0 else a
    print(calc_score(winner))


part1(p1.copy(), p2.copy())

part2(p1, p2)
