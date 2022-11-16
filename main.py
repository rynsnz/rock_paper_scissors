import random

#0
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
#1
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
#2
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choice = random.randint(0, 2)
plays = [rock, paper, scissors]

if player_choice == 0:
    print(rock)
    if computer_choice == 0:
        print('Computer chose:')
        print(plays[computer_choice])
        print('Draw!')
    elif computer_choice == 1:
        print('Computer chose:')
        print(plays[computer_choice])
        print('You lose!')
    elif computer_choice == 2:
        print('Computer chose:')
        print(plays[computer_choice])
        print('You win!')
elif player_choice == 1:
    print(paper)
    if computer_choice == 0:
        print('Computer chose:')
        print(plays[computer_choice])
        print('You win!')
    elif computer_choice == 1:
        print('Computer chose:')
        print(plays[computer_choice])
        print('Draw!')
    elif computer_choice == 2:
        print('Computer chose:')
        print(plays[computer_choice])
        print('You lose!')

elif player_choice == 2:
    print(scissors)
    if computer_choice == 0:
        print('Computer chose:')
        print(plays[computer_choice])
        print('You lose!')
    elif computer_choice == 1:
        print('Computer chose:')
        print(plays[computer_choice])
        print('You win!')
    elif computer_choice == 2:
        print('Computer chose:')
        print(plays[computer_choice])
        print('Draw!')