#Alinea Grace M. Del Mundo
#This is adventure game

def scene():
    print('You are standing on a trail in a forest')
    print('Before the trail splits in two')
    print('Which way will you go right or left?','\n')

def makeChoice():
    choice = ''
    while choice != '1' and choice !='2':
        print('Press 1 followed by enter to choose the first option')
        print('Press 2 followed by enter to choose the second option')
        choice = input()
    return choice

def scene2A():
    print('You come to a stream with bridge')
    print('You can cross and follow the trail that leads from the bridge')
    print('or follow the trail that leads along the nearside of the river','\n')
    
def scene2B():
    print('You come to a steep hill')
    print('You can climb over the hill')
    print('or you can follow the trail which leads around it','\n')

#main program starts here
scene()

#use the makeChoice function to get the player to decide which way to go
firstChoice = makeChoice()
    
