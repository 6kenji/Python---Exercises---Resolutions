# Program a system that takes as inputs:
#   The average speed of a car over the length of a journey
#   The distance that the car has to travel
# The system should output, in minutes the length of time the journey will take

# Receive and store the variables average speed and the distance that the car has to travel

car_speed = float(input('Insert the average speed of the car (in Km/h): '))
distance_to_travel = float(input('Insert the distance that the car has to travel in (km): '))

time_to_travel = (distance_to_travel / car_speed ) * 60

# Display the value of the area

print('The journey will take: ', time_to_travel, 'minutes. ')