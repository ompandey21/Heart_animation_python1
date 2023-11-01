import random
user_choice=input("Enter your choice(rock/paper/scissor): ").lower()
li=["rock","paper","scissor"]
computer_choice= random.choice(li)
print(f"Computer's Choice = {computer_choice}")
if user_choice=="rock" and computer_choice=="paper":
    print("Computer Wins!")
elif user_choice=="paper" and computer_choice=="scissor":
    print("Computer Wins!")
elif user_choice=="scissor" and computer_choice=="rock":
    print("Computer Wins!")
elif computer_choice==user_choice:
    print("Match tied!!...let's try again")
elif user_choice=="paper" and computer_choice=="rock":
    print("You Win,Congratulations!!")
elif user_choice=="scissor" and computer_choice=="paper":
    print("You Win,Congratulations!!")
elif user_choice=="rock" and computer_choice=="scissor":
    print("You Win,Congratulations!!")
else:
    print("Invalid input")

