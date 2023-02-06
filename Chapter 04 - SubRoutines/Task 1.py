# A function is required that will be passed the radius of a circle and return the area

def area(radius):
    circ_area = 3.14 * (radius * radius)
    return circ_area

radius_input = float(input('Insert the Radius of the circle: '))

print('The area of this circle is: ', area(radius_input))