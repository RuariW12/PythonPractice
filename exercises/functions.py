# function = a block of reusable code
#       place () after the function name to invoke it

#def birthday_song(name, age):
    #print(f"Happy birthday to {name}!")
    #print(f"Happy birthday you are {age}!")
    #print("Happy birthday dear me!")
    #print("Happy birthday to you!")
    #print()

#birthday_song("Bro", 20)
#birthday_song("Friend", 30)
#birthday_song("Steve", 40)

#def calls the function
# birthday_song() - inside of parenthesis is the parameter. Inside the parameter, are arguments.

def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of ${amount:.2f} is due: {due_date}")

display_invoice("Ruari", 42.50, "01/01")



