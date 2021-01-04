f = open('./day-06-problem.txt')
data = f.read().split('\n\n')

data = [a.splitlines() for a in data]

def get_set_1(group):
    total = set()

    for person in group:
        answers = set(person)
        total = total.union(answers)

    return total

def get_set_2(group):
    total = set(group[0])

    for p in group:
        answers = set(p)
        total = total.intersection(answers)

    return total


counts = [len(get_set_1(g)) for g in data]

print(sum(counts))

counts = [len(get_set_2(g)) for g in data]

print(sum(counts))

