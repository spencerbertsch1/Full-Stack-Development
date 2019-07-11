# Create parent class

class Parent():
    """
    We define the Parent class to identify the benifits of inheritance in OOP!
    """
    def __init__(self, last_name, eye_color):
        print("Parent constructor has been called!")
        self.last_name = last_name
        self.eye_color = eye_color

    def show_info(self):
        print("Last name: " + self.last_name)
        print("Eye color: " + self.eye_color)

#Inherits instance variables from parent - we can even inherit the __init__ method from the parent class
class Child(Parent):
    def __init__(self, last_name, eye_color, number_of_toys):
        print("Child's constructor has been called!")
        Parent.__init__(self, last_name, eye_color)
        self.number_of_toys = number_of_toys

    def show_info(self):
        print("Last name: " + self.last_name)
        print("Eye color: " + self.eye_color)
        print("Number of toys: " + str(self.number_of_toys))

