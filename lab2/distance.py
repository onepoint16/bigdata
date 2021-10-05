import math as m 

x1 = int(input("please enter in a number for coordinate x1:"))

y1 = int(input("please enter in a number for coordinate y1:"))

x2 = int(input("please enter in a number for coordinate x2:"))

y2 = int(input("please enter in a number for coordinate y2:"))

coordinates1 = (x1,y1)

coordinates2 = (x2, y2)

xEquals = (x2 - x1)**2

yEquals = (y2 - y1)**2

distance = xEquals + yEquals

distance = (m.sqrt((x2 - x1))) + (m.sqrt((y2 - y1)))

print(distance)

