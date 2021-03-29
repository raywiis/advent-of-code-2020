from functools import reduce

f = open('./day-13-problem.txt')
[start, times] = f.read().splitlines()
start = int(start)
times = times.split(',')

offsets = [-1 if times[i] == 'x' else i for i in range(len(times))]
offsets = filter(lambda x: x >= 0, offsets)
offsets = list(offsets)

times = filter(lambda x: x != 'x', times)
times = [int(x) for x in times]

offsets = [times[i] - offsets[i] for i in range(len(times))]

mods = [start % time for time in times]
waits = [times[i] - mods[i] for i in range(len(times))]


min_wait = min(waits)
min_wait_idx = waits.index(min_wait)


print(min_wait * times[min_wait_idx])


def inverse_mod(a, m):
    m0 = m
    y = 0
    x = 1

    if (m == 1):
        return 0

    while (a > 1):
        q = a // m

        t = m

        m = a % m
        a = t
        t = y

        y = x - q * y
        x = t

    # Make x positive
    if (x < 0):
        x = x + m0

    return x


N = reduce(lambda a, b: a * b, times)
y = [N // times[i] for i in range(len(times))]
z = [inverse_mod(y[i], times[i]) for i in range(len(times))]
products = [offsets[i] * y[i] * z[i] for i in range(len(times))]
sol = sum(products) % N

print(sol)
