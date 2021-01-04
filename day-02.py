f = open('./day-02-problem.txt')
passwords = [line.split(':') for line in f.read().splitlines()]


def matches_rules_2(rule, password):
    first, second, letter = parse_rule(rule)

    if password[first] == letter and password[second] != letter:
        return True

    if password[first] != letter and password[second] == letter:
        return True

    return False


def matches_rules(rule, password):
    lower, upper, letter = parse_rule(rule)

    letter_map = dict()
    for let in password:
        if let not in letter_map:
            letter_map[let] = 0
        letter_map[let] += 1

    if letter not in letter_map:
        if lower == 0:
            return True
        else:
            return False

    letter_count = letter_map[letter]
    if letter_count <= upper and letter_count >= lower:
        return True
    else:
        return False


def parse_rule(ruleString):
    [numbers, letter] = ruleString.split(' ')
    [lower, upper] = numbers.split('-')

    return int(lower), int(upper), letter


count = 0
for [rule, password] in passwords:
    if matches_rules(rule, password):
        count += 1

print(count)

count = 0
for [rule, password] in passwords:
    if matches_rules_2(rule, password):
        count += 1

print(count)
