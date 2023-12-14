class Rectangle:
    def __init__(self, side_a, side_b, side_c):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    @property
    def area(self):
        return self.side_a + self.side_b + self.side_c

rect = Rectangle(5, 6, 7)
print(rect.area)