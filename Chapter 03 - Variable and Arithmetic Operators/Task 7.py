# Program a system that takes the three inputs required to calculate the area of a trapezoid and outputs the area

# Receive and store the three variables required to calculate the area of a trapezoid

superior_base = float(input('Insert the length superior base of the trapezium: '))
inferior_base = float(input('Insert the length inferior base of the trapezium: '))
height = float(input('Insert the height of the trapezium: '))

trapezoid_area = ((superior_base + inferior_base) * height) / 2

# Display the value of the area

print('The area of the given trapezium is: ', trapezoid_area)