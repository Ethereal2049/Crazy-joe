import random

def main():
    print("This is a number guessing game \n")
    answer = random.randint(1,100)
    guesses = 0
    
    do_agian = True

    while do_agian == True:
        
        
        while True:
            
            guess = int(input("Now chooes a number between 1 to 100 :"))
            guesses += 1
            if (answer == guess):
                print(" Correct ! you guessed", guesses,"times to get the number.")
                break
            elif(answer > guess):
                print(" Bigger! ")
            elif(answer < guess):
                print(" Smaller!")
        respon = input("do you want to do another one?\t Type Yes to comfirm or any other words to exit: ")
        if(respon != "Yes" and respon != "yes"):
            do_agian = False
    print("Bye")


            
main()
