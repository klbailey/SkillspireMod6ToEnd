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
        # Go to attack method
        self.attack(anotherBigCat)
        anotherBigCat.damageApplied = True
    else:
      # Set all attributes of the Cheetah to 0
      anotherBigCat.speed = 0
      anotherBigCat.strength = 0
      anotherBigCat.intelligence = 0
      anotherBigCat.health = 0
      anotherBigCat.durability = 0

  # If lion's attack is unsuccessful
  def attack(self, anotherBigCat):
    if random.random() <= 0.5:
        anotherBigCat.speed = 0
        anotherBigCat.strength = 0
        anotherBigCat.intelligence = 0
        anotherBigCat.health = 0
        anotherBigCat.durability = 0
    else:
      print('The lion missed.')

# Create a Cheetah class inherits from BigCat class, set the Cheetah's speed to 75, and the rest of its attributes to 25
class Cheetah(BigCat):
  def __init__(self):
    super().__init__()
    self.speed = 75
    self.strength = 25
    self.intelligence = 25
    self.health = 25
    self.durability = 25

    # Flag to see if damage has been applied
    self.damageApplied = False

    # Give the Cheetah a method called run() that accepts a BigCat object.
  def run(self, anotherBigCat):
    # Reset the damageApplied flat at start of each encounter
    self.damageApplied = False
    # If it encounter's a Leopard run the Leopard's pounce method; leopard will pounce and decreases cheetah health by 15
    if isinstance(anotherBigCat, Leopard):
      if random.random() <= 0.6:
        print('The cheetah is unscathed.')
      else:
        anotherBigCat.pounce(self) # refers to current run/attack
      # If it encounters the Lion run the Lion's king() method; anotherBigCat object performs king action which is
      # a method defined in Lion class and does things to another BigCat object like setting attributes to 
      # specific values in this case set to 0
    elif isinstance(anotherBigCat, Lion):
      anotherBigCat.king(self)
      # If it encounters another Cheetah 
    elif isinstance(anotherBigCat, Cheetah):
      if not self.damageApplied:
        damageTaken = 20
        self.health -= damageTaken
        print(f'The cheetah lost {damageTaken} health.')
        self.damageApplied = True
    # If the Cheetah runs away from any of its foes then they lose 20 points in health
    else:
      if not self.damageApplied:
        damageTaken = 20
        self.health -= damageTaken
        print(f'The cheetah lost {damageTaken} health.')
    
# Create a Leopard class that inherits from the BigCat class; set the Leopard's strength intelligence and health to 30
class Leopard(BigCat):
  def __init__(self):
    super().__init__()
    self.strength = 30
    self.intelligence = 30
    self.health = 30

  def pounce(self, anotherBigCat):
    # If object is Lion, run Lion's king() function
    if isinstance(anotherBigCat, Lion):
      anotherBigCat.king(anotherBigCat)
    
      # If object is not Lion but a Cheetah, it should have a 60% chance of leaving unscathed.
    elif isinstance(anotherBigCat, Cheetah):
      if random.random() <= 0.6:
        print('The cheetah is unscathed.')
      else:
        anotherBigCat.health -= 15
    else:
      # If object is not lion, deplete health by 15 points
      anotherBigCat.health -= 15
    
# Create instances / interactions for BigCat, Lion, Cheetah, Leopard
# Must have instance if I want to print out the attributes of an instance of BigCat
bigCatInstance = BigCat()
lionInstance = Lion()
cheetahInstance = Cheetah()
leopardInstance = Leopard()

# Create a game where ALL objects get created and All their methods are used 
''' Objects:
bigCatInstance = BigCat()
lionInstance = Lion()
cheetahInstance = Cheetah()
leopardInstance = Leopard()
    Methods:
__init__
king
run
pounce
'''

# One random encounter between 2 cats
# random choice will randomly select one item from a given list [lion, cheetah, or leopard]
catOne = random.choice([lionInstance, cheetahInstance, leopardInstance])
remaining_cats = [cat for cat in [lionInstance, cheetahInstance, leopardInstance] if cat != catOne]
catTwo = random.choice(remaining_cats)

# Print the initial state
print("Initial state:")
print("Cat One:", catOne.__class__.__name__, "Health:", catOne.health)
print("Cat Two:", catTwo.__class__.__name__, "Health:", catTwo.health)

# Are the two cats different? If not, keeps randomly choosing until they different
while catOne is catTwo:
  catTwo = random.choice([lionInstance, cheetahInstance, leopardInstance])



# Simulate an encounter
if isinstance(catOne, Cheetah):
    catOne.run(catTwo)
# If it's a Leopard, run the Leopard's pounce method
elif isinstance(catOne, Leopard):
    catOne.pounce(catTwo)
# If it's a Lion, run the Lion's king() method
elif isinstance(catOne, Lion):
    catOne.king(catTwo)

# Print updated health attributes after interactions
print("Lion:", lionInstance.health)
print("Cheetah:", cheetahInstance.health)
print("Leopard:", leopardInstance.health)

# Who is the winner with the highest health attribute
allCats = [lionInstance, cheetahInstance, leopardInstance]
# Initialize variables
maxHealth = 0
winner = None
for cat in allCats:
  # Chec health after encounter
  currentHealth = cat.health
  # Only consider non-cheetah cats for he winner
  if not (isinstance(cat, Cheetah) and cat.damageApplied) and currentHealth > maxHealth:
    maxHealth = currentHealth
    winner = cat

# Get type of winner (Lion, or Leopard) of the winner
# Empty string to assign to winnerType
winnerType = "Unknown"
if isinstance(winner, Lion):
  winnerType = "Lion"
elif isinstance(winner, Leopard):
  winnerType = "Leopard"

print("The winner is a", winnerType)