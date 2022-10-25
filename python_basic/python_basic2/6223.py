class Circle():
    def __init__(self, radius=2):
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius

    def get_area(self):
        return self.radius * self.radius * 3.14

if __name__ == '__main__':
    c = Circle()
    print('원의 면적: {0}'.format(c.get_area()))
