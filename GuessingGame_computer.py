import random

def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != "C":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f"Is {guess} correct? Enter (H) for high, (L) for low, and (C) for correct. ")
        if feedback == "H":
            high = guess - 1

        elif feedback == "L":
            low = guess + 1
                
    print("It was fun playing with you!")
computer_guess(10)