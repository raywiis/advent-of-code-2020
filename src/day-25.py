

def transform(sm, divisor, loops, initial_value=1):
    value = initial_value

    for _ in range(loops):
        value *= sm
        value %= divisor

    return value


def find_loop_count(sm, divisor, key):
    value = 1
    loop = 0

    while value != key:
        loop += 1
        value *= sm
        value %= divisor

    return loop


subject_number = 7
divisor = 20201227


# Sample
# card_pub_key = 17807724
# door_pub_key = 5764801

# Problem
card_pub_key = 15113849
door_pub_key = 4206373

card_ls = find_loop_count(subject_number, divisor, card_pub_key)
door_ls = find_loop_count(subject_number, divisor, door_pub_key)

print(card_ls)
print(door_ls)

encryption_key = transform(door_pub_key, divisor, card_ls)
print(encryption_key)

assert encryption_key == transform(card_pub_key, divisor, door_ls)


# 12917057 - too high
