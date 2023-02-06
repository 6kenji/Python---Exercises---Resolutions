# Area and Circumference of a Circle with it's radius

# Request and store user input

PI = 3.1415
radius = float(input('Insert the circle radius: '))

area = PI * (radius * radius)
perimeter = 2 * PI * radius

# Display the value held in the variables

print('The area of this circle is: ', area)
print('The perimeter of this circle is: ', perimeter)