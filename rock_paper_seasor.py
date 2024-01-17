import random

def get_userchoice():
    userchoice = input("Choose rock, paper, or scissors: ").lower()
    while userchoice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        userchoice = input("Choose rock, paper, or scissors: ").lower()
    return userchoice

def get_computerchoice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'It\'s a tie!'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return 'You win!'
    else:
        return 'You lose!'

def display_result(userchoice, computerchoice, result):
    print(f"\nYour choice: {userchoice.capitalize()}")
    print(f"Computer's choice: {computerchoice.capitalize()}")
    print(f"Result: {result}")

def play_game():
    user_score = 0
    computer_score = 0

    while True:
        userchoice = get_userchoice()
        computerchoice = get_computerchoice()

        result = determine_winner(userchoice, computerchoice)
        display_result(userchoice, computerchoice, result)

        if result == 'You win!':
            user_score += 1
        elif result == 'You lose!':
            computer_score += 1

        print(f"\nScore - You: {user_score}, Computer: {computer_score}")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing. Goodbye!")
            break

if __name__ == "__main__":
    print("Welcome to Rock, Paper, Scissors Game!")
    play_game()
