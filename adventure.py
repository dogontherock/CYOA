#Setup
import random
from os import system, name

#Variables and lists can just be setup, no need for functions
yes_no = ["yes", "no"]
directions = ["left", "right", "forward", "backward"]
myHP=20
level=1
gold=20
#This will save you time entering lots of if else statements

#Clears the screen
def clear():
 # for windows
 if name == 'nt':
  _ = system('cls')
  return()
 # for mac and linux(here, os.name is 'posix')
 else:
  _ = system('clear')

#Randmon animal generator
def animal():
 global monsterHP
 global colour
 global creature
 roll = random.randint(1,3)
 #print (roll)
 if roll == 1:
  creature='wolf'
  monsterHP=20
  colour='black'
 elif roll == 2:
  creature='bear'
  monsterHP=30
  colour='brown'
 elif roll == 3:
  creature='giant'
  monsterHP=40
  colour='pink'

#Old way to randomly generate the way you die
#def get_killing_blow():
#  roll = random.randint(1,5)
#  if roll == 1:
#   killing_blow = "knocked your head clean off"
#  if roll == 2:
#   killing_blow = "Your right arm was ripped off"
#  if roll == 3:
#    killing_blow = "your left arm was ripped off"
#  if roll == 4:
#    killing_blow = "you were hit so hard your spleen exploded"
#  if roll == 5:
#    killing_blow = "you died from massive blood loss"
#  return killing_blow

#New way to randomly generate the way you die - taken from a video by Rory
def get_killing_blow():
	deaths= [
  "knocked your head clean off",
  "Your right arm was ripped off",
  "your left arm was ripped off",
  "you were hit so hard your spleen exploded",
  "you died from massive blood loss"
  ]
	killing_blow = random.choice(deaths)
	return killing_blow

#The fight function
def fight():
 global myHP
 global monsterHP
 while True: #while lets us loop indefinately, True must have a capital
  number = random.randint(1, 10)
  print("You have " + str(myHP) + " hit points left. The " + creature + " has " + str(monsterHP) + " left")
  #guess=input("pick a number from 1 to 10 for the attack : ")
  #guess = int(input())
  guess=""
  while guess not in range(1,11):
            guess=int(input("pick a number from 1 to 10 for the attack : "))
            #guess = int(input())
  if guess >= number: # == is used to compare values, = is used to assign them
    print("Congratulations, You hit the monster")
    monsterHP=monsterHP-5
    if  monsterHP == 0:
     print("You killed the " + creature + " its " + colour + " body lies dead on the ground")
     return
  elif guess < number:
    print("You got hit")
    myHP=myHP-5
    if myHP == 0:
     killing_blow=get_killing_blow()
     print("The " + creature + " killed you. " +  killing_blow + " Farewell, " + player_name + ".")
     quit()

def end():
  print("Thanks for playing " + player_name + " you have " + str(myHP) + " hit points left. Come back when there is more to play")
  quit()

#these definitions or functions are just planned, nothing runs until they are called
def setup():
  global player_name
  player_name = input("What is your name, adventurer?\n")
  print("Greetings, " + player_name + ". Let us go on a quest!")
  print("You find yourself on the edge of a dark forest.")
  print("Can you find your way through?\n")
  game_start()
  #this goes to the game_start function below
  #it makes it easier to plana nd change extra parts later on

def game_start():
  response = ""
  while response not in yes_no:
      response = input("Would you like to step into the forest? - yes or no > ")
      if response == "yes":
        print("You head into the forest. You hear crows cawwing in the distance.\n")
        clear()
        entry_point()

      elif response == "no":
        print("You are not ready for this quest. Goodbye, " + player_name + ".")
        quit()
      else:
        print("I didn't understand that. Try again\n")

def the_bridge():
  location=the_bridge
  level=2
  print("You walk for several minutes through the forest, when you come accross a small bridge")
  response = ""
  while response not in yes_no:
      response = input("Would you like to cross the bridge? - yes or no > ")
      if response == "yes":
        animal()
        print("You head onto the bridge, halfway accross the bridge a big " + colour + " " + creature + " jumps out and attacks you")
        fight()
        yesno=""
        while yesno not in yes_no:
         yesno = input("You dust your self down, weary after the fight, do you wish to carry on the quest? - yes or no > ")
         if yesno == "yes":
           clear()
           print("You carry on walking for a while and come across a small inn")
           response=""
           while response not in yes_no:
            response=input("Do you wish to enter the inn - yes or no > ")
            if response == "yes":
             the_inn()
            elif response== "no":
              clear()
              print("You walk pask the inn and carry on down a  along a path, the path leads to the opening of a dungeon")
              the_dungeon()
         elif yesno == "no":
          clear()
          the_warning()
         else:
          print("I didn't understand that. Try again\n")
      elif response == "no":
       clear()
       the_warning()
      else:
       print("I didn't understand that. Try again\n")


def the_inn():
 clear()
 location="the_inn"
 global gold
 global myHP
 print("You are in an inn, across the back of the inn is a bar, in the corner is a roaring fire, next to the fire is a gentlman playing cups")
 response= ""
 while response not in ["cups","drink","leave"]:
  response = input("Do you want to play cups, buy a drink or leave - cups, drink, leave > ")
  if response == "cups":
   clear()
   print("5 Gold per bet 10 gold if you win")
   print("you have " + str(gold) + " gold")
   while True: #while lets us loop indefinately, True must have a capital
    yesno=""
    while yesno not in yes_no:
     yesno = input("Do you want to play - yes or no > ")
     if yesno == "yes":
      if gold==0:
        input("You do not have enough gold to play - sorry. Press return")
        the_inn()
      else:
       gold-=5
       number = random.randint(1, 3)
       print("Good, another mug...eh I mean contestant")
       print("which cup is the ball under, cup 1, cup 2 or cup 3 = 1, 2, 3 > ")
       guess = int(input())
       if guess == number: # == is used to compare values, = is used to assign them
        print("Congratulations, you found the cup!")
        gold+=10
        print("you have "+str(gold) + " gold")
       elif guess != number:
        #elif means else if, you use this when you have more than two outcomes
        print("Wrong Guess.")
        print("you have "+str(gold) + " gold")
     elif yesno == "no":
        the_inn()
     else:
      print("I didn't understand")
  elif response == "drink":
   print("Drinks are 20 gold and will heal you. You have " + str(myHP) + " hit points and  " + str(gold) + " gold")
   if gold < 20:
    print("You do not have enough gold for a drink")
    input("Press Enter to continue")
    the_inn()
   if gold >= 20:
    yesno=""
    while yesno not in yes_no:
     yesno = input("You have enough gold for a drink. Would you like to buy one = yes or no > ")
     if yesno == "yes":
      print("You are fully refreshed")
      myHP=20
      input("Press Enter to continue")
      the_inn()
     elif yesno== "no":
      print("You walk away thristy and tired")
      input("Press Enter to continue")
      the_inn()
  elif response == "leave":
    clear()
    print("You leave the inn and walk along a path, the path leads to the opening of a dungeon")
    the_dungeon()
 else:
  print("I didn't understand that. Try again\n")

def the_dungeon():
  print("Please come back later when the dungeon module is finished")
  end()

def the_maze():
 number = random.randint(5, 15)
 print(number)
 print("You walk through the forest until you reach then opening of a maze")
 print("Next to the opening stands a little old man who says 'I wouldn't go in there if I was you'")
 yesno=""
 while yesno not in yes_no:
  yesno = input("Do you want to enter the maze of never ending - yes or no > ")
  if yesno == "yes":
   clear()
   print("As you enter the maze it closes behind you, there is no going back the way you came")
   response=""
   count=0
   while response not in directions:
    while True: #while lets us loop indefinately, True must have a capital
     if count==number:
      print("You made it out of the maze - well done. You realise you are back where you started")
      entry_point()
     else:
      count=count+1
      response=input("You can go forward, left or right - forward, left or right > ")
     if response == "forward":
      print("You walk forward until you come to a cross roads")
      print("The maze it closes behind you, there is no going back the way you came")
     elif response == "left":
      print("You go left and keep walking until you come to a cross roads")
      print("The maze it closes behind you, there is no going back the way you came")
     elif response == "right":
      print("You go right and keep walking until you come to a cross roads")
      print("The maze it closes behind you, there is no going back the way you came")
    else:
     print("I do not understand")
  elif yesno == "no":
    the_warning()
  else:
    print("I do not understand")


def entry_point():
  global location
  location="entry_point"
  response = ""
  while response not in directions:
    animal()
    print("To your left you see a "+ colour + " " + creature + " with " + str(monsterHP) + " hit points")
    print("To your right, there is more forest.")
    print("There is a rock wall directly in front of you.")
    print("Behind you is the forest exit.\n")
    response = input("What direction do you move? = left or right or forward or backward > ")
    if response == "left":
        print("Lets Fight")
        fight()
        print("Well done on wining your first fight")
        input("Press Return")
        clear()
        the_bridge()
    elif response == "right":
        print("You head deeper into the forest.\n")

        the_maze()
    elif response == "forward":
        print("You cannot scale the wall.\n")
        response = ""
    elif response == "backward":
        print("You leave the forest. Goodbye, " + player_name + ".")
        quit()
    else:
        print("I didn't understand that. Try again\n")

def the_warning():
  response = ""
  while response not in yes_no:
    response = input("Are you afraid?\nyes/no\n")
    if response == "yes":
        print("Good, only a fool wouldn't be...\n")
    elif response == "no":
        print("You should be " + player_name + " you should be...")
        quit()
    else:
        print("I didn't understand, you are clearly to afraid to type. Try again\n")

#now we can call the first fucntion to run the game
setup()