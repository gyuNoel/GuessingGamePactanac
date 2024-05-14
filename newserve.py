import socket
import random
import json

# FINAL
last_difficulty = 'a'# DEFAULT VALUE FOR EASY MODEs
host = ""
port = 7777
banner = """
== Guessing Game v1.0 ==
Choose difficulty level:
a - Easy (1-50)
b - Medium (1-100)
c - Hard (1-500)
"""

def generate_random_int(difficulty):
    if difficulty == 'a':
        return random.randint(1, 50)
    elif difficulty == 'b':
        return random.randint(1, 100)
    elif difficulty == 'c':
        return random.randint(1, 500)

def update_leaderboard(name, score, difficulty, leaderboard):
    leaderboard.append({"name": name, "score": score, "difficulty": difficulty})
    leaderboard.sort(key=lambda x: x["score"])
    return leaderboard[:10]

def save_leaderboard(leaderboard):
    with open("leaderboard.json", "w") as f:
        json.dump(leaderboard, f)

def load_leaderboard():
    try:
        with open("leaderboard.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def filter_leaderboard_by_difficulty(leaderboard, difficulty):
    return [entry for entry in leaderboard if entry["difficulty"] == difficulty]

def format_leaderboard(leaderboard):
    formatted = ""
    for entry in leaderboard:
        formatted += f"Name: {entry['name']}, Score: {entry['score']}\n"
    return formatted

# Initialize the socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(5)

print(f"server is listening on port {port}")
guessme = 0
conn = None
leaderboard = load_leaderboard()

while True:
    if conn is None:
        print("waiting for connection..")
        conn, addr = s.accept()
        print(f"new client: {addr[0]}")
        conn.sendall(banner.encode())
    else:
        client_input = conn.recv(1024).decode().strip()
        if client_input in ['a', 'b', 'c']:
            difficulty = client_input
            last_difficulty = difficulty
            guessme = generate_random_int(difficulty)
            conn.sendall(b"\n")
            tries = 0
        elif client_input.isdigit():
            guess = int(client_input)
            print(f"User guess attempt: {guess}")
            tries += 1
            if guess == guessme:
                conn.sendall(b"Correct Answer!\n")
                name = conn.recv(1024).decode().strip()
                score = tries
                update_leaderboard(name, score, difficulty, leaderboard)
                save_leaderboard(leaderboard)
                #conn.sendall(b"\nLeaderboard:\n" + format_leaderboard(filter_leaderboard_by_difficulty(leaderboard, difficulty)).encode())
                conn.sendall(b"LA CHA TA")
            elif guess > guessme:
                conn.sendall(b"Guess Lower! Try again! ")
                continue
            elif guess < guessme:
                conn.sendall(b"Guess Higher! Try again!")
                continue
        elif client_input == 'y':
            print("Koman")
        elif client_input.lower() != 'y':  # Check for play again before sending leaderboard
            conn.sendall(b"\nLeaderboard:\n" + format_leaderboard(filter_leaderboard_by_difficulty(leaderboard, difficulty)).encode())
        else:
            conn.sendall(b"Invalid input!\nEnter guess or choose difficulty level:")

