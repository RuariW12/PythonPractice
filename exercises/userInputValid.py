# validate user input exercise
# username is no more than 12 characters
# username must not contain spaces
# username must not contain digits

username = input("Enter your username: ")

if len(username) > 12:
    print("Username not valid")
elif not username.isalpha():
    print("Username not valid")
elif username.isdigit():
    print("Username not valid")
else:
    print(f"Your username is:{username}")