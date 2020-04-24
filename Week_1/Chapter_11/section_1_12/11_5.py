from Week_1.Chapter_11.section_1_12.point import Point


p = Point(20, 20)
q = Point(15, 15)
r = Point(20, 10)
s = Point(25, 15)

west = min(p.x, q.x, r.x, s.x)
east = max(p.x, q.x, r.x, s.x)
north = max(p.y, q.y, r.y, s.y)
south = min(p.y, q.y, r.y, s.y)

x = (west + east)/2
y = (south + north)/2

print(x, y)