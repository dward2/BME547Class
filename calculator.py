# calculator.py

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
else:
   print("The {} command is not recognized.".format(operator))
   exit()

print("{} {} {} = {}".format(a, symbol, b, answer))
