# Volume of water in Aquarium

# Receive and store the variables height, width and depth of the aquarium

height = float(input('Insert the height of the aquarium in litres: '))
width = float(input('Insert the width of the aquarium in litres: '))
depth = float(input('Insert the depth of the aquarium in litres: '))

volume_value = (height * width * depth)/1000

# Display the value of the volume

print('The aquarium has a total of ', volume_value, 'litres or ', volume_value * 10000, 'cubic centimeters')