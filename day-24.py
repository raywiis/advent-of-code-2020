import collections

tiles = collections.defaultdict(lambda: 'W')

f = open('./day-24-problem.txt')
tile_paths = f.read().splitlines()

# Using axial coordinates for hex grids

directions = {
	'A': (-1, 0),
	'B': (0, 1),
	'C': (1, 1),
	'D': (1, 0),
	'E': (0, -1),
	'F': (-1, -1)
}

def decode_path(p):
	d = p.replace('se', 'D')
	d = d.replace('sw', 'E')
	d = d.replace('nw', 'A')
	d = d.replace('ne', 'B')
	d = d.replace('e', 'C')
	d = d.replace('w', 'F')

	return list(d)

def count_black_neighbors(tiles, pos):
	(x, y) = pos
	total = 0
	for (dx, dy) in directions.values():
		lx = x + dx
		ly = y + dy

		if ((lx, ly) in tiles) and 'B' == tiles[(lx, ly)]:
			total += 1

	return total


def follow_directions(dirs, start):
	(x, y) = start
	for d in dirs:
		(dx, dy) = directions[d]
		x += dx
		y += dy
	return (x, y)

for p in tile_paths:
	d = decode_path(p)
	pos = follow_directions(d, (0, 0))

	if tiles[pos] == 'W':
		tiles[pos] = 'B'
	else:
		tiles[pos] = 'W'

black_count = sum([1 for t in tiles.values() if t == 'B'])
print(black_count)

for _ in range(100):
	n_tiles = collections.defaultdict(lambda: 'W')
	min_x = min(map(lambda p: p[0], tiles.keys()))
	max_x = max(map(lambda p: p[0], tiles.keys()))
	min_y = min(map(lambda p: p[1], tiles.keys()))
	max_y = max(map(lambda p: p[1], tiles.keys()))

	for x in range(min_x - 1, max_x + 2):
		for y in range(min_y - 1, max_y + 2):
			pos = (x, y)
			t = tiles[pos]
			neighbors = count_black_neighbors(tiles, pos)

			if t == 'B' and (neighbors == 0 or neighbors > 2):
				n_tiles[pos] = 'W'
			elif t == 'W' and neighbors == 2:
				n_tiles[pos] = 'B'
			else:
				n_tiles[pos] = t
		
	tiles = n_tiles

black_count = sum([1 for t in tiles.values() if t == 'B'])
print(black_count)
