from Week_1.Chapter_11.section_1_12.point import Point
from Week_1.Chapter_11.section_2_6.rectangle import Rectangle

target = Rectangle(Point(0, 5), 10, 5)
bullet = Rectangle(Point(10, 1), 1, 1)

print(target.collide(bullet))