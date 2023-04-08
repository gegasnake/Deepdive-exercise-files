class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return 'Rectangle Width = {0}, Height = {1}'.format(self.width, self.height)

    def __repr__(self):
        return 'Rectangle({0}, {1})'.format(self.width, self.height)

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.width == other.width and self.height == other.height
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area() < other.area()
        else:
            return NotImplemented

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        if width <= 0:
            raise ValueError("Width must be positive")
        else:
            self._width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        if height <= 0:
            raise ValueError("Width must be positive")
        else:
            self._height = height


r1 = Rectangle(10, 20)
r2 = Rectangle(10, 30)
print(r1.width)
print(r1.height)
print(r1.area())
print(r1.perimeter())
print(r1.__str__())
print(r1 == r2)
print(r1 == 100)
print(r1 < r2)
r1.width = -100
print(r1.width)


if __name__ == '__main__':
    print('')
