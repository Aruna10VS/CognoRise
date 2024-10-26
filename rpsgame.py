import random
import tkinter as tk

player_score = 0
computer_score = 0

def play(player_choice):
    global player_score, computer_score
    options = ("rock", "paper", "scissors")
    computer_choice = random.choice(options)
    
    result_label.config(text=f"Computer chose: {computer_choice}")
    
    if player_choice == computer_choice:
        feedback = "It's a tie!"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        feedback = "Congrats..! You win!"
        player_score += 1  
    else:
        feedback = "Oops...You lose!"
        computer_score += 1 
    
    result_label.config(text=f"Computer chose: {computer_choice}\n{feedback}")
    score_label.config(text=f"Player: {player_score}  |  Computer: {computer_score}")


def reset_game():
    global player_score, computer_score
    player_score = 0
    computer_score = 0
    result_label.config(text="Make your move!")
    score_label.config(text=f"Player: {player_score}  |  Computer: {computer_score}")


def exit_game():
    root.quit()

root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("600x500")  
instructions = tk.Label(root, text="Choose rock, paper, or scissors:", font=("Arial", 16, "bold"))
instructions.pack(pady=20)

button_frame = tk.Frame(root)
button_frame.pack(pady=20)

rock_button = tk.Button(button_frame, text="Rock", width=12, font=("Arial", 14, "bold"), command=lambda: play("rock"))
rock_button.grid(row=0, column=0, padx=10)

paper_button = tk.Button(button_frame, text="Paper", width=12, font=("Arial", 14, "bold"), command=lambda: play("paper"))
paper_button.grid(row=0, column=1, padx=10)

scissors_button = tk.Button(button_frame, text="Scissors", width=12, font=("Arial", 14, "bold"), command=lambda: play("scissors"))
scissors_button.grid(row=0, column=2, padx=10)

result_label = tk.Label(root, text="Make your move!", font=("Arial", 16, "bold"), fg="blue")
result_label.pack(pady=20)


score_label = tk.Label(root, text=f"Player: {player_score}  |  Computer: {computer_score}", font=("Arial", 16, "bold"))
score_label.pack(pady=10)


button_frame2 = tk.Frame(root)
button_frame2.pack(pady=20)

reset_button = tk.Button(button_frame2, text="Reset", font=("Arial", 14, "bold"), command=reset_game)
reset_button.grid(row=0, column=0, padx=40)

exit_button = tk.Button(button_frame2, text="Exit", font=("Arial", 14, "bold"), command=exit_game)
exit_button.grid(row=0, column=1, padx=40)

root.mainloop()
