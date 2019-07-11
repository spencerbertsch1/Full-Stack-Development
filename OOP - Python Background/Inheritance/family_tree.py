#Import our inheritance class
import inheritance


# Instantiate a new parent object named billy cyrus
billy_cyrus = inheritance.Parent('Cyrus', 'Blue')
#print(billy_cyrus.eye_color)
billy_cyrus.show_info()

# Instantiate a new Child object named Miley Cyrus
miley_cyrus = inheritance.Child('Cyrus', 'Blue', 5)
miley_cyrus.show_info()


#print(miley_cyrus.last_name)
#print(miley_cyrus.number_of_toys)