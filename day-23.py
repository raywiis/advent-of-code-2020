import collections
from itertools import islice

def list_to_map(data):
	c = {}
	c[data[0]] = (data[-1], data[1])
	c[data[-1]] = (data[-2], data[0])

	for i in range(1, len(data) - 1):
		c[data[i]] = (data[i - 1], data[i + 1])

	return c


def run(c, start, iterations):
	min_val = min(c.keys())
	max_val = max(c.keys())

	current = start
	for _ in range(iterations):
		(l1, n1) = c[current]
		(_, n2) = c[n1]
		(_, n3) = c[n2]
		(l0, n4) = c[n3]

		c[current] = (l1, n4)

		sl = set([n1, n2, n3])

		target = current - 1
		if target < min_val:
			target = max_val

		while target in sl:
			target -= 1
			if target < min_val:
				target = max_val

		(l2, r1) = c[target]
		c[target] = (l2, n1)

		(_, r2) = c[r1]
		c[r1] = (n3, r2)

		c[n1] = (target, n2)
		c[n3] = (l0, r1)

		(_, current) = c[current]

#data = '389125467' # sample
data = '853192647' # my input

data = [int(n) for n in data]


c = list_to_map(data)

run(c, data[0], 100)

(_, curr) = c[1]
p1_ans = str(curr)
for i in range(7):
	(_, curr) = c[curr]
	p1_ans += str(curr)
print(p1_ans)

data = data + list(range(10, 1000001))

c = list_to_map(data)

run(c, data[0], 10000000)

(_, n1) = c[1]
(_, n2) = c[n1]
print(n1 * n2)
