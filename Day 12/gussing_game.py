import random
from art import logo
def play(tries):
    answer=random.randint(1,100)
    while tries !=0:
        print(f"You have {tries} attempts remaining to guess the number")
        guess=int(input("Guess the number: "))
        if guess>answer:
            print("Too high")
            tries-=1
        elif guess<answer:
            print("Too low")
            tries-=1
        else:
            print(f"You got it! The answer was {answer}.")
            return
    print("You've run out of guesses, you lose.")


print(logo)
print("Welcome to the Number Guessing Game!")
game=input("Press 'y' to Play and 'n' to exit: " ).lower()
while game=='y':
    print("I'm thinking of a number between 1 and 100.")
    difficulty=input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == "easy":
        play(10)
    elif difficulty == "hard":
        play(5)
    else:
        print("Invalid input. Please try again.")
    game=input("Press 'y' to Play and 'n' to exit: " ).lower()


