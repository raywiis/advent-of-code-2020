f = open('./day-21-problem.txt')
inp = f.read().splitlines()

data = []
totallergens = set()
all_ingredients = set()
for i in inp:
    [ingredients, allergens] = i.split('(contains ')
    ingredients = ingredients.strip()
    ingredients = ingredients.split(' ')

    allergens = set(allergens[:-1].split(', '))
    data += [(ingredients, allergens)]

    totallergens = totallergens.union(allergens)
    all_ingredients = all_ingredients.union(ingredients)

totallergens = list(totallergens)

mistery = []
for a in totallergens:
    possibilities = set(all_ingredients)
    for it in data:
        (ingredients, allergens) = it
        if a in allergens:
            possibilities = possibilities.intersection(ingredients)

    mistery += [(a, possibilities)]


solution = []
known_ingredients = set()
while len(mistery) > 0:
    mistery = sorted(mistery, key=lambda x: len(x[1]))
    
    (a, i) = mistery.pop(0)

    assert len(i) == 1

    i = next(iter(i))

    known_ingredients.add(i)

    solution += [(a, i)]

    for m in range(len(mistery)):
        if i in mistery[m][1]:
            mistery[m][1].remove(i)

non_allergic_sum = 0
for d in data:
    non_allergic_sum += len(set(d[0]) - known_ingredients)

print(non_allergic_sum)

solution = sorted(solution, key=lambda x: x[0])

ans = ','.join(list(map(lambda x: x[1], solution)))
print(ans)

