"""
Написать генератор fibonacci, которая принимает номер значения num_count
из чисел Фибоначчи и выводит на экран результат до заданного значения.

Номер значения нужно проверить

Пример:

fibonacci(0) -> raise ValueError('Введите значение больше 1')
fibonacci(5)
1
2
3
5
8
Traceback (most recent call last):
File «C:/Python/Python3/python_generator.py», line 29, in
print(next(fib))
StopIteration
"""


def fibonacci(num_count):
    start = 0
    fib_1 = 0
    fib_2 = 1
    if num_count > 1:
        while start < num_count:
            fib_1, fib_2 = fib_2, fib_1 + fib_2
            start += 1
            yield fib_1
    else:
        raise ValueError('Введите значение больше 1')


a = fibonacci(4)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
