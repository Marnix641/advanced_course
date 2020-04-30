from Week_1.Chapter_11.section_1_12.point import Point
from Week_1.Chapter_11.section_2_6.rectangle import Rectangle

r = Rectangle(Point(0, 0), 10, 5)


print(r.contains(Point(0,0)))
print(r.contains(Point(3,3)))
print(not r.contains(Point(3,7)))
print(not r.contains(Point(3,5)))
print(r.contains(Point(3,4.999)))
print(not r.contains(Point(-3,-3)))
