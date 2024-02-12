import random

# Set all attributes to 5 / needs 'self' to reference variables
class BigCat:
  def __init__(self):
    self.speed = 5
    self.strength = 5
    self.intelligence = 5
    self.health = 5
    self.durability = 5
  
# Create Lion class that inherits from BigCat and set strength and health to 50
class Lion(BigCat):
  def __init__(self):
    super().__init__()
    self.strength = 50
    self.health = 50
      
# The king method in Lion  that acceepts BigCat params & sets all attributes of another big cat to 0
  def king(self, anotherBigCat):
    # If the object is a Cheetah then it should have a 60% chance of leaving unscathed. (Hint use a random number generator)
     if isinstance(anotherBigCat, Cheetah):
      #random.random() returns floating numbers between 0 and 1
      if random.random() <= .60:
        print('The cheetah was unscathed.')
      else:
        anotherBigCat.speed = 0
        anotherBigCat.strength = 0
        anotherBigCat.intelligence = 0
        anotherBigCat.health = 0
        anotherBigCat.durability = 0

# Create a Cheetah class inherits from BigCat class, set the Cheetah's speed to 75, and the rest of its attributes to 25
class Cheetah(BigCat):
  def __init__(self):
    super().__init__()
    self.speed = 75
    self.strength =25
    self.intelligence = 25
    self.health = 25
    self.durability =25

    # Give the Cheetah a method called run() that accepts a BigCat object.
  def run(self, anotherBigCat):
    # If it encounter's a Leopard run the Leopard's attack method
    if isinstance(anotherBigCat, Leopard):
      anotherBigCat.pounce()
      # If it encounters the Lion run the Lion's king() method; anotherBigCat object performs king action which is
      # a method defined in Lion class and does things to another BigCat object like setting attributes to 
      # specific values
    if isinstance(anotherBigCat, Lion):
      anotherBigCat.king(anotherBigCat)
    
# Create a Leopard class that inherits from the BigCat class; set the Leopard's strength intelligence and health to 30
class Leopard(BigCat):
  def __init__(self):
    super().__init__()
    self.strength = 30
    self.intelligence = 30
    self.health = 30

  # Give Leopard a method king() that accepts BigCat object and sets attributes to 0
  def king(self, anotherBigCat):
    anotherBigCat.speed = 0
    anotherBigCat.strength = 0
    anotherBigCat.intelligence = 0
    anotherBigCat.health = 0
    anotherBigCat.durability = 0

    def pounce(self, anotherBigCat):
      # If object is Lion, run Lion's king() function
      if isintance(anotherBigCat, Lion):
        anotherBigCat.king(anotherBigCat)
      else:
        # If object is not lion, depete health by 15 points
        anotherBigCat.health =+ 15
    
# Create instance / interactions for BigCat 
# Must have instance if I want to print out the attributes of an instance of BigCat
bigCatInstance = BigCat()
print("Big Cat speed:", bigCatInstance.speed)
print("Big Cat strength:", bigCatInstance.strength)
print("Big Cat intelligence:", bigCatInstance.intelligence)
print("Big Cat health:", bigCatInstance.health)
print("Big Cat durability:", bigCatInstance.durability)

# Create instance / interactions for Lion
lionInstance = Lion()
print("Lion speed:", lionInstance.speed)
print("Lion strength:", lionInstance.strength)
print("Lion intelligence:", lionInstance.intelligence)
print("Lion health:", lionInstance.health)
print("Lion durability:", lionInstance.durability) 

# Create instance / interactions for Cheetah
cheetahInstance = Cheetah()

# Create instance / interactions for Leopard
leopardInstance = Leopard()
