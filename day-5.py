f = open('./day-5-problem.txt')
passes = f.read().splitlines()

def get_position(p):
    row_upper = 127
    row_lower = 0
    row_step = 128 / 2

    for i in range(0, 7):
        if p[i] == 'F':
            row_upper -= row_step
        elif p[i] == 'B':
            row_lower += row_step
        else:
            raise "row fuck"

        row_step /= 2

    assert(row_upper == row_lower)

    row = row_upper

    col_upper = 7
    col_lower = 0
    col_step = 8 / 2

    for i in range(7,  10):
        if p[i] == 'R':
            col_lower += col_step
        elif p[i] == 'L':
            col_upper -= col_step
        else:
            raise "col fuck"
        col_step /= 2

    assert(col_lower == col_upper)

    col = col_upper

    return (row, col)


def seat_id(s):
    (row, col) = s
    return (row * 8) + col

seats = [[(row, col) for col in range(0, 7)] for row in range(0, 127)]
positions = [get_position(s) for s in passes]

ids = [seat_id(p) for p in positions]
print(max(ids))

for pos in positions:
    (row, col) = pos
    seats[int(row) - 1][int(col) - 1] = (-1, -1)

# 63 * 8 + 4 = 508 - too low
# 64 * 8 + 5 = 517 - yes
#print(seats)
print(seat_id((64, 5)))
