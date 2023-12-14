from contextlib import contextmanager

@contextmanager
def my_context():
    print("Вход")
    
    yield
    
    print("Выход")


with my_context():
    print("Внутри_1")
    print("Внутри_2")
    print("Внутри_3")
