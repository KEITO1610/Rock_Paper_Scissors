import random

player_choice = input("Enter a choice(rock, paper, scissors):")
options = ["rock", "paper", "scissors"]
computer_choice = random.choice(options)
choices = {"player":player_choice, "computer":computer_choice}

def check_win(player, computer):
    print("You chose "+ player+", computer chose "+ computer +".")
    if player == computer:          
        return "it's a tie!"
    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes scissors! You win!"
        else:
            return "Paper covers rock! You lose."
    elif player == "paper":
        if computer == "rock":
            return "Paper covers rock! You win!"
        else:
            return "Scissors cuts paper! You lose."
    elif player == "scissors":
        if computer == "rock":
            return "Rocks smashes scissors! You lose."
        else:
            return "Scissors cuts paper! You win!"
        

result = check_win(player_choice, computer_choice)
print(result)        

        