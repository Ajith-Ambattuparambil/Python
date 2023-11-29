#Pgm to import the rectangle and circle modules from graphics directory. Also using subpackage dgraphics wit cuboid and sphere area and volume

from graphics import rectangle,circle
from graphics.dgraphics import cuboid,sphere
#Area and perimeter of rectanle
l=int(input("Enter the length of rectangle in centimetres: "))
b=int(input("Enter the breadth of rectangle centimetres: "))
rectangle.area(l,b)
rectangle.perimeter(l,b)
#Area and perimeter of circle
r=int(input("Enter the radius of circle in centimetres: "))
circle.area(r)
circle.perimeter(r)

#volume and Area of cuboid
le=int(input("Enter the length of cuboid: "))
br=int(input("Enter the breadth of cuboid: "))
he=int(input("Enter the height of cuboid: "))
cuboid.area(le,br,he)
cuboid.volume(le,br,he)

#volume and Area of Sphere
r=int(input("Enter the radius of sphere in centimetres: "))
sphere.area(r)
sphere.volume(r)

'''Enter the length of rectangle in centimetres: 5
Enter the breadth of rectangle centimetres: 5
Area of rectangle =  25 square centimetres
Perimeter of rectangle =  20 cms
Enter the radius of circle in centimetres: 5
Area of the circle with radius 5 = 78.57142857142857 square centimetres
Perimeter of the circle with radius 5 = 31.428571428571427 cms
Enter the length of cuboid: 5
Enter the breadth of cuboid: 5
Enter the height of cuboid: 5
The area of cuboid =  150
The volume of cuboid =  125
Enter the radius of sphere in centimetres: 5
The area of sphere =  314.2857142857143
The volume of sphere =  523.8095238095237'''
