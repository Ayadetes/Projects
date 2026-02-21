import random
PossibleComputerReactions = ["rock", "paper", "scissors"]
ComputeReactions = random.choice(PossibleComputerReactions)
inpu = str(input("Rock, Paper, or Scissors? \n").lower())
print("The computer's reaction is ", ComputeReactions, ".", sep="")
if inpu == ComputeReactions:
    print("You and the computer cancel out eachother \nbecause you both picked",inpu)
elif inpu == "scissors":
    if ComputeReactions == "rock":
        print("The Rock bends you, you lose")
    else:
        print("You cut the paper, you win")
elif inpu == "rock":
    if ComputeReactions == "paper":
        print("The paper wraps you, you lose")
    else:
        print("You bend your enemy's scissors, you win")
else:
    if ComputeReactions == "rock":
        print("You wrap the rock, you win")
    else:
        print("You get cut by scissors, you lose")