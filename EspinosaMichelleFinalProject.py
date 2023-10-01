import tkinter as tk
import random
from PIL import Image, ImageTk

def play_game(player_choice):
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)
    result = ""

    if player_choice == computer_choice:
        result = "It's a tie!"
    elif (
        (player_choice == "Rock" and computer_choice == "Scissors")
        or (player_choice == "Paper" and computer_choice == "Rock")
        or (player_choice == "Scissors" and computer_choice == "Paper")
    ):
        result = "You win!"
    else:
        result = "Computer wins!"

    result_label.config(text=f"Computer chose: {computer_choice}\n{result}")

# Create the main window
window = tk.Tk()
window.title("Rock, Paper, Scissors Game")



# Images for rock, paper, scissors
imageRock = Image.open('rock.png')
imageRock = imageRock.resize((100, 100),)
imageRock = ImageTk.PhotoImage(imageRock)
imagePaper = Image.open('paper.png')
imagePaper = imagePaper.resize((100, 100),)
imagePaper = ImageTk.PhotoImage(imagePaper)
imageScissor = Image.open('scissor.png')
imageScissor = imageScissor.resize((100, 100),)
imageScissor = ImageTk.PhotoImage(imageScissor)

# Create buttons for player choices
rock_button = tk.Button(window, image=imageRock, command=lambda: play_game("Rock"))
paper_button = tk.Button(window, image=imagePaper, command=lambda: play_game("Paper"))
scissors_button = tk.Button(window, image=imageScissor, command=lambda: play_game("Scissors"))

# Create a label to display results
result_label = tk.Label(window, text="", font=("Helvetica", 14))

# Place buttons and labels on the window
rock_button.pack()
paper_button.pack()
scissors_button.pack()
result_label.pack()

# Start the main loop
window.mainloop()

