"""
Написать рекурсивную функцию sum_of_numbers, которая будет вычислять сумму
цифр целого числа.

Можно пользоваться только функциями, операторами и условиями.
"""


def sum_of_numbers(n):
    i = 0
    for j in str(n):
        i += int(j)
    return i


print(sum_of_numbers(33333))
