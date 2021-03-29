f = open('./day-11-problem.txt')

area = [[spot for spot in line] for line in f.read().splitlines()]
reference = [line.copy() for line in area]

height = len(area)
width = len(area[0])


def safe_count(area, x, y):
    if x < 0 or x >= len(area):
        return 0

    if y < 0 or y >= len(area[0]):
        return 0

    if area[x][y] != '#':
        return 0

    return 1


def count_adjacent_seats(area, x, y):
    return sum([
        safe_count(area, x - 1, y - 1),
        safe_count(area, x - 1, y),
        safe_count(area, x - 1, y + 1),
        safe_count(area, x, y - 1),
        safe_count(area, x, y + 1),
        safe_count(area, x + 1, y - 1),
        safe_count(area, x + 1, y),
        safe_count(area, x + 1, y + 1)
    ])


def safe_seen(area, x, y, dx, dy):
    x += dx
    y += dy
    while x >= 0 and x < len(area) and y >= 0 and y < len(area[0]):
        if area[x][y] == 'L':
            return 0
        elif area[x][y] == '#':
            return 1

        x += dx
        y += dy

    return 0


def count_seen_seats(area, x, y):
    return sum([
        safe_seen(area, x, y, -1, -1),
        safe_seen(area, x, y, -1, 0),
        safe_seen(area, x, y, -1, 1),
        safe_seen(area, x, y, 0, -1),
        safe_seen(area, x, y, 0, 1),
        safe_seen(area, x, y, 1, -1),
        safe_seen(area, x, y, 1, 0),
        safe_seen(area, x, y, 1, 1),
    ])


changes = 1
temp = [line.copy() for line in area]

while changes != 0:
    changes = 0

    next_area = temp

    for idx in range(height * width):
        x = idx // width
        y = idx % width

        if reference[x][y] == '.':
            continue

        taken_seats = count_seen_seats(area, x, y)
        # taken_seats += count_adjacent_seats(area, x, y)

        if area[x][y] == 'L' and taken_seats == 0:
            next_area[x][y] = '#'
            changes += 1
        elif area[x][y] == '#' and taken_seats >= 5:  # 4 for part 1
            next_area[x][y] = 'L'
            changes += 1
        else:
            next_area[x][y] = area[x][y]

    temp = area
    area = next_area


total = ''.join([''.join(line) for line in area]).count('#')

print(total)
