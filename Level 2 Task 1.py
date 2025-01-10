import random

print("\t\t\tNumber Guessing Game.")

def number_guessing ():
    number = random.randint(1,100)
    while True :
        guess = int (input("Enter a number :"))

        if guess == number:
            print("Congrats you guessed correct number")
            break
        elif guess > number :
            print("Too High !!! , Try again")
            break
        elif guess < number :
            print("Too Low !!! , Try again")
            break
        else:
            print("Please enter correct input")
            break

    choice = input("Want to try again ? Yes to CONTINUE , No to EXIT :").strip().lower()
    if choice != 'yes' :
        print("EXITING .... Thank You")
    else :
        number_guessing()
number_guessing()