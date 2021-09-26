"""
Напишите функцию yes_or_no, которая принимает список из целых чисел,
проходит по нему и выводит Yes, если число уже встречалось и No, если нет
"""


def yes_or_no(new_list):
    my_set = set()
    set_count = len(my_set)
    for i in new_list:
        my_set.add(i)
        if set_count < len(my_set):
            set_count += 1
            yield "No"
        else:
            yield "Yes"


some_set = [4, 4, 5, 1, 9, 1, 7, 4, 1, 8]
n = yes_or_no(some_set)
print(next(n))
print(next(n))
print(next(n))
print(next(n))
print(next(n))
print(next(n))
print(next(n))
print(next(n))
print(next(n))
print(next(n))
