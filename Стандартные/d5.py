from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper():
        func()
    return wrapper

@my_decorator
def metadata():
    """Здесь могла быть ваша реклама"""
    pass

metadata()


print("Имя функции:", metadata.__name__)
print("Документация:", metadata.__doc__)
