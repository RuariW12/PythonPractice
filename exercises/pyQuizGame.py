# Python quiz game

questions = ("How many elements are in the periodic table?: ",
             "Which animal lays the largest eggs?: ",
             "What is the most abundant gas in the Earth's atmosphere?: ",
             "How many bones are in the human body?: ",
             "Which planet in the solar system is the hottest?: ")

options = (("A. 116","B. 117","C. 118","D. 119"),
           ("A. Whale","B. Crocodile","C. Elephant","D. Ostrich"),
           ("A. Nitrogen","B. Oxygen","C. Carbon-Dioxide","D. Hydrogen"),
           ("A. 206","B. 207","C. 208","D. 209"),
           ("A. Mercury","B. Venus","C. Earth","D. Mars"))

answers = ("C", "D", "A", "A", 'B')
guesses = []
score = 0
question_num = 0

for question in questions: #delcares "question" as elements in question tuple
    print("-------------------")
    print(question)
    for option in options[question_num]: #when the loop is run, "option" is declared as tuples inside 2d tuple option.
        print(option) # will print the first option, and since question_num += 1, it will go to the next.

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

print("--------------------")
print("-------RESULTS------")
print("--------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")



#question num acts as index finding number. since declared first as 0, options[0], will first display the
#   first list, then when the loop is run and completes one cycle, += 1 is added thus corresponding to the
#   list number. The loop is then over once every list is displayed.

