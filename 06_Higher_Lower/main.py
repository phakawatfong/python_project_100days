from art import logo
from game_data import data
import random
import os


def clear_console():
    os.system('clear')

# random.seed(99) ## set seed to check first -- to be delete later
# rand_list = []
# for i in range(2):
#   answer = random.choice(data)
#   # print(f"{answer}\n")
#   rand_list.append(answer)

# create function to random for our DATA
def get_random_account():
  rand_choice = random.choice(data)
  return rand_choice
  
# create function just to display description
def format_data(account):
  name = account["name"]
  follower_count = account["follower_count"]
  description = account["description"]
  country = account["country"]
  # print(f"follower numbers {follower_count}")
  # print(f"[{name}], a {description} from {country}.")
  return f"[{name}], a {description} from {country}."

# account_1 = get_random_account()
# format_data(account_1)

# account_2 = get_random_account()
# format_data(account_2)

# guess = input("Which person has more follower on 'Instragram' A or B ? ")
def check_answer(account_1, account_2):
  a_follower = account_1["follower_count"]
  b_follower = account_2["follower_count"]
  print(a_follower)
  print(b_follower)
  if a_follower > b_follower:
    return "a"
  elif a_follower < b_follower:
    return "b"
# check_answer(guess, account_1, account_2)
    
# guess = input("Which person has more follower on 'Instragram' A or B ? ")
# check_answer(guess, account_1[follower_count], account_2[follower_count])

# for i in range(len(name_list)):
#   guess_dict[name_list[i]]=value_list[i]

# print(guess_dict)

# def game(guess, account_a, account_b):
#   guess = input("Which person has more follower on 'Instragram' A or B ? ")
#   account_a = get_random_account()
#   account_b = get_random_account()



# merge our code
def game_play():
  print(logo)
  score = 0
  game_on = True
  account_a = get_random_account()
  account_b = get_random_account()
  
  
  while game_on:
    account_a = account_b
    account_b = get_random_account()

    while account_a == account_b:
      account_b = get_random_account()
      
    print(f"Compare A: {format_data(account_a)}")
    print("vs")
    print(f"Against B: {format_data(account_b)}")
    print('\n')
      
    guess = input("Which person has more follower on 'Instragram' A or B ? ")
    ans = check_answer(account_a, account_b)


    clear_console()
    if guess.lower() == ans:
      score += 1
      # print(f"guess: {guess}")
      # print(f"answer {ans}")
      print(f"correct! your score is {score}\n")
    else:
      game_on = False
      print(f"wrong! your final score is {score}")

game_play()
        

