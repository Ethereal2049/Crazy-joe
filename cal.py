import math

def main():
    
    run_agian = True
    
    while(run_agian == True):
        print("This is a calculater that calculates + - * / \n")

        num1 = float(input("enter first number: "))
        op = input("Enter operater: ")
        num2 = float(input("enter second number: "))
        if (op == "+"):
            print(num1 + num2)
        elif(op == "-"):
            print(num1 - num2)
        elif(op == "*"):
            print(num1 * num2)
        elif(op == "/"):
            print(num1 / num2)
        else:
            print("Enter only + - * / \n")
        answer = input("\n Do you want to do another calculation? \t Enter Yes if you want to do another calculation:\n\n")
        if (answer != "yes" and answer != "Yes"):
            run_agian = False
    print("Bye")

main()


