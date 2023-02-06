# A function is required that will be passed the radius of a circle and return the circumference (perimeter)

def circumference(radius):
    circ = 3.14 * radius * 2
    return circ

radius_input = float(input('Insert the Radius of the circle: '))
circumf = circumference(radius_input)

print('The circumference or perimeter of this circle is: ', circumf)