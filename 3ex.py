class Point:
    def __init__(self, x, y):
        self.__x = None
        self.__y = None
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) is int or float:
            self.__x = x
        else:
            return None

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) is int or float:
            self.__y = y
        else:
            return None


point = Point("a", 10)

print(point.x)  # None
print(point.y)  # 10