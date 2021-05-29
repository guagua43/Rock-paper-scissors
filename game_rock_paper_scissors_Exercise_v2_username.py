# game.py
import random

import os

import dotenv

dotenv.load_dotenv()

PLAYER_NAME = os.getenv("PLAYER_NAME")

print("===========================================")
print("Welcome", PLAYER_NAME, "to Rock, Paper, Scissors, Shoot!")
print("===========================================")


user_choice = input("Please choose one of 'rock', 'paper', 'scissors':")

print("USER CHOICE: ", user_choice)

if user_choice in ("rock", "paper", "scissors"):
    print("VALID. KEEP GOING")
else:
    print("OOPS, invalid input. Please try again.")
    exit()


computer_choice = random.choice(["rock","paper","scissors"])
print("COMPUTER CHOICE: ", computer_choice)

if (user_choice == "rock") and (computer_choice == "paper"):
    print("COMPUTER WIN!")

elif (user_choice == "rock") and (computer_choice == "scissors"):
    print("YOU WIN!")

elif (user_choice == "paper") and (computer_choice == "scissors"):
    print("COMPUTER WIN!")

elif (user_choice == "paper") and (computer_choice == "rock"):
    print("YOU WIN!")

elif (user_choice == "scissors") and (computer_choice == "rock"):
    print("COMPUTER WIN!")

elif (user_choice == "scissors") and (computer_choice == "paper"):
    print("YOU WIN!")

elif (user_choice == "scissors") and (computer_choice == "scissors"):
    print("IT'S A TIE!")

elif (user_choice == "paper") and (computer_choice == "paper"):
    print("IT'S A TIE!")

elif user_choice in ("rock") and computer_choice in ("rock"):
    print("IT'S A TIE!")
    
print("Thanks for Playing! Let's try again!")
