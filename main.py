import art
import random

x = int(random.randint(1,100))
a = 0

def check_answer(counter, user_input, correct_answer):
    if user_input > correct_answer and counter > 1:
        print("Too High")
        print("Guess Again")
        return True
    elif user_input > correct_answer and counter == 1:
        print("Too High")
        print("Sorry, you've run out of guesses, you lose.")
        return False
    elif user_input < correct_answer and counter > 1:
        print("Too Low")
        print("Guess Again")
        return True
    elif user_input < correct_answer and counter == 1:
        print("Too Low")
        print("Sorry, you've run out of guesses, you lose.")
        return False
    else:
        print(f"You got it! The answer was {correct_answer}")
        return False



print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
print(f"Psst, the correct answer is {x}")
y = input("Choose a difficulty. Type 'easy' or 'hard': ")
if y == 'hard':
    a = 5
elif y == 'easy':
    a = 10

play_game = True
while play_game:
    print(f"You have {a} attempts remaining to guess the number. ")
    user_guess = int(input("Make a guess "))
    aa = check_answer(a, user_guess, x)
    if not aa:
        play_game = False
    a -= 1