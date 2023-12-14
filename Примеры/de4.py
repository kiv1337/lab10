from functools import wraps


def fourth_decorator(func):
    """Декоратор, который перенял всю документацию от декорируемой функции"""
    @wraps(func)
    def wrapper():
        result = func()
        return result
    return wrapper


@fourth_decorator
def say_message():
    """Документация функции say_message"""
    print(say_message.__doc__)


say_message()