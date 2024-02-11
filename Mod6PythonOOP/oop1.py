# Create a car class that has a top speed property 
class MyCar:

# __init__() method we define and set all of the class properties/is constructor
# Self is how a class talks about itself. car says I'm talking about myself / passed as parameter
    
    def __init__(self, topSpeed, make, model, year):
        self.topSpeed = topSpeed
        self.make = make
        self.model = model
        self.year = year
        # Create a location property that starts at 0. 
        self.location = 0

# Create a function that prints out that top speed property.
    def printTopSpeed(self):
        print("Top Speed:", self.topSpeed)

# Create a # drive() function that increases the location variable by 10 miles. 
    def drive(self):
        self.location += 10
    
#Create a stop() function that prints out your final location.
    def stop(self):
        print(f"Final location: {self.location} miles")

# Create instance (object) of MyCar class
shelby = MyCar("180mph", "Shelby", "GT500", 2023)
   
# Call the method and print top speed
shelby.printTopSpeed()

#Call drive
shelby.drive()

# Call stop to print final location
shelby.stop()
