import socket

HOST = "localhost"  
PORT = 7777        

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.connect((HOST, PORT))
  print("Connected to server")

  # Receive and display server banner
  banner = s.recv(1024).decode()
  print(banner)

  while True:
    # Choose difficulty level
    difficulty_choice = input("Choose difficulty level (a/b/c): ")
    s.sendall(difficulty_choice.encode())

    # Receive prompt to enter guess
    guess_prompt = s.recv(1024).decode()
    print(guess_prompt)

    # Guessing loop
    while True:
      user_guess = input("Enter your guess: ")
      s.sendall(user_guess.encode())

      # Receive response from server
      response = s.recv(1024).decode()
      print(response)

      if "Correct Answer!" in response:
        break

    # Get name and send to server
    name = input("Enter your name: ")
    s.sendall(name.encode())
    
    # Play again prompt
    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() != 'y':
      leaderboard_data = s.recv(1024)
      print(leaderboard_data.decode())
      break
    
print("Thank you for playing!")
print("\n\n\n\n\n\n\n\n\nDisconnected from server")
