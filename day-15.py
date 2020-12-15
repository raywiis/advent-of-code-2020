#starting = [0, 3, 6] # sample
#starting = [1,3,2] # sample
#starting = [2,1,3] # sample
#starting = [3,1,2] # sample
starting = [19,20,14,0,9,1]


current = 1
numbers = {}
last_number = 0
for i in starting:
    numbers[i] = [current]
    current += 1
    last_number = i

while current <= 30000000: # 2020:

    if len(numbers[last_number]) == 1:
        if 0 not in numbers:
            numbers[0] = [current]
            continue
        else:
            numbers[0] = ([current] + numbers[0])[:2]
        last_number = 0
    else:
        [f, l] = numbers[last_number]
        new = f - l
        if new not in numbers:
            numbers[new] = [current]
            continue
        else:
            numbers[new] = ([current] + numbers[new])[:2]
        last_number = new

    current += 1



print(last_number)
