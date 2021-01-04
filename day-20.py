from collections import defaultdict, deque

tiles = open('./day-20-problem.txt').read().split('\n\n')


def parse_tile(tile_string):
    parts = tile_string.splitlines()

    tile_id = int(parts[0].split(' ')[1][:-1])

    tile_body = parts[1:]
    return (tile_id, tile_body)


tiles = [parse_tile(t) for t in tiles]


def t_top(tile):
    (_, body) = tile
    return body[0]


def t_right(tile):
    (_, body) = tile
    return ''.join([line[-1] for line in body])


def t_bottom(tile):
    (_, body) = tile
    return body[-1][::-1]


def t_left(tile):
    (_, body) = tile
    return ''.join([line[0] for line in body][::-1])


edge_to_tile = defaultdict(set)


def get_edges(tile, directions):
    edges = []
    for d in directions.items():
        (side, edge_fn) = d
        edges += [(side, edge_fn(tile))]
    return edges


directions = {
    'top': t_top,
    'right': t_right,
    'bottom': t_bottom,
    'left': t_left,
}

tile_by_id = {}

for t in tiles:
    (tile_id, tile) = t
    for (side, edge) in get_edges(t, directions):
        edge_to_tile[edge].add((side, tile_id))

    tile_by_id[tile_id] = tile


def print_positions(positions):
    min_x = min(map(lambda x: x[0][0], positions.items()))
    max_x = max(map(lambda x: x[0][0], positions.items()))
    min_y = min(map(lambda x: x[0][1], positions.items()))
    max_y = max(map(lambda x: x[0][1], positions.items()))

    tile_size = len(next(iter(positions.values()))[1])

    for y in range(min_y, max_y + 1):
        fat_row = []
        for x in range(min_x, max_x + 1):
            pos = (x, y)
            if pos in positions:
                tile = positions[pos][1]
                fat_row += [tile]
            else:
                fat_row += [[' ' * tile_size] * tile_size]

        for i in range(tile_size):
            line = ' '.join([t[i] for t in fat_row])
            print(line)
        print()


def remove_edges(t):
    for (side, edge) in get_edges(t, directions):
        edge_to_tile[edge].remove((side, t[0]))

        if len(edge_to_tile[edge]) == 0:
            del edge_to_tile[edge]


first_tile = tiles[0]
initial_pos = (0, 0)
positions = {
    initial_pos: first_tile,
}
remove_edges(first_tile)
tile_queue = deque([(initial_pos, first_tile)])

coord_modifiers = {
    'top': lambda pos: (pos[0], pos[1] - 1),
    'right': lambda pos: (pos[0] + 1, pos[1]),
    'bottom': lambda pos: (pos[0], pos[1] + 1),
    'left': lambda pos: (pos[0] - 1, pos[1]),
}


def flip_hor(t):
    (tile_id, t_body) = t
    n_body = t_body.copy()[::-1]
    tile_by_id[tile_id] = n_body
    return (tile_id, t_body)


def flip_ver(t):
    (tile_id, t_body) = t
    n_body = [line[::-1] for line in t_body]
    tile_by_id[tile_id] = n_body
    return (tile_id, n_body)


def rot_count(a, b):
    direction_nums = {
        'top': 0,
        'right': 1,
        'bottom': 2,
        'left': 3
    }

    an = direction_nums[a]
    bn = direction_nums[b]

    if ((an + 3) % 4) == bn:
        return 3
    elif ((an + 1) % 4) == bn:
        return 1
    elif (an % 4) == bn:
        return 2
    return 0


def rot_once(body):
    t_body = []
    for col in range(len(body[0])):
        t_body += [((''.join([line[col] for line in body]))[::-1])]
    return t_body


def rotate(t, count):
    (tile_id, tile_body) = t

    n_body = tile_body.copy()
    for _ in range(count):
        t_body = []
        for col in range(len(n_body[0])):
            t_body += [((''.join([line[col] for line in n_body]))[::-1])]
        n_body = t_body

    tile_by_id[tile_id] = n_body

    return (tile_id, n_body)


while len(tile_queue) > 0:
    (pos, t) = tile_queue.pop()

    for (d, edge_fn) in directions.items():
        next_pos = coord_modifiers[d](pos)

        if next_pos in positions:
            continue

        matches = edge_to_tile[edge_fn(t)]

        invert = True

        if len(matches) == 0:
            matches = edge_to_tile[edge_fn(t)[::-1]]
            invert = False

        if len(matches) == 0:
            continue

        (match_side, match_id) = next(iter(matches))

        remove_edges((match_id, tile_by_id[match_id]))

        rots = rot_count(d, match_side)
        rotate((match_id, tile_by_id[match_id]), rots)

        if invert:
            if (d == 'left') or (d == 'right'):
                flip_hor((match_id, tile_by_id[match_id]))
            else:
                flip_ver((match_id, tile_by_id[match_id]))

        tile_queue.append((next_pos, (match_id, tile_by_id[match_id])))

        positions[next_pos] = (match_id, tile_by_id[match_id])

assert len(positions) == len(tile_by_id)


def positions_to_grid(positions):
    min_x = min(map(lambda x: x[0][0], positions.items()))
    max_x = max(map(lambda x: x[0][0], positions.items()))
    min_y = min(map(lambda x: x[0][1], positions.items()))
    max_y = max(map(lambda x: x[0][1], positions.items()))

    grid = []
    for y in range(min_y, max_y + 1):
        row = []
        for x in range(min_x, max_x + 1):
            pos = (x, y)
            assert pos in positions
            row += [positions[pos]]
        grid += [row]
    return grid


grid = positions_to_grid(positions)

print(grid[0][0][0] * grid[0][-1][0] * grid[-1][0][0] * grid[-1][-1][0])


def grid_to_picture(grid):
    # Punch in
    tiles = []
    for row_idx, row in enumerate(grid):
        tiles += [[]]
        for t in row:
            new_tile = [line[1:-1] for line in t[1][1:-1]]
            tiles[row_idx] += [new_tile]

    picture = ''
    for row in tiles:
        for l_idx in range(len(row[0])):
            picture += ''.join([t[l_idx] for t in row]) + '\n'

    return picture


picture = grid_to_picture(grid).splitlines()

sea_monster_pattern = [
    '                  # ',
    '#    ##    ##    ###',
    ' #  #  #  #  #  #   ',
]


def loose_match(a, b):
    for idx, let in enumerate(a):
        if let == '#' and b[idx] != '#':
            return False
    return True


def match_monsters(pat, picture):
    picture_len = len(picture[0])
    monster_len = len(pat[0])
    monster_height = len(pat)

    matches = 0
    for row_offset in range(len(picture) - monster_height):
        for col_offset in range(picture_len - monster_len):
            match = True
            for p_idx, p_line in enumerate(pat):
                if not loose_match(
                    p_line,
                    picture[row_offset + p_idx][col_offset:]
                ):
                    match = False
            if match:
                matches += 1
    return matches


# sample transforms
# picture = rot_once(picture)

# problem transforms
picture = rot_once(rot_once(picture))

monsters_found = match_monsters(sea_monster_pattern, picture)

waves_per_monster = ''.join(sea_monster_pattern).count('#')
waves_in_picture = ''.join(picture).count('#')

print(waves_in_picture - (monsters_found * waves_per_monster))
