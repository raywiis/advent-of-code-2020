entries = [int(x) for x in open('./day-1-problem.txt').read().splitlines()]

target = 2020
numbers = set()

for entry in entries:
    numbers.add(entry)

    if (target - entry) in numbers:
        print(entry * (target - entry))

for entry in entries:
    for fuck in entries:
        if entry + fuck >= target:
            continue
        else:
            if (target - entry - fuck) in numbers:
                print(entry * fuck * (target - entry - fuck))
                exit()
