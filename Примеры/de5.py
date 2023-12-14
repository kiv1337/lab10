def repeat(n):
    """Декоратор с аргументами"""
    def decorator(func):
        def wrapper(name):
            for el in range(n):
                result = func(name)
            return result
        
        return wrapper
    
    return decorator

@repeat(2)
def hi(name):
    print(f"Здравствуйте, {name}!")

hi("Станислав")
