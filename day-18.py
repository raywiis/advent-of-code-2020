from functools import reduce

f = open('./day-18-problem.txt')

d = f.read().splitlines()


def calc_expr(line, start =0):

    total = 0
    op = '+'
    pos = start
    while pos < len(line):
        #print(line[pos], total)
        num = 0
        if line[pos] == '*' or line[pos] == '+':
            op = line[pos]
            pos += 1
            continue
        elif line[pos] == '(':
            num, pos = calc_expr(line, pos + 1)
        elif line[pos] == ')':
            return total, pos
        else: # assume number
            num = int(line[pos])

        if op == '*':
            total *= num
        elif op == '+':
            total += num
        else:
            raise 'unexpected op'

        pos += 1
    return total


exprs = [l.replace('(', '( ') for l in d]
exprs = [l.replace(')', ' )') for l in exprs]
exprs = [l.split(' ') for l in exprs]

vals = [calc_expr(l) for l in exprs]
print(sum(vals))

def calc_sum(a):
    return sum(int(e) for e in a.split('+'))

def calc_flat(t):
    t = ''.join(t)
    mults = [calc_sum(a) for a in t.split('*')]
    return str(reduce(lambda a, b: a * b, mults))


def calc_expr_2(line):
    stack = [[]]
    sp = 0
    idx = 0
    while idx < len(line):
        if line[idx] == '(':
            sp += 1
            stack.append([])
        elif line[idx] == ')':
            sp -= 1
            res = calc_flat(stack.pop())
            stack[sp] += [res]
        else:
            stack[sp] += [line[idx]]
        idx += 1

    return calc_flat(stack[0])
            





#print(calc_expr_2(exprs[0]))
vals_2 = [int(calc_expr_2(l)) for l in d]
print(sum(vals_2))

