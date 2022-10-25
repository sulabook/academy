class Shape():
    def __init__(self, length):
        self.__length = length

    @property
    def length(self):
        return self.__length

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        super().__init__(length)

    def area(self):
        return self.length * self.length

if __name__ == '__main__':
    square = Square(3)
    print('정사각형의 면적: {0}'.format(square.area()))
