import random
while True:
    str = input("Roll the dice? (y/n)? ")
    if str == 'y':
        comp_dice = random.randint(1,6)
        print(f"You rolled a {comp_dice}")
    elif str == 'n':
        print("---------------QUITTING---------------")
        break
    else:
        print("You chose wrong. So choose again")