# Create a Person class.
# The constructor for the Person class should accept a name and id number as parameters
class Person:
  def __init__(self, name, idNumber):
    self.name = name
    self.idNumber = idNumber

  # Create a function that displays the persons name and Id number
  def displayParams(self):
    print(f"Name: {self.name}")
    print(f"idNumber: {self.idNumber}")

# Create an Employee class that inherits from the Person class
# The constructor for the Employee class should accept a name, id number, salary and post as parameters
class Employee(Person):
  def __init__(self, name, idNumber, salary, post):
    self.salary = salary
    self.post = post
    # Inside the constructor use the super function to invoke the constructor of the parent class
    super().__init__(name, idNumber)

  # Can we override displayParms to include employee object info?
  def displayParams(self):
    super().displayParams()
    print(f"Salary: {self.salary}")
    print(f"Post: {self.post}")
    
# Outside of the Employee class create a new Person object (I'm passing name and idNumber as in class Person)
personObject = Person("Kathy Bailey Hines", 100)

# Outside of Employee class create a new Employee object (passing name idNumber salary post as in Employee class)
employeeObject = Employee("Jane Smith", 101, 70000, "Python Developer")

# Use the display method to print out the information on both employee and person
personObject.displayParams()
employeeObject.displayParams()