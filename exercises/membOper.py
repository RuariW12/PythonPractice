# Membership operators = used to test whether a value or variable is found in a sequence
#       (string, list, tuple, set or dictionary)
#       1. in
#       2. not in

#word = "APPLE"

#letter = input("Guess a letter in the secret word: ")

#if letter in word:
#   print(f"There is a {letter}")
#else:
#    print(f"{letter} was not found")


#students = {"Jerry", "Sandy", "Joe"}

#student = input("Enter the name of a student: ")

#if student in students:
#    print(f"{student} is a student")
#else:
#    print(f"{student} is not a student")


#grades = {"Jerry": "A",
#          "Sandy": "B",
#          "Joe": 'D',
#          "Christian": "C-"
#          }

#student = input("Enter the name of a student: ")

#if student in grades:
#    print(f"{student}'s grade is {grades[student]}")
#else:
#    print(f"{student} was not found")

email = "ruariwh@gmail.com"

if "@" in email and "." in email:
    print("Email is valid")
else:
    print("invalid email")