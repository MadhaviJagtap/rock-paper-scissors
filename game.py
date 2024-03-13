import random as rd
import art as a

def get_user_choice():
    """Get user choice from input."""
    return int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))

def display_choices(choice_art, choice_name):
    """Display the choice made by the user or the computer."""
    print(f"\nYou chose {choice_name}!")
    print(choice_art)

def main():
    """Main function to run the Rock-Paper-Scissors game."""
    print(a.logo)

    user = get_user_choice()
    comp = rd.randint(0, 2)

    choices = [a.rock, a.paper, a.scissors]
    choice_names = ["Rock", "Paper", "Scissors"]

    if user not in [0, 1, 2]:
        print("You haven't entered a valid input. Thanks for playing!")
        return

    display_choices(choices[user], choice_names[user])

    print("Computer chose:")
    display_choices(choices[comp], choice_names[comp])

    # rock 0
    # paper 1
    # scissors 2

    if user == comp:
        print("It's a tie!")
    elif user == 0 and comp == 2 or user == 2 and comp == 1 or user == 1 and comp == 0:
        print("You win!")
    else:
        print("You lose!")

if __name__ == "__main__":
    main()
