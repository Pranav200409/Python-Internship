import random

def feedback(guess1, number, min_num, max_num):
    range_value = max_num - min_num 
    n1 = guess1 - number
    if abs(n1) > range_value * 0.2:
        if guess1 < number:
            print("Too low.")
        else:
            print("Too high.")
    else:
        print("Low, try again." if guess1 < number else "High, try again.")

def num_guessing(min_num, max_num):
    number = random.randint(min_num, max_num)
    
    while True:
        # Ask for user's guess
        guess1 = int(input(f"Guess the number between {min_num} and {max_num}: "))
        
        if guess1 == number:
            print(f"You guessed the correct number: {number}")
            break
        else:
            feedback(guess1, number, min_num, max_num)

    # Ask user if they want to play again
    choice = input("Do you want to try again? Y to CONTINUE, N to EXIT: ").lower()
    
    if choice != 'y':
        print("Exiting... Thank You!")
    else:
        num_guessing(min_num, max_num)

# Main execution
min_range = int(input("Enter minimum number: "))
max_range = int(input("Enter maximum number: "))
num_guessing(min_range, max_range)
