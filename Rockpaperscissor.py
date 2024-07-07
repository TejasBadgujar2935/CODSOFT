import random

print("Welcome to Rock, Paper, Scissors Game!")
player_name =input("enter player name:")

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"

def main():
    user_score = 0
    computer_score = 0
    choices = ['rock', 'paper', 'scissors']
    print("Rules: Rock beats Scissors, Scissors beat Paper, and Paper beats Rock.")

   
    
    while True:
        print("\nPlease choose (type 'quit' to end the game):")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")

        user_choice = input("Enter your choice: ").lower()

        if user_choice == 'quit':
            break
        elif user_choice in ['rock', 'paper', 'scissors']:
            computer_choice = random.choice(choices)
            print(f"\nYou chose: {user_choice}")
            print(f"Computer chose: {computer_choice}")

            result = determine_winner(user_choice, computer_choice)
            print(result)

            if result == "You win!":
                user_score += 1
            elif result == "You lose!":
                computer_score += 1

            print(f"Score - You: {user_score}, Computer: {computer_score}")
        else:
            print("Invalid choice. Please choose 'rock', 'paper', 'scissors', or 'quit'.")
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

    print("Thank you for playing!")

if __name__ == "__main__":
    main()



