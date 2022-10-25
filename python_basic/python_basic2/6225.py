class Rectangle():
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def get_area(self):
        return self.__x * self.__y

if __name__ == '__main__':
    r1 = Rectangle(4, 5)
    print('사각형의 면적: {0}'.format(r1.get_area()))
