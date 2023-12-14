def third_decorator(func):
    """Декоратор для функции с неизвестным количеством аргументов"""
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return wrapper


@third_decorator
def unknown_arguments(*args, **kwargs):
    print("args:", args, "kwargs:", kwargs)


unknown_arguments(1, 2, 3, a=4, b=5)