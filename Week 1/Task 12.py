# properties of a circle

diameter = input("Diameter of Circle: ")
ArcAngle = input("Arc Angle of circle: ")

radius = int(diameter) / 2
print("Radius of the cirlce: ", radius)
Area = 3.14 * (radius * radius)
print("Area of  the cirlce: ", Area)
Circumference = 3.14 * int(diameter)
print("Circumference of the cirlce: ", Circumference)
ArcLength = (Circumference * int(ArcAngle)) / 360
print("Arc Length of the circle: ", ArcLength)
