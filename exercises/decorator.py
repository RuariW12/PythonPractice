# Decorator = A function that extends the behavior of another function
#           w/o modifying the base function (Adding something to a function without changing it)
#           Pass the base function as an argument to the decorator
#       @add_sprinkles
#       get_ice_cream("vanilla")

def add_sprinkles(func):
    def wrapper():
        print("You add sprinkles")
        func()
    return wrapper # wrapper function makes it so the code is ran only when it is called in get_ice_cream

@add_sprinkles
def get_ice_cream():
    print("Here is your ice cream <o")

get_ice_cream()

