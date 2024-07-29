import random
rock = '''
    _______
---'   ____)
      (_)
      (_)
      ()
---.(_)
'''

paper = '''
    _______
---'   ___)___
          ______)
          _______)
         _______)
---.)
'''

scissors = '''
    _______
---'   ___)___
          ______)
       __________)
      ()
---.(_)
'''

#Write your code below this line 👇

computer_choice = random.randint(0,2)

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

rock_paper_scissors = [rock,paper,scissors]

print(f"Computer chose:\n {rock_paper_scissors[computer_choice]}")
print(f"Your choice:\n {rock_paper_scissors[user_choice]}")

if computer_choice == 0 and user_choice == 0:
    print("Draw")
elif computer_choice == 0 and user_choice == 1:
    print("You win")
elif computer_choice == 0 and user_choice == 2:
    print("You lose")

elif computer_choice == 1 and user_choice == 1:
    print("Draw")
elif computer_choice == 1 and user_choice == 2:
    print("You win")
elif computer_choice == 1 and user_choice == 0:
    print("You lose")

if computer_choice == 2 and user_choice == 2:
    print("Draw")
elif computer_choice == 2 and user_choice == 0:
    print("You win")
elif computer_choice == 2 and user_choice == 1:
    print("You lose")

else:
    print("Invalid Choice")