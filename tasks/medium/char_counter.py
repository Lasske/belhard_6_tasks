"""
Написать функцию count_char, которая принимает строковое значение STR_VAL,
из которого создает и возвращает словарь, следующего вида:
{
    'буква': количество-вхождений-в-строку
}

например: {
    'p': 2,
    'y': 1,
    ...
}

Нельзя пользоваться collections.Counter!
"""
STR_VAL = 'python is the fastest-growing major programming language'


def count_char(any_str):
    some_dict = {}
    for key in any_str:
        some_dict.setdefault(key, 0)
        some_dict[key] += 1
    return some_dict


print(count_char(STR_VAL))
