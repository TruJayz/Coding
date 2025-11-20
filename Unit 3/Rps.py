



'The game should be able allow u to choose between rock, paper, or scissor.'

'Then the program should choose rock, paper, or scissors randomly.'

'Then depending on the one you choose you could either win, lose, or tie.'







import random


def rpsGame():
    RpsGame_Cpu = ["rock, paper, scissor"]

    print("Welcome to Rock Paper Scissor the GAME")
    print('Please choose one of the following: enter P to start the game, or enter to rules')
    selection = input()
    if selection == 'r':
        print("here are the game rules... ")
    elif selection == 'p':
        print("The game is starting...")
        choiceUser = input("please make selction r= Rock, p= Paper, or s= Scissor!")
        ChoiceCpu = random.choice(RpsGame_Cpu)
        if choiceUser == 'r':
            selection
    else:
        print("Sorry, we didn't understand your entry!!!")





























