from Week_1.Chapter_11_1_12.section_1_12.point import Point

p = Point(10, 25)
q = Point(5, 15)

print(p.x, p.y, q.x, q.y)
print(p.distance_from_origin())
print(q.distance_from_origin())
print(p)

print(p.x, -p.y)
print(p.slope_of_origin())

print(p.get_line(q))



def slope(q):
    return ((q.y-p.y)/(q.x-p.x))

def constant(q):
    return (p.y-(slope(q)*p.x))

print(slope(q))
print(constant(q))
print("The formula is: y =", slope(q), "x +", constant(q))
