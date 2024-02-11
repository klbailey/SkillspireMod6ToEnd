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
      
# The king method in Lion sets all attributes of another big cat to 0.
    def king(self, anotherBigCat):
      otherBigCat.speed = 0
      otherBigCat.strength = 0
      otherBigCat.intelligence = 0
      otherBigCat.health = 0
      otherBigCat.durability = 0

# If the object is a Cheetah then it should have a 60% chance of leaving unscathed. (Hint use a random number generator)


# Create instance and print for BigCat 
# Must have instance if I want to print out the attributes of an instance of BigCat
bigCatInstance = BigCat()
print("Big Cat speed:", bigCatInstance.speed)
print("Big Cat strength:", bigCatInstance.strength)
print("Big Cat intelligence:", bigCatInstance.intelligence)
print("Big Cat health:", bigCatInstance.health)
print("Big Cat durability:", bigCatInstance.durability)

#create instance and print for Lion
lionInstance = Lion()
print("Lion speed:", lionInstance.speed)
print("Lion strength:", lionInstance.strength)
print("Lion intelligence:", lionInstance.intelligence)
print("Lion health:", lionInstance.health)
print("Lion durability:", lionInstance.durability)
