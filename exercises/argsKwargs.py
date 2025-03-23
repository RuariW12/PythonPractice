# *args = allows you to pass multiple non key arguments
# **kwargs = allows you to pass multiple keyword arguments
# * unpacking operator

#ARBITRARY ARGUMENTS

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total


print(add(1, 2, 3))

def display_name(*args):
    for arg in args:
        print(arg, end=" ")

display_name("harold", "funny", "awesome")

def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}:{value}")

print_address(street="123 fake st",
              apt="100",
              city="detroit",
              state="michigan",
              zip="54321"
              )

print()

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    for value in kwargs.values():
        print(value, end=" ")
    print()

shipping_label("Dr.", "Spongebob", "Squarepants", "III",
               street="123 Fake St.",
               apt="100",
               city="Detroit",
               state="MI",
               zip="53241")
