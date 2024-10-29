from random import randrange

def userWeapon():
    print("Sellect your weapon (1 - 3) \n" + "-"*15)
    print("1. Rock \n2. Paper \n3. Scissors")
    weapon = -1
    while weapon != 1 and weapon != 2 and weapon != 3:
        weapon = int (input("Enter your weapon: "))
    return weapon
def computerWeapon():
    weapon = randrange(1,3)
    return weapon

def winner(user , computer):
    if user == computer:
        print("its a tie!")
    elif user == 1 and computer == 2:
        print("You lose, Paper covers Rock")
    elif user == 1 and computer == 3:
        print("You win, Rock crushes Scissors")
    elif user == 2 and computer == 1:
        print("You win, Paper covers Rock")
    elif user == 2 and computer == 3:
        print("You lose, Scissors cuts Paper")
    elif user == 3 and computer == 1:
        print("You lose, Rock crushes Scissors")
    elif user == 3 and computer == 2:
        print("You lose, Scissors cuts Paper")


def main():
    play_again = "y"
    while play_again == "y":
        winner(userWeapon(),computerWeapon())
        play_again = input("would you like to play again (y/n)").lower()
        while play_again.lower() != "y" and play_again.lower() != "n":
            play_again = input("would you like to play again (y/n)").lower()
    print("\n" + "-"*15)
    print("Coded by samuel Simmons")


