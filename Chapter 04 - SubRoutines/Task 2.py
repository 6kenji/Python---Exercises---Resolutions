# A function is required that will be passed the radius of a circle and return the area and circumference

def area_circumference(radius):
    circ_area = 3.14 * (radius * radius)
    circ_circumf = 3.14 * radius * 2
    return circ_area, circ_circumf

radius_input = float(input('Insert the Radius of the circle: '))
circ_area,  circ_circumf  = area_circumference(radius_input)

print('The area of this circle is: ', circ_area)
print('The circumference of this circle is: ', circ_circumf)

print('The area and the circumference of this circle are: ', area_circumference(radius_input))