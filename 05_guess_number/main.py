#Number Guessing Game 

# Include an ASCII art logo.
import random
from art import logo
print(logo)

EASY_TURNS = 10
HARD_TURNS = 5


def check_high_low(guess, answer, turns):
  if guess > answer:
    print("too high")
    return turns - 1
  elif guess < answer:
    print("too low")
    return turns - 1
  elif guess == answer:
    print(f"you got the right answer!  it is {answer}")


def set_difficulty():
  diff = input("Choose 'easy' or 'hard' ")
  if diff == "easy":
    return EASY_TURNS
  elif diff == "hard":
    return HARD_TURNS

def play_game():

  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  answer = random.randint(1,100)
  turns = set_difficulty()
  guess = 0 # set guess = 0 to get into while loop

  while guess != answer:
    print(f"you have {turns} attempts remaining to guess the number.")
    guess = int(input("Guess a number from 1-100: "))
    turns = check_high_low(guess, answer, turns)
    
    if turns == 0:
      print(f"You ran out of attemps the answer is {answer}")
      break
    elif guess != answer:
      print('guess again\n')
     
play_game()



    
    
