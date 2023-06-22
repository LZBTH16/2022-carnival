#Creating a 'Carnival' type code

#importing important stuff for the code
import time
import random
import turtle
#making a variable to only type one letter instead of the full 'turtle' when using the module
t = turtle

#Creating a selection list for the user to select one of the activities
#having some welcome words before providing the starting list of activities
print("Welcome to the Easter Egg Carnival!")
print("Please make a selection from the following activities below:")
activities = ["1. Mini Mad Libs", "2. Rock, Paper, Scissors", "3. A Fun Picture"]
print(activities)
chooseactivity = int(input("Activity Number: "))

if(chooseactivity == 1):
    #Section 1 - smaller scale Mad Libs

    #making the variables
    #noun variables
    noun1 = str(input("name of a city: "))
    noun2 = str(input("group of something, plural: "))
    noun3 = str(input("type of transportation (ex. car, plane): "))
    noun4 = str(input("another name of a city: "))

    #verb variables
    verb1 = str(input("moving verb in the past tense: "))
    verb2 = str(input("another moving verb in the past tense: "))
    verb3 = str(input("and another moving verb in the past tense: "))
    verb4 = str(input("verb, in the present tense: "))

    #number variables
    num1 = int(input("Please enter a number: "))
    num2 = int(input("Another number: "))
    num3 = int(input("A third number: "))
    num4 = int(input("And a final number: "))

    #calculations from the number variables
    num5 = num1 - num3
    num6 = num4 * num2
    num7 = num2 + num1
    num8 = num3 / num4

    #extra variables
    timeperiod = str(input("A period of time (ex. months, days, years): "))


    #welcoming the user to the activity
    print("Welcome to Mini Mad Libs!")

    #the story
    #first paragraph
    print("Team Sparty - PART 2")
    print("Many ", timeperiod, "had gone by since the sad loss of Team Sparty in the city of ", noun1, ".", end=" ")
    print(num6, noun2, "decided to have a rematch Amazing Race in a different city.", end=" ")
    print("This time, they had a new driver who ", verb1, "the", noun3, "at the same pace as the previous driver.")
    print("Team Sparty", verb2, "the", noun3, "with", num7, "times more speed than the last time.")
    #second paragraph
    print("The ", noun3, "driver ", end=" ")
    print(verb3, verb3, verb3, sep=" and ", end=" ")
    print(" until they reached the destination of", noun4, ".")
    print("There, they would ", verb4, "for the team that defeated them.")
    print("They", end=" ")
    print("searched ", "searched ", "searched ", sep="and ", end=" ")
    print("but they didn't find the other team.")
    print("Therefore, Team Sparty had automatically won the rematch due to the other team not showing up.")
    #Creating a space to separate the story from the end bit
    print("This is the end of the story!")
    print("I hope you enjoyed creating the mini sequel to the first story!")

    #another Easter egg comment (1/3)
elif(chooseactivity == 2):
    #Section 2 - Rock, Paper, Scissors

    #allowing the user to choose how many rounds they play
    #rounds = int(input("Amount of rounds: "))

    #list from which the computer will choose from
    rps = ["Rock", "Paper", "Scissors"]
    #making the computer select a random selection
    rpscomp = random.choice(rps)
    #print("The computer has chosen", rpscomp)

    #Welcoming the user to the game
    print("Welcome to Rock, Paper, Scissors!")

    #creating user input for the r/p/s selection
    rpsguess = str(input("Please make your selection between 'rock, paper, or scissors': "))

    #waiting function
    def wait_Time():
        print("Comparing selections...")
        #delaying seeing the results
        time.sleep(1)

    #a function for when the player runs out of rounds
    def rounds_print():
        print("You have run out of rounds, resulting in the end of the game.")

    wait_Time()


    if(rpsguess == rpscomp):
        print("You have tied with the computer, no win or loss")
    else:
        #if the guess equals rock
        if(rpsguess == "Rock"):
            if(rpscomp == "Scissors"):
                print("The computer has chosen Scissors, resulting in a win!")
            else:
                print("The computer has chosen Paper, resulting in a loss :(")
        #if the guess equals scissors
        if(rpsguess == "Scissors"):
            if(rpscomp == "Paper"):
                print("The computer has chosen Paper, resulting in a win!")
            else:
                print("The computer has chosen Rock, resulting in a loss :(")
        #ifi the guess equals paper
        if(rpsguess == "Paper"):
            if(rpscomp == "Rock"):
                print("The computer has chosen Rock, resulting in a win!")
            else:
                print("The computer has chosen Scissors, resulting in a loss :(")

    #Easter egg comment (2/3)
else:
    #Section 3 - Turtle module

    #Welcoming the user to the activity
    print("Welcome to a picture drawing activity!")

    #starting position
    start1 = int(input("Please choose your starting position, first coordinate (ex. 10): "))
    start2 = int(input("Please choose your starting position, second coordinate (ex. 10): "))
    #how fast the pen should move
    userspeed = int(input("How fast would you like the turtle to move? "))
    #Allowing the user to choose a colour of the pen
    pencolour = str(input("What colour would you like for the pen to be? "))
    #how many times the line drawing occurs
    linecount = int(input("How many times should the action repeat? "))
    #how many pixels forward it should move
    forwardcount = int(input("How many pixels should the turtle move forward? "))
    #to move to right
    rightmove = int(input("How many degrees should the turtle move right? "))

    #won't show the line when it moves to that position
    t.penup()
    #will move it to the position the user inputted
    t.goto(start1, start2)
    #will have the pen showing again
    t.pendown()
    #the speed of the drawing
    t.speed(userspeed)
    #the pen colour
    t.pencolor(pencolour)
    #to repeat the motion
    for i in range(linecount):
        t.fd(forwardcount)
        t.rt(rightmove)
        rightmove+= 5

    #keeps the program running
    input(' ')

#another Easter egg comment (3/3)