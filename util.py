from random import randint, choice
import string

def random_nip_11():
    return randint(10000000000, 99999999999)

def random_nip_16():
    return randint(100000000000000000, 999999999999999999)

def random_part_number():
    part1 = ''.join([str(randint(0, 9)) for _ in range(5)])
    part2 = ''.join([str(randint(0, 9)) for _ in range(3)])
    return 'PL-' + part1 + '-' + part2

def random_serial_number():
    part1 = str(randint(0,9))
    part2 = choice(string.ascii_lowercase)
    part3 = ''.join([str(randint(0, 9)) for _ in range(3)])
    return part1 + part2 + part3
