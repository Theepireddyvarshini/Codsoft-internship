import tkinter as tk
import random

def play(user_choice):
    c = ['rock', 'paper', 'scissor']
    computer_choice = random.choice(c)

    # Display user and computer choices
    user_label.config(text=f"You chose: {user_choice}")
    computer_label.config(text=f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        result_label.config(text="It's a Tie!", fg="cyan")
    elif (user_choice == 'rock' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'scissor') or \
         (user_choice == 'scissor' and computer_choice == 'rock'):
        result_label.config(text="Computer won the game!", fg="red")
    elif (computer_choice == 'rock' and user_choice == 'paper') or \
         (computer_choice == 'paper' and user_choice == 'scissor') or \
         (computer_choice == 'scissor' and user_choice == 'rock'):
        result_label.config(text="You won the game!", fg="lime")
    else:
        result_label.config(text="Invalid input", fg="orange")

# Create the main window
root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("400x350")
root.resizable(False, False)
root.configure(bg="black")

# Header
tk.Label(root, text="Rock Paper Scissors", font=("Helvetica", 18, "bold"), bg="black", fg="white").pack(pady=10)

# Buttons
button_frame = tk.Frame(root, bg="black")
button_frame.pack()

btn_style = {"width": 10, "bg": "gray20", "fg": "white", "activebackground": "gray40"}

tk.Button(button_frame, text="Rock", **btn_style, command=lambda: play("rock")).grid(row=0, column=0, padx=10, pady=10)
tk.Button(button_frame, text="Paper", **btn_style, command=lambda: play("paper")).grid(row=0, column=1, padx=10, pady=10)
tk.Button(button_frame, text="Scissor", **btn_style, command=lambda: play("scissor")).grid(row=0, column=2, padx=10, pady=10)

# Display labels
user_label = tk.Label(root, text="", font=("Helvetica", 12), bg="black", fg="white")
user_label.pack()

computer_label = tk.Label(root, text="", font=("Helvetica", 12), bg="black", fg="white")
computer_label.pack()

result_label = tk.Label(root, text="", font=("Helvetica", 14, "bold"), bg="black")
result_label.pack(pady=10)

# Exit Button
exit_button = tk.Button(root, text="Exit", command=root.destroy, width=10, bg="white", fg="black", activebackground="lightgray")
exit_button.pack(pady=10)

# Start GUI
root.mainloop()
