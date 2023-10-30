answer = input("Would you like to play (yes/no)")
if answer.lower().strip() == 'yes':
    answer = input("You reached a crossroads, would you like to go left or right?")
    if answer == "left":
        answer = input("You encounter a monster, would you like to run or attack?")

        if answer == "attack":
            print("That was not a great idea, you lost!")
        else: print("Good choice, you made it away safely.")
        
        answer = input("You see a car and a plane. Which one will you take? (car/plane)")
        if answer == "plane":
            print("Unfortunately, you do not know how to fly... You crash and burn. Game over!")
        else:
            print("You won!!!")
    elif answer == "right":
        print("You walk aimlessly to the right, and fall on a patch of ice. You injure your leg and cannot continue. Game over!")
    else: print("Invalid choice, you lose!")
else:
    print('Thats too bad')