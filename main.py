from functions import *
import time
import random

colors = ['\033[95m','\033[96m','\033[36m','\033[94m','\033[92m','\033[93m','\033[91m','\33[37m']

l1 = " ██████╗ ██████╗  ██████╗ ██╗  ██╗    ██████╗  ██████╗  ██████╗ ██╗  ██╗ "
l2 = "██╔════╝██╔═══██╗██╔═══██╗██║ ██╔╝    ██╔══██╗██╔═══██╗██╔═══██╗██║ ██╔╝ "
l3 = "██║     ██║   ██║██║   ██║█████╔╝     ██████╔╝██║   ██║██║   ██║█████╔╝  "
l4 = "██║     ██║   ██║██║   ██║██╔═██╗     ██╔══██╗██║   ██║██║   ██║██╔═██╗  "
l5 = "╚██████╗╚██████╔╝╚██████╔╝██║  ██╗    ██████╔╝╚██████╔╝╚██████╔╝██║  ██╗ "
l6 = " ╚═════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝    ╚═════╝  ╚═════╝  ╚═════╝ ╚═╝  ╚═╝ "
l7 = "}-------------------{+} THE PERFECT APP FOR COOKING {+}-----------------{"
l8 = "}---------------------{+} Coded By Rachit Chandak {+}-------------------{"
printedMessage = [l1, l2, l3, l4, l5, l6, l7, l8]
width = int(list(os.get_terminal_size())[0])
counter = 0
point = width
while True:

    os.system("clear")
    for row in range(6):
        print(" " * point + "{}".format(printedMessage[row][max(0,point*-1):width - point]))

    point -=1

    if point < (width//2 - 36):
        os.system("clear")
        print(' '*(width//2 - 36) + l1)
        print(' '*(width//2 - 36) + l2)
        print(' '*(width//2 - 36) + l3)
        print(' '*(width//2 - 36) + l4)
        print(' '*(width//2 - 36) + l5)
        print(' '*(width//2 - 36) + l6)
        print(' '*(width//2 - 36) + '\033[1m' + '\033[91m' + l7)
        print(' '*(width//2 - 36) + '\033[1m' + '\033[91m' + l8)
        print('\033[0m')
        time.sleep(3)
        os.system("clear")
        break
    time.sleep(.055)

try:
    file = open("inventory.txt",'r')
    file.close()
except:
    print("Inventory File Doesn't Exists")
    time.sleep(1)
    print("Making One...")
    time.sleep(1)
    file = open("inventory.txt", 'w')
    file.close()
    print("Enter Items In The Inventory First! ")
    item_entry()

file_size = os.stat("inventory.txt").st_size
if file_size == 0:
    print("Nothing In The Inventory...")
    time.sleep(1)
    print("Enter Items In The Inventory First!")
    item_entry()

while True:
    menu = '''
       {1}--You Can Make.
       {2}--Search.
       {3}--Your Supplies.
       {4}--You Need To Get.
       {5}--Recipes.
       {6}--Item Used.
       {7}--You Brought.
       {8}--Add Recipe.
       {99}-EXIT\n
'''
    print(menu)
    choice = int(input("Choose: "))
    os.system("clear")
    if choice == 1:
        check_dish()
    elif choice == 2:
        dish_checker()
    elif choice == 3:
        view_inv()
    elif choice == 4:
        inventory_check()
    elif choice == 5:
        view_rec()
    elif choice == 6:
        item_used()
    elif choice == 7:
        item_entry()
    elif choice == 8:
        recipe_entry()
    elif choice == 99:
        print("Bye. ")
        break
    else:
        print("Invalid Option!")
