import os
from art import logo
print(logo)
def calculation(a,b,c):
    if b == '+':
        return a + c
    elif b == '-':
        return a - c
    elif b == '*':
        return a * c
    elif b == '/':
        return a / c
    else:
        return "Invalid operator"
while(True):
    number_1=float(input("What's the first number?: "))
    operator=input("+\n-\n*\n/\nPick an operation: ")
    number_2=float(input("What's the second number?: "))
    answer=calculation(number_1,operator,number_2)


    print(f"{number_1} {operator} {number_2} = {answer}")
    flag=True
    while(flag):
        ans=input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ").lower()
        if ans == 'y':
            number_1=answer
            operator=input("+\n-\n*\n/\nPick an operation: ")
            number_2=float(input("What's the second number?: "))
            answer=calculation(number_1,operator,number_2)
            print(f"{number_1} {operator} {number_2} = {answer}")
        else:
            flag=False
    os.system('cls')
    