# ***********************Treminal base project**************************



# import random;
# cscore=0;
# hscore=0;
# while True:
#     print(f"Current score you - {hscore} computer - {cscore}\n")
#     user=(int(input("1 for stone 2 for paper and 3 for sessior choose --:")))
#     com=random.randint(1,3)
#     if user==1 and com==3:
#         hscore+=1;
#         print("you won the round \n");
#     elif user==2 and com==1:
#         hscore+=1;
#         print("you won the round \n");
#     elif user ==3 and  com==2:
#         hscore+=1;
#         print("you won the round \n");
#     elif user== com:
#         print("It was draw:");
#     else:
#         cscore+=1;
#         print("computer won this round") 
#     if cscore ==5:
#         print("computer won this game:")
#         break;
#     elif hscore==5:
#         print("Congratulation you won:");
#         break








# *********************************ui base project**************************8 

import tkinter as tk
import random

cscore = 0
hscore = 0

def play(user_choice):
    global cscore, hscore
    com_choice = random.randint(1, 3)

    choices = {1: "Stone", 2: "Paper", 3: "Scissor"}

    user_label.config(text=f"You chose: {choices[user_choice]}")
    computer_label.config(text=f"Computer chose: {choices[com_choice]}")

    if (user_choice == 1 and com_choice == 3) or \
       (user_choice == 2 and com_choice == 1) or \
       (user_choice == 3 and com_choice == 2):

        hscore += 1
        result_label.config(text="You won this round!", fg="green")
    elif user_choice == com_choice:
        result_label.config(text="It's a Draw!", fg="blue")
    else:
        cscore += 1
        result_label.config(text="Computer won this round!", fg="red")

    score_label.config(text=f"Score → You: {hscore}   Computer: {cscore}")

    if hscore == 5:
        result_label.config(text="🎉 YOU WON THE GAME!", fg="green")
        disable_buttons()
    elif cscore == 5:
        result_label.config(text="💀 COMPUTER WON THE GAME!", fg="red")
        disable_buttons()


def disable_buttons():
    stone_btn.config(state=tk.DISABLED)
    paper_btn.config(state=tk.DISABLED)
    scissor_btn.config(state=tk.DISABLED)


# ---------------- UI ----------------
root = tk.Tk()
root.title("Stone Paper Scissor")
root.geometry("350x400")

score_label = tk.Label(root, text="Score → You: 0   Computer: 0",
                       font=("Arial", 14))
score_label.pack(pady=10)

user_label = tk.Label(root, text="You chose: -", font=("Arial", 12))
user_label.pack()

computer_label = tk.Label(root, text="Computer chose: -", font=("Arial", 12))
computer_label.pack()

result_label = tk.Label(root, text="", font=("Arial", 16, "bold"))
result_label.pack(pady=20)

stone_btn = tk.Button(root, text="STONE", width=15, font=("Arial", 12),
                      command=lambda: play(1))
stone_btn.pack(pady=5)

paper_btn = tk.Button(root, text="PAPER", width=15, font=("Arial", 12),
                      command=lambda: play(2))
paper_btn.pack(pady=5)

scissor_btn = tk.Button(root, text="SCISSOR", width=15, font=("Arial", 12),
                        command=lambda: play(3))
scissor_btn.pack(pady=5)

root.mainloop()
