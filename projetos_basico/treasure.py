
print("welcome to the treasure island!\n your mission is to find the treasure.")

answer1 = input("you are at a cross road, where do you want to go? type 'left' or 'right'")
answer1_lower = answer1.lower()

if answer1_lower == 'left':
    answer2 = input("you arrived at a island. Do you want to swim or wait for the boat? Type 'swim' or 'wait'")
    answer2_lower = answer2.lower()
    if answer2_lower == 'wait':
        answer3 = input("there are 3 doors, wich do you want to choose? Type 'red','blue', or 'yellow'")
        answer3_lower = answer3.lower()
        if answer3_lower == 'yellow':
            print("you win the game!")
        elif answer3_lower == 'red':
            print("you died")
        else:
            print("you died")
    else: 
        print("you died")
else:
    print("you died")

