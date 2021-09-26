"""
Написать рекурсивную функцию check_number, которая должна возвращать True,
если переданное ей число n является степенью двойки (1 тоже степень двойки) и
False, если нет

Нельзя пользоваться операцией возведения в степень
"""


def check_number(n):
    if n % 2 == 0:
        n = n / 2
        return check_number(n)
    elif n == 2 or n == 1:
        return True
    else:
        return False


print(check_number(8))
