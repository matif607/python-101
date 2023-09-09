rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

player = input("chose rock paper or scissor\n")

computer_choice = ["rock", "paper", "scissor"]
computer = random.choice(computer_choice)
print(computer)

if player != computer:
  if player == "rock" and computer == "paper":
    print("Computer wins")
  elif player == "scissor" and computer == "paper":
    print("player wins")
  elif player == "rock" and computer == "scissor":
    print("player wins")
  elif player == "paper" and computer == "scissor":
    print("computer wins")
  elif player == "paper" and computer == "rock":
    print("player wins")
  elif player == "scissor" and computer == "rock":
    print("computer wins")
else:
  print("it's a draw")