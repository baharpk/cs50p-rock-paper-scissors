# Rock_Paper_Scissors Game

#### Video Demo: https://youtu.be/e4MKmhcpQ10?si=ImzAvdLe9mvxfTNn

#### Description:

This project is a simple version of the classic **Rock_Paper_Scissors** game,created as my final project.The program allows users to play multiple rounds against the computer,the game saves the scores,and decides who wins each round based on the rules.

The game starts by welcoming the user and explaining that they may type **"exit"** or **"over"** at any time to end the game .

Inside the main loop the user is asket to enter thair choice **rock**, **paper** or **scossors**.Empty inputs or invalid values trigger clear error messages and the player will be asked agian.

The computer's choice is generated randomly using the `numpy.random.choice()` function. Both choices are shown with emojies to make the game more atractive and clear.

Each round's outcome is determined by the `determine_winner()`function, which compares the player's selection with the computer's selection.The rules are implemented in a dictionary structure:
- rock beats scissors
- scissors bests paper
- paper beats rock

Scores will be updated after each round, including:
- **player_score**
- **computer_score**
- **draws**

At the end of the game , the code prints a summary of the final scores and announce the final winner (player, computer or a draw).

### Main Components:
- `main()` _ game loop, score tracking, input handling
- `player_choice()` _ validate and return the player's choice
- `computer_choice()` _ generates a random choice for the computer
- `determine_winner()` _ compares choices and return the round result

### Features:
- Input validation with error handling
- Multiple_round gameplay
- Random computer choices
- Score tracking (wins, losses, draws)
- Emoji_based dasplay
- Clear end-of-game summary

This project shows basic Python skills such as loops, conditions, functions, error checking, and user input.It is simple but complete and works as a small interactive game.
