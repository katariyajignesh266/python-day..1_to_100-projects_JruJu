print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

Side = input("you're at a cross road. where do you want to go? type 'left' or 'right' ")
if Side == "left":
    print("you've come to a lake. there is an island in in the middle of the lake.")
    inside = input("type 'wait' to wait for a boat. type 'swim' to swim across. ")
    if inside == "wait":
        print("You arrive at the island unharmed. there is a house with 3 doors.")
        colour = input("one red, one yellow and one blue. which colour do you choose? ")
        if colour == "yellow":
            print("you found the treasure! you win!")
        elif colour == "blue":
            print("it's a room of fire. game over.")
        else:
            print("it's a room of fire. game over.")
    else:
        print("you get attacked by an angry trout. game over.")
else:
    print("you fell into a hole. game over.")

