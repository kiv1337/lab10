class CLass_decorator:
    """Декоратор в виде класса"""
    def __init__(self, function):
        self.function = function

    def __call__(self):
        print('ДО')
        self.function()
        print('ПОСЛЕ')


@CLass_decorator
def hello_world():
    print("hello, world!")

hello_world()