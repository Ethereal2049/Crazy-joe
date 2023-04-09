
import random


print("**enter the nearest 2 decimal places for divisions**")


def random_num():
    return random.randint(0,100)

def additon(num1,num2):
    answer = num1 + num2
    while True:
        try:
            user = eval(input(f"{num1} + {num2} = "))
            break
        except NameError:
            print("Enter numbers!")
        except SyntaxError:
             print("Enter numbers!")

    if user == answer:
        print("correct!\n")
    else:
        print("incorrect\n")

def subtraction(num1,num2):
    answer = num1 - num2
    while True:
        try:
            user = eval(input(f"{num1} - {num2} = "))
            break
        except NameError:
            print("Enter numbers!")
        except SyntaxError:
            print("Enter numbers!")

    if user == answer:
        print("correct!\n")
    else:
        print("incorrect\n")
    
def multiplication(num1,num2):
    answer = num1 * num2
    while True:
        try:
            user = eval(input(f"{num1} * {num2} = "))
            break
        except NameError:
            print("Enter numbers!")
        except SyntaxError:
             print("Enter numbers!")

    if user == answer:
        print("correct!\n")
    else:
        print("incorrect\n")

def division(num1,num2):
    if num1 < num2 or num2 == 0:
        return

    answer = round(num1/num2,2)
    while True:
        try:
            user = eval(input(f"{num1} / {num2} = "))
            break
        except NameError:
            print("Enter numbers!")
        except SyntaxError:
             print("Enter numbers!")

    if user == answer:
        print("correct!\n")
    else:
        print("incorrect\n")

def main():
    while True:
        while True:
            try:
                try_time = eval(input("How many times you want to play the game?: "))
                break
            except NameError:
                print("Enter numbers!")
            except SyntaxError:
                print("Enter numbers!")

        for k in range(0,try_time,1):
            
            num1 = random_num()
            num2 = random_num()

            signs = ['+','-','*','/']
            sign = random.choice(signs)

            if sign == '+':
                additon(num1,num2)
            elif sign == '-':
                subtraction(num1,num2)
            elif sign == '*':
                multiplication(num1,num2)
            elif sign == '/':
                division(num1,num2)

        print("Thanks for playing! want to play another one?")

        a = input("Enter yes to play or no to quit: ")

        if (a != 'yes' and a != 'Yes'):
            break

    print("Bye!")

main()


        




