import random

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

choices = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

print(choices[user_choice])

print("Computer chose: ")

Computer_choose = random.randint(0,2)
print(choices[Computer_choose])

if user_choice == 0 and Computer_choose == 1:
    print("you lose")
elif user_choice == 0 and Computer_choose == 2:
    print("you win")
elif user_choice == 1 and Computer_choose == 2:
    print("you lose")
elif user_choice == 1 and Computer_choose == 0:
    print("you win")
elif user_choice == 2 and Computer_choose == 1:
    print("you win")
elif user_choice == 2 and Computer_choose == 0:
    print("you lose")
else:
    print("It's a draw")
