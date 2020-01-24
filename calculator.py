# calculator.py

import math

def add(x, y):
    z = x + y
    return z


def subtract(x, y):
    z = x - y
    return z
    

def multiply(x, y):
    z = x * y
    return z


def divide(x, y):
    z = x / y
    return z
    
def square_root(x):
    z = math.sqrt(x)
    return z
    

if __name__ == "__main__":
    operator = input("Enter a letter: ")
    print("You entered {}".format(operator))
    a = input("Enter the first number: ")
    b = input("Enter the second number: ")
    if operator == "a":
       answer = add(int(a), int(b))
       symbol = '+'
    elif operator == "s":
       answer = subtract(int(a), int(b))
       symbol = '-'
    elif operator == "m":
       answer = multiply(int(a), int(b))
       symbol = 'x'
    elif operator == "d":
       answer = divide(int(a), int(b))
       symbol = '/'
    elif operator == "r":
       answer = square_root(int(a))
       symbol = 'root'
    else:
       print("The {} command is not recognized.".format(operator))
       exit()

    print(math.sqrt(25))
    print("{} {} {} = {}".format(a, symbol, b, answer))
