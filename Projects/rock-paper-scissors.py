import random
def get_choices():
  options = ["rock", "paper", "scissors"]
  player_choice = input("Enter rock, paper, or scissors: ")
  computer_choice = random.choice(options)
  choices = {"player": player_choice, "computer": computer_choice}
  return choices

def check_win(player, computer):
  print(f"You chose {player}, computer chose {computer}")
  if player == computer:
    print("It's a tie!")
  elif player == "rock":
    if computer == "scissors":
      print("You win!")
    else:
      print("Computer wins!")
  elif player == "paper":
    if computer == "rock":
      print("You win!")
    else:
      print("Computer wins!")
  elif player == "scissors":
    if computer == "paper":
      print("You win!")
    else:
      print("Computer wins!")

choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)