f = open('./day-19-problem.txt')

[rules, data] = f.read().split('\n\n')

rules = rules.splitlines()
data = data.splitlines()

rules = [r.split(':') for r in rules]
rules = [[r[0], r[1].strip().split('|')] for r in rules]

r_map = {}
for r in rules:
    [res, options] = r

    options = [opt.strip().split(' ') for opt in options]

    r_map[res] = options


def make_production(production):
    line = [a[1:2] for a in production]
    return ''.join(line)


def verify(message, production, r_map, cache):
    for idx, item in enumerate(production):

        if item in r_map:
            possibilities = r_map[item]

            for p in possibilities:

                uprod = production[:idx] + p + production[idx + 1:]
                valid = verify(message, uprod, r_map, cache)
                if (valid):
                    return True
            break
        else:
            continue
    else:
        test = make_production(production)
        cache.add(test)
        if test == message:
            return True
        else:
            return False
    return False


def part_1():
    results = 0
    cache = set()
    verify('x', ['0'], r_map, cache)

    for a in data:
        if a in cache:
            results += 1

    print(results)


def parts_verify(message, c42, c31, seglen):
    parts = [message[i:i + seglen] for i in range(0, len(message), seglen)]

    assert len(parts[-1]) == seglen

    # Handmade rules for the dataset
    # at least 2 c42 in front, at least c31 in back
    # count of c31 + 1 <= count of c42

    idx = 0
    c42c = 0
    c31c = 0

    while idx < len(parts):
        if parts[idx] not in c42:
            break
        c42c += 1
        idx += 1

    while idx < len(parts):
        if parts[idx] not in c31:
            break
        c31c += 1
        idx += 1

    if idx != len(parts):
        return False

    if c42c < 2 or c31c < 1:
        return False

    if c31c + 1 > c42c:
        return False
    return True


def part_2():
    cache = set()
    verify('x', ['42'], r_map, cache)
    cache_42 = cache

    cache = set()
    verify('x', ['31'], r_map, cache)
    cache_31 = cache

    res = 0
    for m in data:
        if parts_verify(m, cache_42, cache_31, 8):  # last arg 5 for sample-2
            res += 1
    print(res)


part_1()
part_2()
