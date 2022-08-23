# Calculator

# Add
def add(num1, num2):
  return num1 + num2

# Subtract
def subtract(num1, num2):
  return num1 - num2

# Multiply
def multiply(num1, num2):
  return num1 * num2
  
# Divide
def divide(num1, num2):
  return num1 / num2

# dict
  # keys = + - * / 
  # val = name of function
operators = {"+" : add,
            "-": subtract,
            "*": multiply,
            "/": divide}

def calculator():
  num1 = float(input("What's the first number?: "))
  close_cal = False   
  for symbol in operators:
    print(symbol)
    
  while not close_cal:
    operator_symbol = input("Pick an operator from the line above: ")
    num2 = float(input("What's the second number?: "))
        # operator_symbol = input("Pick an operator: ")
    calculation_function = operators[operator_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operator_symbol} {num2} = {answer}")

    play_again = input(f"Do you want to continue the calculation with {answer}? press 'yes' or 'no' and 'o' to start a new calculation ")
    if play_again[0].lower() == 'y':
      num1 = answer
    elif play_again[0].lower() == 'o':
      close_cal = True
      calculator()
    else:
      close_cal = True

calculator()
