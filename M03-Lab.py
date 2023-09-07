# Defining the Vehicle superclass
class Vehicle:
    def __init__(self):
        self.vehicle_type = ""

# Defining the Automobile class inheriting from Vehicle
class Automobile(Vehicle):
    def __init__(self):
        super().__init__()
        self.year = ""
        self.make = ""
        self.model = ""
        self.doors = ""
        self.roof = ""

# Getting the input based on the year,make,model,number of doors,and type of roof 
    def get_input(self):
        self.vehicle_type = "car"
        self.year = input("Enter the year: ")
        self.make = input("Enter the make: ")
        self.model = input("Enter the model: ")
        self.doors = input("Enter the number of doors (2 or 4): ")
        self.roof = input("Enter the type of roof (solid or sun roof): ")

# Displaying the information 
    def display_info(self):
        print("Vehicle type:", self.vehicle_type)
        print("Year:", self.year)
        print("Make:", self.make)
        print("Model:", self.model)
        print("Number of doors:", self.doors)
        print("Type of roof:", self.roof)

# Creating an instance of the Automobile class
car = Automobile()

# Geting user input for car details
car.get_input()

# Displaying the car information
print("\nCar Information:")
car.display_info()
