f = open('./day-04-problem.txt')

batch = f.read().split('\n\n')
batch = [e.split() for e in batch]
batch = [dict([tuple(a.split(':')) for a in e]) for e in batch]


def is_valid_passport(p):
    if ('byr' in p and 'iyr' in p and 'eyr' in p and 'hgt' in p and
       'hcl' in p and 'ecl' in p and 'pid' in p):
        return True
    return False


def valid_fields(p):
    bir = int(p['byr'])
    iyr = int(p['iyr'])
    eyr = int(p['eyr'])
    hgt = p['hgt']

    if bir < 1920 or bir > 2002:
        return False

    if iyr < 2010 or iyr > 2020:
        return False

    if eyr < 2020 or eyr > 2030:
        return False

    if hgt.endswith('cm'):
        cm = int(hgt[:-2])
        if cm < 150 or cm > 193:
            return False

    if hgt.endswith('in'):
        inc = int(hgt[:-2])
        if inc < 59 or inc > 76:
            return False

    hcl = p['hcl']
    if not hcl.startswith('#') and len(hcl) != 7:
        return False

    try:
        int('0x' + hcl[1:], 0)
    except ValueError:
        return False

    if p['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return False

    if len(p['pid']) != 9:
        return False
    try:
        int(p['pid'])
    except ValueError:
        return False

    if not (hgt.endswith('cm') or hgt.endswith('in')):
        print(p)
        return False

    return True


count = 0
for p in batch:
    if is_valid_passport(p):
        if valid_fields(p):
            count += 1

# 154 - too high
# 153 -
print(count)
