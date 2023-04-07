
import random


print("**enter only nearest integer without the decimal for divisions**")


def random_num():
    return random.randint(0,100)

def additon(num1,num2):
    answer = num1 + num2
    user = eval(input(f"{num1} + {num2} = "))
    if user == answer:
        print("correct!\n")
    else:
        print("incorrect\n")

def subtraction(num1,num2):
    answer = num1 - num2
    user = eval(input(f"{num1} - {num2} = "))
    if user == answer:
        print("correct!\n")
    else:
        print("incorrect\n")
    
def multiplication(num1,num2):
    answer = num1 * num2
    user = eval(input(f"{num1} * {num2} = "))
    if user == answer:
        print("correct!\n")
    else:
        print("incorrect\n")

def division(num1,num2):
    if num1 < num2 or num2 == 0:
        return
    answer = num1 // num2
    user = eval(input(f"{num1} // {num2} = "))
    if user == answer:
        print("correct!\n")
    else:
        print("incorrect\n")

def main():
    ke = True
    
    while ke == True:

        num1 = random_num()
        num2 = random_num()

        signs = ['+','-','*','//']
        sign = random.choice(signs)

        if sign == '+':
            additon(num1,num2)
        elif sign == '-':
            subtraction(num1,num2)
        elif sign == '*':
            multiplication(num1,num2)
        elif sign == '//':
            division(num1,num2)
main()


        




