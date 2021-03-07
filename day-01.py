entries = [int(x) for x in open('./day-01-problem.txt').read().splitlines()]

target = 2020
numbers = set()

for entry in entries:
    numbers.add(entry)

    if (target - entry) in numbers:
        print(entry * (target - entry))

for e1 in entries:
    for e2 in entries:
        if e1 + e2 >= target:
            continue
        else:
            if (target - e1 - e2) in numbers:
                print(e1 * e2 * (target - e1 - e2))
                exit()
