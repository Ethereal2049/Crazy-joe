
import random


ke = True


print("**enter only nearest integer without the decimal for divisions**")

while ke == True:
    num1 = random.randint(0,100)

    num2 = random.randint(0,100)

    signs = ['+','-','*','//']
    sign = random.choice(signs)

    if sign == '+':
        answer = num1 + num2
        user = eval(input(f"{num1} + {num2} = "))
        if user == answer:
            print("correct!\n")
        else:
            print("incorrect\n")

    if sign == '-':
        answer = num1 - num2
        user = eval(input(f"{num1} - {num2} = "))
        if user == answer:
            print("correct!\n")
        else:
            print("incorrect\n")

    if sign == '*':
        answer = num1 * num2
        user = eval(input(f"{num1} * {num2} = "))
        if user == answer:
            print("correct!\n")
        else:
            print("incorrect\n")

    if sign == '//':
        if num1 < num2 or num2 == 0:
            continue
        answer = num1 // num2
        user = eval(input(f"{num1} // {num2} = "))
        if user == answer:
            print("correct!\n")
        else:
            print("incorrect\n")



