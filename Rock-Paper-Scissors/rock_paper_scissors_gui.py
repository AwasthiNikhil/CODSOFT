import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'tie'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return 'user'
    else:
        return 'computer'

def on_choice(choice):
    global user_score, computer_score

    user_choice = choice
    computer_choice = get_computer_choice()
    
    # Update images
    user_image = Image.open(f"{user_choice}.png")
    user_image = user_image.resize((100, 100))
    user_photo = ImageTk.PhotoImage(user_image)
    user_label.config(image=user_photo)
    user_label.image = user_photo
    
    computer_image = Image.open(f"{computer_choice}.png")
    computer_image = computer_image.resize((100, 100))
    computer_photo = ImageTk.PhotoImage(computer_image)
    computer_label.config(image=computer_photo)
    computer_label.image = computer_photo

    result = determine_winner(user_choice, computer_choice)

    if result == 'user':
        user_score += 1
        messagebox.showinfo("Result", "You win!")
    elif result == 'computer':
        computer_score += 1
        messagebox.showinfo("Result", "You lose!")
    else:
        messagebox.showinfo("Result", "It's a tie!")

    score_label.config(text=f"Score - You: {user_score}, Computer: {computer_score}")

def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    score_label.config(text="Score - You: 0, Computer: 0")
    user_label.config(image='')
    computer_label.config(image='')

# Create the main window
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")

# Initialize scores
user_score = 0
computer_score = 0

# Load images
rock_img = Image.open("rock.png")
paper_img = Image.open("paper.png")
scissors_img = Image.open("scissors.png")

rock_img = rock_img.resize((100, 100))
paper_img = paper_img.resize((100, 100))
scissors_img = scissors_img.resize((100, 100))

rock_photo = ImageTk.PhotoImage(rock_img)
paper_photo = ImageTk.PhotoImage(paper_img)
scissors_photo = ImageTk.PhotoImage(scissors_img)

# Create and place widgets
tk.Button(root, image=rock_photo, command=lambda: on_choice('rock')).grid(row=0, column=0, padx=10, pady=10)
tk.Button(root, image=paper_photo, command=lambda: on_choice('paper')).grid(row=0, column=1, padx=10, pady=10)
tk.Button(root, image=scissors_photo, command=lambda: on_choice('scissors')).grid(row=0, column=2, padx=10, pady=10)

user_label = tk.Label(root)
user_label.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

computer_label = tk.Label(root)
computer_label.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

score_label = tk.Label(root, text="Score - You: 0, Computer: 0", font=("Helvetica", 14))
score_label.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

tk.Button(root, text="Reset Game", command=reset_game).grid(row=4, column=0, columnspan=3, padx=10, pady=10)

# Run the application
root.mainloop()
