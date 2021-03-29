f = open('./day-16-problem.txt')


def parse_input(text):
    [fields, my_ticket, nearby_tickets] = text.split('\n\n')

    fields = [f.split(':') for f in fields.split('\n')]
    fields = [(n, cs.split('or')) for [n, cs] in fields]
    fields = [(n, [[int(a.strip()) for a in c.split('-')] for c in cs])
              for [n, cs] in fields]

    my_ticket = [int(v) for v in my_ticket.split('\n')[1].split(',')]

    nearby_tickets = [[int(v) for v in t.split(',')]
                      for t in nearby_tickets.split('\n')[1:-1]]

    return fields, my_ticket, nearby_tickets


def matches_constraint(v, constraint):
    (_, [[lr1, ur1], [lr2, ur2]]) = constraint
    match_1 = v >= lr1 and v <= ur1
    match_2 = v >= lr2 and v <= ur2
    return match_1 or match_2


def get_invalid_values(constraints, ticket):
    bad_vals = []
    for v in ticket:
        matches = [1 for field in constraints if matches_constraint(v, field)]
        if sum(matches) == 0:
            bad_vals += [v]

    return bad_vals


def part_1(constraints, tickets):
    errors = []
    for ticket in tickets:
        invalid_vals = get_invalid_values(constraints, ticket)
        errors += invalid_vals
    return sum(errors)


def rule_columns(rule, valid_tickets):
    cols = []
    for col in range(len(valid_tickets[0])):
        for t in valid_tickets:
            if not matches_constraint(t[col], rule):
                cols += [0]
                break
        else:
            cols += [1]

    return cols


def part_2(constraints, my_ticket, other_tickets):
    valid_tickets = list(filter(
            lambda t: len(get_invalid_values(constraints, t)) == 0,
            [my_ticket] + other_tickets
    ))

    matrix = [(r[0], rule_columns(r, valid_tickets)) for r in constraints]
    matrix = sorted(matrix, key=lambda row: sum(row[1]))

    positions = [None] * len(constraints)

    for (name, fields) in matrix:
        for idx, valid in enumerate(fields):
            if valid and positions[idx] is None:
                positions[idx] = name

    result = 1
    for idx, p in enumerate(positions):
        if p.startswith('departure'):
            result *= my_ticket[idx]

    return result


fields, my_ticket, nearby_tickets = parse_input(f.read())

print(part_1(fields, nearby_tickets))
print(part_2(fields, my_ticket, nearby_tickets))
