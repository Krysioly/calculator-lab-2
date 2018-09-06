"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here
# No setup
# repeat forever:
#     read input
#     tokenize input
#     if the first token is "q":
#         quit
#     else:
#         decide which math function to call based on first token

def calculator():
    print("""Use spaces between answer
            If adding use + (provide 2 numbers)
            If subtracting use - (provide 2 numbers)
            if mulitplication use * (provide 2 numbers)
            if dividing use / (provide 2 numbers)
            if squaring use square (provide 1 number)
            if cubing use cube (provide 1 number)
            if looking for remainder use mod (provide 2 numbers)
            if power use pow (provide 2 numbers 
            if you want to quit press Q""")
    while True:

        user_input = input("What math function do you want? What are the numbers?: ")
        user_words = user_input.split(" ")
        if user_words[0] == "q":
            break
        else:
            cal = user_words[0]
            if cal == "cube" or cal == "square":
                num1 =  int(user_words[1])
                if cal == "square":
                    print(square(num1))
                elif cal == "cube":
                    print(cube(num1))
            else:
                num1 =  int(user_words[1])
                num2 = int(user_words[2])
                if cal == "+" :
                    print(add(num1, num2))
                elif cal == "-":
                    print(subtract(num1, num2))
                elif cal == "*":
                    print(multiply(num1, num2))
                elif cal == "/":
                    print(divide(num1, num2))
                elif cal == "pow": 
                    print(power(num1, num2))
                elif cal == "mod":
                    print(mod(num1, num2))
calculator()
