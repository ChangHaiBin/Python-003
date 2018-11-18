import random

location = 10
print(f"Your character is {location} meters away.")
input("Press ENTER to roll a dice.")




x = random.randint(1,6)
print(f"You rolled a dice, and the number is {x}")
input("Press ENTER to continue.")




newLocation = location + x
print(f"After moving {x} meters, your new character is now {newLocation} meters away.")






input("Press Enter to continue:")

