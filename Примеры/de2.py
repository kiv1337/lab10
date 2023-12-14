def second_decorator(func):
    """Декоратор для функции с двумя аргументами"""
    def wrapper(a, b):
        result = func(a, b)
        return result
    return wrapper


@second_decorator
def multiply(a, b):
    print(f'Результат умножения: {a * b}')


multiply(10, 10)