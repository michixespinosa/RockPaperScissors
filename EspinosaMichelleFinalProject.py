import tkinter as tk
import random
from PIL import Image, ImageTk

# Initialize scores
player_score = 0
computer_score = 0

# User accounts
user_accounts = {}
 

# Initialize the main window
window = tk.Tk()
window.title("Rock, Paper, Scissors Game")

# Images for rock, paper, scissors
imageRock = Image.open('rock.png')
imageRock = imageRock.resize((100, 100))
imageRock = ImageTk.PhotoImage(imageRock)
imagePaper = Image.open('paper.png')
imagePaper = imagePaper.resize((100, 100))
imagePaper = ImageTk.PhotoImage(imagePaper)
imageScissor = Image.open('scissor.png')
imageScissor = imageScissor.resize((100, 100))
imageScissor = ImageTk.PhotoImage(imageScissor)


# Function to disable game buttons
def disable_game_buttons():
    global player_score
    global computer_score

    rock_button.config(state="disabled")
    paper_button.config(state="disabled")
    scissors_button.config(state="disabled")
    player_score = 0
    computer_score = 0
    
    result_label.pack()
    player_score_label.pack()
    computer_score_label.pack()
    logout_button.pack()

    result_label.config(text=f"")
    player_score_label.config(text=f"Player: {player_score}")
    computer_score_label.config(text=f"Computer: {computer_score}")



# Function to play the game
def play_game(player_choice, username):
    global player_score, computer_score
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)
    result = ""

    logout_button.pack()

    if player_choice == computer_choice:
        result = "It's a tie!"
    elif (
        (player_choice == "Rock" and computer_choice == "Scissors")
        or (player_choice == "Paper" and computer_choice == "Rock")
        or (player_choice == "Scissors" and computer_choice == "Paper")
    ):
        result = f"{username} wins!"
        player_score += 1
    else:
        result = "Computer wins!"
        computer_score += 1

    result_label.config(text=f"Computer chose: {computer_choice}\n{result}")
    player_score_label.config(text=f"Player: {player_score}")
    computer_score_label.config(text=f"Computer: {computer_score}")

# User registration and login function
def register_and_login():
    username = username_entry.get()
    password = password_entry.get()
    
    if username and password:
        if username in user_accounts:
            if user_accounts[username] == password:
                login_label.config(text=f"Welcome back, {username}!")
                enable_game_buttons(username)
            else:
                login_label.config(text="Invalid password.")
        else:
            user_accounts[username] = password
            login_label.config(text=f"Registration successful, {username}!")
            enable_game_buttons(username)
    else:
        login_label.config(text="Please enter a username and password.")

# Function to enable game buttons
def enable_game_buttons(username):
    rock_button.config(state="active", command=lambda: play_game("Rock", username))
    paper_button.config(state="active", command=lambda: play_game("Paper", username))
    scissors_button.config(state="active", command=lambda: play_game("Scissors", username))
    
# Create labels to display results and scores
result_label = tk.Label(window, text="", font=("Helvetica", 14))
player_score_label = tk.Label(window, text=f"Player: {player_score}", font=("Helvetica", 12))
computer_score_label = tk.Label(window, text=f"Computer: {computer_score}", font=("Helvetica", 12))
logout_button = tk.Button(window, text="logout", command=disable_game_buttons)

# Place labels on the window
result_label.pack()
player_score_label.pack()
computer_score_label.pack()
logout_button.pack()


# Create a registration/login window
registration_window = tk.Toplevel(window)
registration_window.title("User Registration / Login")

# Comments for registration/login section
login_label = tk.Label(registration_window, text="Register or Log in to play")
username_label = tk.Label(registration_window, text="Username:")
username_entry = tk.Entry(registration_window)
password_label = tk.Label(registration_window, text="Password:")
password_entry = tk.Entry(registration_window, show="*")
register_button = tk.Button(registration_window, text="Register / Log in", command=register_and_login)


login_label.pack()
username_label.pack()
username_entry.pack()
password_label.pack()
password_entry.pack()
register_button.pack()

# Create buttons for player choices (initially disabled)
rock_button = tk.Button(window, image=imageRock, state="disabled")
paper_button = tk.Button(window, image=imagePaper, state="disabled")
scissors_button = tk.Button(window, image=imageScissor, state="disabled")

# Place buttons on the window
rock_button.pack()
paper_button.pack()
scissors_button.pack()

# Start the main loop
window.mainloop()