# Create a Boxer class that has size, strength, wins and losses properties.
# __init__ is constructor method takes 4 parameters and self
class Boxer:
    def __init__(self, size, strength, wins, losses):
        self.size = size
        self.strength = strength
        self.wins = wins
        self.losses = losses

# Create a function that displays the boxer’s stats (Size, Strength, Wins, Losses). 
    def displayStats(self):
        print(f"Boxer Stats:")
        print(f"Size: {self.size}")
        print(f"Strength: {self.strength}")
        print(f"Wins: {self.wins}")
        print(f"Losses: {self.losses}")
    
# Create instance Muhammad Ali and Mike Tyson; \" escape"
ali = Boxer(size="6'3\"", strength=95, wins=56, losses=5)
tyson = Boxer(size="5'10\"", strength=92, wins=50, losses=6)

# Display stats
print("Ali, boxer 1")
ali.displayStats()
print("\n")
print("Tyson, boxer 2")
tyson.displayStats()

# Use the input function to prompt the user to choose which boxer they would like to bet on.
print("Which boxer would you like to bet on? Enter 1 or 2")
x = int(input()) #must be int else will never be true as a string

# If user chooses the boxer that has the best properties in size strength wins and losses 
# then the user wins their bet. Other wise the user loses.
if x == 1:
    print("Winner winner chicken dinner!")
elif x == 2:
    print("You lost. Better luck next time!")
else:
    print("Invalid entry. You must enter 1 or 2.")