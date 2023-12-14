class Classmethod:
    a = 10
    s = a ** 2
    @classmethod
    def function(cls):
        return f"Это @classmethod, s = {cls.s}"
    
print(Classmethod.function())