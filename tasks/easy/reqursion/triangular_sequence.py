"""
Написать функцию triangular_sequence, которая принимает n и возвращает
последовательность следующего вида:

1
22
333
4444
55555
...

Например:

n = 3:
1
22
333

n = 6:
1
22
333
4444
55555
666666
"""


def triangular_sequence(n, any_str='', any_num=1):
    if n >= any_num:
        any_str += f'{str(any_num) * any_num}\n'
        return triangular_sequence(n, any_str, any_num=any_num + 1)
    else:
        return any_str


print(triangular_sequence(3))

