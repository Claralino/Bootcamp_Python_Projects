import random

computer_choice = random.randint(0, 2)
choice_string = input("what do you choose? type 0 for rock, 1 for paper, 2 for scissors: ")
choice = ['rock', 'paper', 'scissors']


if choice[0]:
    if computer_choice == 0:
        print(f"you choose {choice[0]}, and the computer rock, no one wins")
    elif computer_choice == 1:
        print(f"you choose {choice[0]}, and the computer paper, you lost")
    else:
        print(f"you choose {choice[0]}, and the computer scissors, you win")
elif choice[1]:
    if computer_choice == 0:
        print(f"you choose {choice[1]}, and the computer rock, you win")
    elif computer_choice == 1:
        print(f"you choose {choice[1]}, and the computer paper, no one wins")
    else:
        print(f"you choose {choice[1]}, and the computer scissors, you lost")
elif choice[2]:
    if computer_choice == 0:
        print(f"you choose {choice[2]}, and the computer rock, you lose")
    elif computer_choice == 1:
        print(f"you choose {choice[2]}, and the computer paper, you win")
    else:
        print(f"you choose {choice[2]}, and the computer scissors, no one wins")




