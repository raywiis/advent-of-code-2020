from functools import reduce
f = open('./day-10-problem.txt')
adapters = [int(i) for i in f.read().splitlines()]
adapters.sort()

cap = max(adapters) + 3

diffs = [0, 0, 1]
current = 0

diffmap = []
for i in adapters:
    diff = i - current

    assert(diff < 4 and diff > 0)

    diffmap.append(diff)

    current = i
    diffs[diff - 1] += 1

print(diffs[0] * diffs[2])

cache = {
    1: 1,
    2: 2,
    3: 4
}


def get_iters(target):
    if target not in cache:
        assert(target > 3)
        cache[target] = sum(
            [get_iters(target - i) for i in range(1, 4)]
        )

    return cache[target]


diffmap = ''.join([str(i) for i in diffmap]).split('3')
diffmap = list(filter(lambda x: x > 0, [len(x) for x in diffmap]))
diffmap = [get_iters(i) for i in diffmap]

target = reduce(lambda a, b: a * b, diffmap)

print(target)
