f = open('./day-8-problem.txt')
gapp = f.read().splitlines()

def run_app(swapIdx):
    ip = 0
    acc = 0
    used_ips = set()

    app = gapp.copy()

    while (ip not in used_ips) and ip < len(app):
        [op, num] = app[ip].split(' ')

        if ip == swapIdx:
            if op == 'nop':
                op = 'jmp'
            else:
                op = 'nop'
            

        used_ips.add(ip)
        if op == 'nop':
            ip += 1
            continue
        elif op == 'acc':
            acc += int(num)
            ip += 1
        elif op == 'jmp':
            ip += int(num)
        else:
            raise "unknown op"

    end = ip == len(app)

    return [end, acc]

for i in range(len(gapp)):
    if gapp[i].startswith('acc'):
        continue

    [end, acc] = run_app(i)

    if end:
        print(acc)
