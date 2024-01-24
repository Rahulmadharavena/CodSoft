import random

def determine_winner(user_choice,computer_choice):         
    if user_choice == computer_choice:
        return "It's a tie!"
    elif user_choice =='rock':
        if computer_choice =='paper':
            return "Computer wins!"
        else: 
            return "You win!"
    elif user_choice == 'paper':
        if computer_choice == 'scissors':
            return "Computer wins!"
        else:
            return"You win"
    elif user_choice == 'Scissors':
        if computer_choice =='rock':
            return "Computer wins!"
        else:
            return "You win"
    else:
        return "Invalid input. Please choice"
def play_game():
         game_values = ['rock','paper','scissors']
         user_choice = input("rock,paper or scissors : ")
         computer_choice = random.choice(game_values)
         print("You choose: ", user_choice)  
         print("Computer chose: ", computer_choice )
         print(determine_winner(user_choice,computer_choice))

play_game()        