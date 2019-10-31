import random
Comp_point = 0
Your_point = 0
print("Enter --> rock | paper | scissor")
Random_ = ["rock", "paper", "scissor"]
while True:
    InpuT = str(input("User: "))

    RandoM = random.choice(Random_)
    print("Computer:",RandoM)
    if InpuT == RandoM:
        print("Tie (0 point)")

    #In case of paper
    elif InpuT == "paper" and RandoM == "rock":
        print("You win (1 point)")
        Your_point = Your_point + 1
    elif InpuT == "paper" and RandoM == "scissor":
        print("Computer win (1 point)")
        Comp_point = Comp_point + 1

    #In case of scissor
    elif InpuT == "scissor" and RandoM == "paper":
        print("You win (1 point)")
        Your_point = Your_point + 1
    elif InpuT == "scissor" and RandoM == "rock":
        print("Computer win (1 point)")
        Comp_point = Comp_point + 1

    #In case of stone
    elif InpuT == "rock" and RandoM == "scissor":
        print("You win (1 point)")
        Your_point = Your_point + 1
    elif InpuT == "rock" and RandoM == "paper":
        print("Computer win (1 point)")
        Comp_point = Comp_point + 1
    else:
        print("you entered wrong input \n")
    print("Your Point:",Your_point,"Computer Point:",Comp_point)
    if(Your_point == 5):
        print("you won the game")
        print(f"you beat computer with {Your_point - Comp_point} points")
        break
    elif(Comp_point == 5):
        print("you lost the game")
        print(f"computer beat you with {Comp_point - Your_point} points")
        break

