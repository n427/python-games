import random
user = input("Pick one; 'r' for rock, 's' for scissors, or 'p' for paper: ")
computer = random.choice(["r", "p", "s"])

if user == computer:
    print("Tie game")

elif user == "r" and computer == "s":
    print("You win! The computer picked scissors")

elif user == "r" and computer == "p":
    print("You lose! The computer picked paper")

elif user == "p" and computer == "s":
    print("You lose! The computer picked scissors")

elif user == "p" and computer == "r":
    print("You win! The computer picked rock")

elif user == "s" and computer == "r":
    print("You lose! The computer picked rock")
    
elif user == "s" and computer == "p":
    print("You win! The computer picked paper")