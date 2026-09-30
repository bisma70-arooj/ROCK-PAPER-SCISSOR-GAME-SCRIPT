import random

print("ROCK PAPER SCISSOR SHOOT!!!!!")

choice_list = ["rock", "paper", "scissor"]
user_choice = input("ENTER YOUR MOVE = rock, paper, scissor ")
computer_choice = random.choice(choice_list)

print(f"so your choice is {user_choice} and computer's choice is {computer_choice}")


if user_choice == computer_choice:
        print("the match is tie ^~^")

elif user_choice == "rock":
    if computer_choice == "paper":
        print("COMPUTER WINNNN!")
    else:
        print("YOU WON!!")
elif user_choice == "paper":
    if computer_choice == "rock":
        print("YOU WINNNN!")
    else:
        print("COMPUTER WON!!")
elif user_choice == "scissor":
    if computer_choice == "rock":
        print("COMPUTER WINNNN!")
    else:
        print("YOU WON!!")        

         
