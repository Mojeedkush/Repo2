#Introduction
import math
n = input ("Hello User, Please enter your name:")

print ("Welcome",n, ",Kindly fill in the parameters of the following shapes to get their areas")

#Requesting for parameters of the triangle to calculate area
input ("Press enter to get the area of a triangle") 
	
a = float (input ("Please enter the value of the base of the triangle:"))

b = float (input (" Enter the value of it's height:"))

At = a * b * 0.5 #Formular for area of triangle

print ("The area of the triangle is:", float (At))

#Requesting for parameters of the sector to calculate area
input ("Press enter to find the area of a sector")

c = float (input("Enter the value of the angle of the sector:"))

d = float (input("Enter the value of it's radius:"))

Ase = math.pi * d * d *(c/360) #Formular for area of sector

print ("The area of the sector is:", float (Ase))

#Requesting for parameters of the square to calculate area
input ("Press enter to calculate the area of a square")
	
e = float (input ("Enter the value of a side of the square:"))

Asq = e * e #Formular for area of square

print ("The area of the square is:", float (Asq))

#Requesting for parameters of the trapezoid to calculate area
input ("Press enter to get the area of a trapezoid")
	
f = float (input ("Enter the value of the longer side of the trapezoid:"))

g = float (input ("Enter the value of it's shorter side:"))

h = float (input ("Enter the value of the height:"))

Atp = (f + g) * h * 0.5 #Formular for area of trapezoid

print ("The area of the trapezoid is:", float (Atp))

#Requesting for parameters of the cylinder to calculate area
input ("Press enter to find the area of a cylinder")
	
i = float (input ("Enter the radius of the cylinder:"))

j = float (input ("Enter the value of it's height:"))

Acy = 2 * math.pi * i * (i + j) 
'''Formular for
 area of a cylinder'''

print ("The total surface area of the cylinder is:", float (Acy))