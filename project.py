import numpy

def main():
    """runs the main game loop and keeps track of scores"""
    player_score=0
    computer_score=0
    draws=0

    print("Welcome to the game Rock_Paper_Scissors")
    print("type 'exit' or 'over' when you want to end the game")

    while True:
        # get user's input and clean whitespace and lowercase it
        choice=input("Enter your choice amoung (Rock/Paper/Scissors):").strip().lower()
        # allow user to quit the game
        if choice in ["exit" , "over"]:
            break
        # prevent empty input
        if choice == "":
            print("You should enter somthing")
            continue
        # convert input into a valid move
        try:
            player = player_choice(choice)
        except ValueError:
            print("Invalid input.")
            continue
        # computer choices one option randomly
        computer = computer_choice()

        # emojies to make the game more fun
        emoji = {"rock":"✊",
                 "paper":"✋",
                 "scissors":"✌"
                 }
        print(f"Your choice :{emoji[player]}\nComputer's choice:{emoji[computer]}")
        # determine who wins this round
        result= determine_winner(player,computer)

        if result == "player":
            print ("you won this round!")
            player_score += 1
        elif result == "computer":
            print("computer won this round!")
            computer_score += 1
        else:
            print("This round is a draw!")
            draws += 1
    # final results after the user quit the game
    print("\nTHE FINAL SCORES")
    print(f"\nYour score:{player_score}\nComputer'score:{computer_score}\nDraws:{draws}")

    # final messages
    if player_score > computer_score:
        print("\nThe Final Winner Is You 🎉")
    elif player_score > computer_score:
        print("\nThe Final Winner Is Computer 😟")
    else:
        print("\nIT's a Draw 🤝")


def player_choice(choice):
    """ checks the user's input and return the valid option"""

    if choice == "rock":
        return "rock"
    elif choice == "paper":
        return "paper"
    elif choice == "scissors":
        return "scissors"
    else:
        raise ValueError("Invalid input you must enter 'Rock','Paper' or 'Scissors'.")

def computer_choice():
    """returns rock, paper, scissors randomly"""

    return numpy.random.choice(["rock","paper","scissors"])

def determine_winner(player, computer):
    """desides who wins the round : player, computer, draw"""

    if player == computer:
        return "draw"

    rules = {
        "rock":"scissors",
        "scissors":"paper",
        "paper":"rock"
    }

    if rules[player] == computer:
        return "player"
    else:
        return "computer"

if __name__ == "__main__":
    main()
