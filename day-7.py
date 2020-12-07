import re

f = open('./day-7-problem.txt')
data = f.read().splitlines()

def parse_rule(line):
    [outer, inner] = line.split('contain')
    outer = outer[:-5].strip()

    if inner == ' no other bags.':
        inner = dict()
    else:
        inner = re.split('bags?,', inner)
        inner[len(inner) - 1] = inner[len(inner) - 1][:-5]
        inner = [i.strip() for i in inner]
        inner = [i.split(' ') for i in inner]
        inner = [(' '.join(i[1:]), int(i[0])) for i in inner]
        inner = dict(inner)

    return (outer, inner)


rules = []
for line in data:
    (outer, inner) = parse_rule(line)
    rules.append([outer, inner])


queue = ['shiny gold']
counted_bags = set()
while len(queue) > 0:
    target = queue.pop(0)
    counted_bags.add(target)

    for rule in rules:
        [outer, inner] = rule

        if target in inner and outer not in counted_bags:
            queue.append(outer)

print(len(counted_bags) - 1)


rules = dict([(i[0], i[1]) for i in rules])
def count_inside_bags(color):
    inner = rules[color]

    if len(inner) == 0:
        return 1
    else:
        bags = [(i[1] * count_inside_bags(i[0])) for i in inner.items()]
        count = sum(bags) + 1
        return count

# 195 - too low
print(count_inside_bags('shiny gold') - 1)

