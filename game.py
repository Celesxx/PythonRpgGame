#import cmd
#import textwrap
import sys
import os
import time
#import random

screen_width = 100


##### Setup du joueur ######

class player:
    def __init__(self):
        self.name = ''
        self.job = ''
        self.hp = 0
        self.mp = 0
        self.status_effects = []
        self.location = 'a4'
        self.game_over = False


myPlayer = player()


##### Title Screen #####
def tittle_screen_selection():
    option = input("> ")
    if option.lower() == "play":
        print("test play")
        setup_game()
    elif option.lower() == "help":
        help_menu()
    elif option.lower() == "quit":
        print("Vous avez quitté le jeu")
        sys.exit()
    while option.lower() not in ['play', 'help', 'quit']:
        print("Please enter a valid command.")
        option = input("> ")
        if option.lower() == "play":
            print("test play")
            setup_game()
        elif option.lower() == "help":
            help_menu()
        elif option.lower() == "quit":
            print("Vous avez quitté le jeu")
            sys.exit()


def title_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('##############################')
    print('# Welcome to the Text RPG ! #')
    print('##############################')
    print('      - Play -      ')
    print('      - Help -      ')
    print('      - Quit -      ')
    tittle_screen_selection()


def help_menu():
    print('##############################')
    print('# Welcome to the Text RPG ! #')
    print('##############################')
    print(' use up, down, left, right to move')
    print(' type you command to do them')
    tittle_screen_selection()


### Game fonction ###
def start_game():
    ##### Map #####
    """""
        a1  a2  a3  ..
        -----------------
        |   |   |   |   | a
        -----------------
        |   |   |   |   | b
        -----------------
        |   |   |   |   | c
        -----------------
        |   |   |   |   | d
        ----------------- 
        """""


ZONENAME = ''
DESCRIPTION = 'description'
EXAMINATION = 'examine'
SOLVED = False
UP = 'up', 'north'
DOWN = 'dow,', 'south'
LEFT = 'left', 'west'
RIGHT = 'right', 'east'

solved_places = \
    {
        'a1': False, 'a2': False, 'a3': False, 'a4': False,
        'b1': False, 'b2': False, 'b3': False, 'b4': False,
        'c1': False, 'c2': False, 'c3': False, 'c4': False,
        'd1': False, 'd2': False, 'd3': False, 'd4': False,
    }
zonemap = {
    'c1': {
        ZONENAME: 'Marché',
        DESCRIPTION: 'Le marché est remplis de marchand en tout genre, de quoi trouver votre bonheur',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'a1',
        DOWN: '',
        LEFT: '',
        RIGHT: '',
    },
    'c2': {
        ZONENAME: 'Entrée de la ville',
        DESCRIPTION: "c'est par cette et uniquement cette porte que l'on entre dans la ville",
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'a1',
        DOWN: '',
        LEFT: '',
        RIGHT: '',
    },
    'c3': {
        ZONENAME: 'Auberge',
        DESCRIPTION: 'Un lieu remplis de buveur et de voyageur venue ce reposer',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'a1',
        DOWN: '',
        LEFT: '',
        RIGHT: '',
    },
    'a4': {
        ZONENAME: 'Home',
        DESCRIPTION: 'This is you home',
        EXAMINATION: 'Your home looks the same - nothing has changed',
        SOLVED: False,
        UP: '',
        DOWN: 'b4',
        LEFT: 'a3',
        RIGHT: '',
    },
}

###### Game Interaction #####
def print_location():
    print("\n" + ('#' * (4 + len(myPlayer.location))))
    print('# ' + myPlayer.location.upper() + ' #')
    print('# ' + zonemap[myPlayer.location][DESCRIPTION] + ' #')
    print("\n" + ('#' * (4 + len(myPlayer.location))))

def prompt():
    print("Que veux-tu faire ?")
    action = input("> ")
    acceptable_actions = ['move', 'go', 'travel', 'walk', 'quit', 'examine', 'inspect', 'interact', 'look']
    while action.lower() not in acceptable_actions:
        print("Commande inconnue essayer de nouveau")
        action = input("> ")
    if action.lower() == 'quit':
        sys.exit()
    elif action.lower() == ['move', 'go', 'travel', 'walk']:
        player_move(action.lower())
    elif action.lower() == ['examine', 'inspect', 'interact', 'look']:
        player_examine(action.lower())

def player_move(myAction):
    ask = "Ou veux-tu te rendre ? \n"
    dest = input(ask)
    if dest in ['up', 'north']:
        destination = zonemap[myPlayer.location][UP]
        movement_handler(destination)
    elif dest in ['left', 'west']:
        destination = zonemap[myPlayer.location][LEFT]
        movement_handler(destination)
    elif dest in ['right', 'east']:
        destination = zonemap[myPlayer.location][RIGHT]
        movement_handler(destination)
    elif dest in ['down', 'south']:
        destination = zonemap[myPlayer.location][DOWN]
        movement_handler(destination)

def movement_handler(destination):
    print("\n" + "Vous vous déplacez à la destination : " + destination + " .")
    myPlayer.location = destination
    print_location()

def player_examine(action):
    if zonemap[myPlayer.location] [SOLVED]:
        print("Vous avez déja examiné la zone")
    else:
        print("\n" + "Vous trouvez un puzzle !")


##### Game fonction #####

def main_game_loop():
    while myPlayer.game_over is False:
        prompt()


def setup_game():
    os.system('cls' if os.name == 'nt' else 'clear')
    question1 = "Bonjour aventurier ! quel est ton nom ?\n"
    for character in question1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    player_name = input("> ")
    myPlayer.name = player_name

    question2 = "Bievenue dans le donjon " + myPlayer.name + " il faut choisir une classe maintenant !\n"
    question2added = "(tu à le choix entre : Guerrier, Mage, Voleur)\n"
    for character in question2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.02)
    for character in question2added:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.02)
    player_job = input("> ")
    valid_jobs = ['guerrier', 'mage', 'voleur']
    if player_job.lower() in valid_jobs:
        myPlayer.job = player_job
        print("Tu est maintenant un " + player_job + " ! \n")
    else:
        while player_job.lower() not in valid_jobs:
            player_job = input("> ")
            if player_job.lower() in valid_jobs:
                myPlayer.job = player_job
                print("Tu est maintenant un " + player_job + " ! \n")

    if myPlayer.job is 'Guerrier':
        myPlayer.hp = 120
        myPlayer.mp = 20
    elif myPlayer.job is 'Mage':
        myPlayer.hp = 40
        myPlayer.mp = 120
    elif myPlayer.job is 'Voleur':
        myPlayer.hp = 100
        myPlayer.mp = 50

    ### Introduction ######
    question3 = "Félicitation " + myPlayer.name + " grand " + myPlayer.job + " !\n"
    for character in question3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)

    speech1 = "Tu est maintenant prêt à affronter le grand donjon !\n"
    speech2 = "Il te faudra courage et force pour en venir à bout !\n"
    speech3 = "Bonne chance ahaha...\n"

    for character in speech1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.04)
    for character in speech2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.04)
    for character in speech3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.04)

    os.system('cls' if os.name == 'nt' else 'clear')
    print("##########################################")
    print("# Il est temps de commencer maintenant ! #")
    print("############################################")
    main_game_loop()

title_screen()