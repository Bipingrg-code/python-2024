import random

choices = ["Rock", "Paper", "Scissors"]
computer = random.choice(choices)
# player = None

# while player not in choices:
player = input("rock, paper, scissors?: ").lower()

if player == computer:
    print("computer: ", computer)
    print("player: ", player)
    print("It's a tie!")
elif player == "rock":
    if computer == "paper":
        print("computer: ", computer)
        print("player: ", player)
        print("ypu lose!")

    if computer == "scissors":
        print("computer: ", computer)
        print("player: ", player)
        print("ypu win!")
elif player == "scissors":
    if computer == "rock":
        print("computer: ", computer)
        print("player: ", player)
        print("ypu lose!")

    if computer == "paper":
        print("computer: ", computer)
        print("player: ", player)
        print("ypu win!")
elif player == "paper":
    if computer == "scissors":
        print("computer: ", computer)
        print("player: ", player)
        print("ypu lose!")

    if computer == "rock":
        print("computer: ", computer)
        print("player: ", player)
        print("ypu win!")
