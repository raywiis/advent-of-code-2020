f = open('./day-09-problem.txt')
numbers = [int(num) for num in f.read().splitlines()]

lookback = 25

gtarget = 0
for i in range(lookback, len(numbers)):
    sumables = numbers[i - lookback: i]
    target = numbers[i]

    ss = set(sumables)
    for a in sumables:
        if (target - a) in ss:
            break
    else:
        gtarget = target
        print(target)
        break

bottom = 0
top = 2

while top < len(numbers):
    rang = numbers[bottom:top]
    range_sum = sum(rang)
    if range_sum == gtarget:
        print(min(rang) + max(rang))
        break
    elif range_sum < gtarget:
        top += 1
    elif range_sum > gtarget:
        bottom += 1

    assert bottom + 2 <= top
