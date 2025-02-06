import random

def get_choices():
    options = ["Rock", "Paper", "Scissors"]  # Define options before using them
    player_choice = input("Enter a choice (Rock, Paper, Scissors): ").capitalize()  # Capitalize for consistency
    computer_choice = random.choice(options)
    
    choices = {"player": player_choice, "computer": computer_choice}
    return choices  

def check_win(player, computer):
    print(f"You chose {player}, computer chose {computer}")  # Fixed f-string syntax
    
    if player == computer:  # Fixed missing closing parenthesis
        return "It's a tie!"
    
    elif player == "Rock":
        if computer == "Scissors":
            return "Rock smashes scissors. You win!"
        else:
            return "Paper covers rock. You lose!"
    
    elif player == "Paper":
        if computer == "Rock":
            return "Paper covers rock. You win!"
        else:
            return "Scissors cut paper. You lose!"
    
    elif player == "Scissors":
        if computer == "Paper":
            return "Scissors cut paper. You win!"
        else:
            return "Rock smashes scissors. You lose!"

# Fix function call issue
choices = get_choices()

# Fix incorrect function call syntax
result = check_win(choices["player"], choices["computer"])
print(result)
