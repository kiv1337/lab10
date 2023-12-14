def first_decorator(func):
    """Декоратор для функции без аргументов"""
    def wrapper():
        print('ДОПОЛНИТЕЛЬНО от first_decorator')
        result = func()
        return result
    return wrapper


@first_decorator
def say_message():
    print('Привет!')


say_message()