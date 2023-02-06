# Program a system that takes as inputs:
#   The length of the base of a triangle
#   The perpendicular height of the triangle
# The system should output the area of the triangle

# Receive and store the variables length of the base and perpendicular height of the triangle

base = float(input('Insert the length of the base of a triangle: '))
height = float(input('Insert the height of the triangle: '))

triangle_area = (base * height) / 2

# Display the value of the area

print('The area of the given triangle is: ', triangle_area)