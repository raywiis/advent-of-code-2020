f = open('./day-12-problem.txt')
data = f.read().splitlines()

facing = {
    0: 'N',
    90: 'E',
    180: 'S',
    270: 'W',
}

vectors = {
    'N': (0, 1),
    'E': (1, 0),
    'S': (0, -1),
    'W': (-1, 0),
}


def rotateLeft(pos, angle):
    (a, b) = pos

    for _ in range(angle // 90):
        (a, b) = (-b, a)

    return (a, b)


def rotateRight(pos, angle):
    (a, b) = pos

    for _ in range(angle // 90):
        (a, b) = (b, -a)

    return (a, b)


position = (0, 0)
waypoint = (10, 1)
angle = 90
for action in data:
    (h, v) = position
    (dh, dv) = (0, 0)
    distance = int(action[1:])

    if action[0] == 'F':
        (dh, dv) = vectors[facing[angle]]
    elif action[0] == 'L':
        angle = (angle - distance) % 360
        distance = 0
    elif action[0] == 'R':
        angle = (angle + distance) % 360
        distance = 0
    else:
        (dh, dv) = vectors[action[0]]

    position = (h + distance * dh, v + dv * distance)

total_distance = abs(position[0]) + abs(position[1])
print(total_distance)

position = (0, 0)
waypoint = (10, 1)
for action in data:
    (h, v) = position
    (dh, dv) = (0, 0)
    distance = int(action[1:])

    if action[0] == 'F':
        (dh, dv) = waypoint
        position = (h + dh * distance, v + dv * distance)
    elif action[0] == 'L':
        waypoint = rotateLeft(waypoint, distance)
    elif action[0] == 'R':
        waypoint = rotateRight(waypoint, distance)
    else:
        (dh, dv) = vectors[action[0]]
        waypoint = (waypoint[0] + dh * distance, waypoint[1] + dv * distance)

total_distance = abs(position[0]) + abs(position[1])
print(total_distance)
