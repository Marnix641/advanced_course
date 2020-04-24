class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance_from_origin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

    def slope_of_origin(self):
        return (self.y /self.x)

    def get_line(p1, q):
        mx = ((p1.y - q.y) / (p1.x - q.x))
        my = ((p1.y - mx * p1.x))
        return Point(mx, my)

