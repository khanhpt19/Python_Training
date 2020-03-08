import math
leg1 = input('Enter a number as length of leg 1: ')
while not leg1.isdigit():
    leg1 = input('Length of leg is invalid. Enter again: ')
leg2 = input('Enter a number as length of leg 2: ')
while not leg2.isdigit():
    leg2 = input('Length of leg is invalid. Enter again: ')
print('Hypotenuse :', math.sqrt(int(leg1) * int(leg1) + int(leg2) * int(leg2)))
print('The area of the triangle :', (int(leg1) * int(leg2))/2)
