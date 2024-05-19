# Modified Calculator:
logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

from rich.console import Console

print(logo)

def add(n1, n2):
    return n1 + n2

def minus(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def remainder(n1, n2):
    return n1 % n2

def power(n1, n2):
    return pow(n1, n2)

num1 = float(input("What is the first number: "))

operation = {
    "+": add,
    "-": minus,
    "*": multiply,
    "/": divide,
    "%": remainder,
    "^": power
}

while True:
    for key in operation:
        print(key)
    
    pick = input("Pick the operation: ")
    
    num2 = float(input("What is the next number: "))
    
    arihtmetic_func = operation[pick]
    result = arihtmetic_func(num1, num2)
    
    print(f"{num1} {pick} {num2} = {result}")
    
    y_n = input(f"Type 'y' to continue with {result} or type 'n' to start new calculation.").lower()
    
    if (y_n == 'y'):
        num1 = result
    
    else:
        console = Console()
        console.clear()
        print(logo)
        
        num1 = float(input("What is the first number: "))