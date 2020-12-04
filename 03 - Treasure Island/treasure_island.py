print(
    '''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
'''
)
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.\n\n")

# https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

direction = input("You see a path which forks before you.  Type 'left' or 'right' to choose which path to follow.\n")
if direction == "left":
    print("The path quickly leads to a deadend and a boulder falls on your head, killing you.\nGame Over!")
else:
    water = input("You follow the path and come to a lake.  You can swim or wait for a boat.  Type 'swim' or 'wait'.\n")
    if water == "swim":
        print(
            "You start swimming in the lake and you don't make it far before a giant alligator surfaces and chomps you to death.\nGame Over!"
        )
    else:
        door = input(
            "You wait for a boat, and when it arrives it ferries you to a small island.  You find a wall with 3 doors, one red, one blue, and one yellow. Which door do you try to open?  Type 'blue', 'red', or 'yellow'.\n"
        )
        if door == "red":
            print("The door's handle is coated in a swift-acting poison and you keel over and die.\nGame Over!")
        elif door == "blue":
            print(
                "The door is charged with a sizable electric current and shocks you to death as soon as you approach.\nGame Over!"
            )
        else:
            print("You have made a choice which opens the door to great treasure!\nYou Win!")
