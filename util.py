from random import randint, choice
import calendar
import string

def random_nip_lt_11():
    return randint(0, 9999999999)

def random_nip_11():
    return randint(10000000000, 99999999999)

def random_nip_18():
    return randint(100000000000000000, 999999999999999999)

def random_nip_gt_18():
    return randint(1000000000000000000, 9999999999999999999)

def random_part_number():
    part1 = ''.join([str(randint(0, 9)) for _ in range(5)])
    part2 = ''.join([str(randint(0, 9)) for _ in range(3)])
    return 'PL-' + part1 + '-' + part2

def random_ref_des():
    part1 = str(randint(0,9))
    part2 = choice(string.ascii_lowercase)
    part3 = ''.join([str(randint(0, 9)) for _ in range(3)])
    return part1 + part2 + part3

def random_day(month, year):
    day = 1

    if month in [1, 3, 5, 7, 8, 10, 12]:
        day = randint(1, 31)
    elif month in [4, 6, 9, 11]:
        day = randint(1, 30)
    elif month == 2:

        if calendar.isleap(year):
            day = randint(1, 29)
        else:
            day = randint(1, 28)

    return day

def random_tgl_masuk():
    year_masuk, month_masuk, day_masuk = 0, 0, 0

    year_masuk = randint(2010, 2020)
    month_masuk = randint(1, 12)
    day_masuk = random_day(month_masuk, year_masuk)

    return year_masuk, month_masuk, day_masuk

def random_valid_tgl_masuk_and_expired():
    year_expired, month_expired, day_expired = 0, 0, 0
    year_masuk, month_masuk, day_masuk = random_tgl_masuk()

    month_masuk = str(month_masuk).zfill(2)
    day_masuk = str(day_masuk).zfill(2)

    year_expired = randint(year_masuk, 2024)
    month_expired = randint(1, 12)
    day_expired = random_day(month_expired, year_expired)

    year_expired = str(year_expired)
    month_expired = str(month_expired).zfill(2)
    day_expired = str(day_expired).zfill(2)

    return f"{month_masuk}{day_masuk}{year_masuk}", f"{month_expired}{day_expired}{year_expired}"

def random_invalid_tgl_masuk_and_expired():
    year_expired, month_expired, day_expired = 0, 0, 0
    year_masuk, month_masuk, day_masuk = random_tgl_masuk()

    month_masuk = str(month_masuk).zfill(2)
    day_masuk = str(day_masuk).zfill(2)

    year_expired = randint(year_masuk - 10, year_masuk - 1)
    month_expired = randint(1, 12)
    day_expired = random_day(month_expired, year_expired)

    year_expired = str(year_expired)
    month_expired = str(month_expired).zfill(2)
    day_expired = str(day_expired).zfill(2)

    return f"{month_masuk}{day_masuk}{year_masuk}", f"{month_expired}{day_expired}{year_expired}"
