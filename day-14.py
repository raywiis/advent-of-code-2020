f = open('./day-14-problem.txt')
program = f.read().splitlines()

def parse_mask(m):
    mask = m.split('=')[1].strip()
    zeroMask = int('0b' + mask.replace('X', '1'), 2)
    onesMask = int('0b' + mask.replace('X', '0'), 2)
    return zeroMask, onesMask

def parse_instruction(i):
    i = i.split('=')
    number = int(i[1].strip())
    location = int(i[0].strip()[4:-1])
    return location, number

memory = {}
zeroMask = 0
onesMask = 0

for i in program:
    if i.startswith('mask = '):
        zeroMask, onesMask = parse_mask(i)
        continue

    location, number = parse_instruction(i)
    number = (number & zeroMask) | onesMask
    memory[location] = number

print(sum(memory.values()))

def get_distribution(original_location, mask):
    x_count = mask.count('X')

    float_application = mask.replace('1', '0').replace('X', '1')
    float_application = int('0b' + float_application, 2)
    must_ones = int('0b' + mask.replace('X', '0'), 2)

    sanitized_og = (original_location & (~float_application))
    prepped_og = sanitized_og | must_ones

    locations = []
    ref_mask = mask.replace('1', '0')
    for i in range(pow(2, x_count)):
        local_addr = ref_mask

        for x in range(x_count):
            bit = i & 0b1
            local_addr = local_addr.replace('X', str(bit), 1)
            i = i >> 1

        local_addr = int('0b' + local_addr, 2)
        loc = prepped_og | local_addr

        locations.append(loc)

    return locations


memory = {}
mask = ''
for i in program:
    if i.startswith('mask = '):
        mask = i.split('=')[1].strip()
        continue

    location, number = parse_instruction(i)
    locations = get_distribution(location, mask)
    #print(locations)

    for loc in locations:
        memory[loc] = number


print(sum(memory.values()))
