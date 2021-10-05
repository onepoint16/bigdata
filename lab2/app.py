import cpoint_1
import circle

pt = cpoint_1.Point(1,2)
print(pt.toString())
pt.move(10,10)
print(pt.toString())

circ = circle.Circle(pt, 5)
print(circle.Circle.toString(circ))


