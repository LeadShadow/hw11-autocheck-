class Point:
    def __init__(self, x, y):
        self.__x = None
        self.__y = None
        self.y = y
        self.x = x

    @property
    def get_x(self):
        return self.__x

    @get_x.setter
    def get_x(self, x):
        self.__x = x

    @property
    def get_y(self):
        return self.__y

    @get_y.setter
    def get_y(self, y):
        self.__y = y


point = Point(5, 10)
print(point.y)
