# Number Guessing Game
This is simple client-server number guessing game using Python socket programming. The game generates a random number according to the difficulty selected by the player. The server keeps track of every round and has a leaderboard for each difficulty.

## Features
- Player can play as much round as they want until they disconnect.
- Supports three difficulty levels: Easy, Medium, and Hard, with different ranges for the randomly generated number.
- Saves and update leaderboard every round.

## Requirements
- Python 3.x.x


# How to Run?
- Step 1. Clone the repository or download the source code.
- Step 2. Open two of any of the two: terminal or command prompt.
- Step 3. In one window of terminal/command prompt, navigate to the directory with the server script.
- Step 4. Execute the server script by using the command 'python gameserver.py'
- Step 5. In the other window of terminal/cmd, navigate to the client script run it by using the command 'python gameserver.py'
- Step 6. The game is now ready. Enter the difficulty level and guess the mystery number.

# Files
- `gameserver.py`: Contains the server-side code for handling connection with the client
- `gameclient.py`: Contains the client-side code for connecting to the server, sending player information, and making guesses.
- `leaderboard.json`: JSON file used to store and update the leaderboard data.

____________________________________________________________________________________________________________________________________________________________
- NOEL C. PACTANAC JR
