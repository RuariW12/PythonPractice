# Rock Paper Scissors Game (SOLO MADE)

import random

options = ("rock", "paper", "scissors")
playing = True
player_score = 0
computer_score = 0

print("Welcome to Rock Paper Scissors!")

while playing:

    guess = input("Please throw rock, paper, or scissors: ")
    computer_pick = random.choice(options)


    if guess == "rock":
        if computer_pick == "rock":
            print(f"Tie! You both picked {guess}")
        elif computer_pick == "paper":
            print(f"You lose! Computer picked {computer_pick}")
            computer_score += 1
        elif computer_pick == "scissors":
            print(f"You win! Computer picked {computer_pick}")
            player_score += 1
        print("-----SCORE-----")
        print(f"You:{player_score}, Computer:{computer_score}")

    if guess == "paper":
        if computer_pick == "paper":
            print(f"Tie! You both picked {guess}")
        elif computer_pick == "scissors":
            print(f"You lose! Computer picked {computer_pick}")
            computer_score += 1
        elif computer_pick == "rock":
            print(f"You win! Computer picked {computer_pick}")
            player_score += 1
        print("-----SCORE-----")
        print(f"You:{player_score}, Computer:{computer_score}")

    if guess == "scissors":
        if computer_pick == "scissors":
            print(f"Tie! You both picked {guess}")
        elif computer_pick == "rock":
            print(f"You lose! Computer picked {computer_pick}")
            computer_score += 1
        elif computer_pick == "paper":
            print(f"You win! Computer picked {computer_pick}")
            player_score += 1
        print("-----SCORE-----")
        print(f"You:{player_score}, Computer:{computer_score}")

    play_again = input("Would you like to play again? (Y/N): ")

    if play_again == "N":
        print("-----------------------")
        print("Thanks for playing!")
        print(f"The score was {player_score} to {computer_score}")
        print("-----------------------")
        break










