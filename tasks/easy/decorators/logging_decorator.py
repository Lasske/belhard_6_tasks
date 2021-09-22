"""
Написать функцию hello, которая принимает аргумент name - строку с именем и
выводит принтом "Привет, {name}"

Написать декоратор log_decorator, который перед выполнением
функции печатает на экран строку, вида
"Выполняем {func.__name__} с args: {args} и kwargs: {kwargs}".
После выполнения функции напечатать строку "Выполнено {func.__name__}"
"""


def log_decorator(n):
    def wrapper(*args, **kwargs):
        print(f"Выполняем {n.__name__} с args: {args} и kwargs: {kwargs}")
        result = n
        print(f"Выполнено {n.__name__}")
        return result
    return wrapper


@log_decorator
def hello(name):
    return print(f"Привет, {name}")


if __name__ == "__main__":
    name = "Viacheslav"
    print(hello())
