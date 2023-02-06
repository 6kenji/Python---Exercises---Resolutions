# Program a system that takes the length of one side of a regular octagon and outputs the resultant area of the octagon

# Receive and store the variable required to calculate the area of an octagon

octagon_lenght = float(input('Insert the height of the octagon: '))

octagon_area = 2 *(1+(2**0.5) ) * (octagon_lenght**2)

# Display the value of the area

print('The area of the given octagon is: ', octagon_area )