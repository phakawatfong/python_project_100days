MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}

def is_resource_sufficient(user_order):
  """Returns True when order can be made, False if ingredients are insufficient."""
  for item in user_order:
    if user_order[item] > resources[item]:
        print(f" Sorry there is not enough {item}.")
        return False
  return True

def process_coin():
  print("Please insert coin")
  quarter = int(input("How many quarter? ")) # quater = 25c
  dime = int(input("How many dime? ")) # dime = 10c
  nickel = int(input("How many nickel? ")) # nickel = 5c
  penny = int(input("How many penny? ")) # penny = 1c
  total = (quarter*0.25)+(dime*0.1)+(nickel*0.05)+(penny*0.01)
  return total
# print(process_coin())

def make_coffee(drink_name, user_order):
  for item in user_order:
    resources[item] -= user_order[item]
  print(f"Here is your coffee {drink_name}☕")


profit = 0
def is_transaction_successful(payment, drink_cost):
  if payment > drink_cost:
    change = round(payment - drink_cost,2)
    print(f'Here is your change {change}$')
    global profit
    profit += drink_cost
    return True
  else:
    print(f'Not enough money: Money refunded')
    return False


    
machine_on = True
while machine_on:
  user_input = input("What would you like? (espresso/latte/cappuccino): ")
  if user_input == "off":
    machine_on = False
  elif user_input == "report":
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: {profit}")
    # print(f"Money: ${profit}")
  else:
    drink = MENU[user_input]
    # print(type(drink))
    # print(drink)
    if is_resource_sufficient(drink['ingredients']):
      payment = process_coin()
      if is_transaction_successful(payment, drink['cost']):
        make_coffee(user_input, drink['ingredients'])
        
      
    

  
  
  
