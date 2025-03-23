
from script1 import *

def favorite_drink(drink):
    print(f"Your favorite drink is {drink}")

print("This is script2")
favorite_food("sushi")
favorite_drink("Coffee")
print("Goodbye")


#Sometimes you want to borrow code from other files, however in order to not just run the separate file,
#   you have to check if name is main, or else it will just run the entire other file instead