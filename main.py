print('''
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
''')
print("Welcome to the Treasure island\nYour mission is to find the treasure ")

cross_road=input('you are at a cross road. where do you want to go?Type "left" or "right"\n')

if(cross_road=="left"):
  print("you've come to lake.There is a island in the middle of the lake.Type 'wait' to wait for a lake. Type 'swim' to swim across")
elif(cross_road=="right"):
  print("You fell into a hole.Game over")
else:
  print("You write wrong option")
wait_swim=input()
if(wait_swim=="wait"):
  print('You arrived at island unharmed.There is a house with 3 doors.One red, one yellow and one blue. Which colour do you chose?')
elif(wait_swim=="swim"):
  print("YOu get attacked by a angry trout.Game over.")
else:
  print("You write wrong option")
room=input()
if(room=="yellow"):
  print("you found the treasure: you win!")
elif(room=="blue"):
  print("You enter a room of beasts.Game over")
elif(room=="red"):
  print("It's a room full of fire.Game over")
else:
  print("You write wrong option")