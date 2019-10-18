#imports
import random
import sys
import os
from time import sleep


class Character:
    """Class for holding general character information, this will be used for both the hero and enemies"""
    def __init__(self,hp=1,status=None,inventory=[],active_weapon={}):
        self.hp = hp
        self.status = status
        self.inventory = inventory
        self.active_weapon = active_weapon

class Hero(Character):
    """Additional stats and such for the hero"""
    pass

class Enemy(Character):
    """Additional stats and such for the Enemies"""
    pass

#A practice character playing around with for the sake of testing functionality
Merlyn = Character(hp=20,status = None,inventory=['apple','pair of socks','mysterious gem','old sword'], active_weapon={'old sword': '6'})
#Dummy story to test the text scrolling
story = 'You wake up in a dark dank room with no windows and only one door. You hear people speaking outside the door but are unable to make out what they are saying '
story1 = "You do nothing, and nothing happens"
story2 = 'You look around and find a dirty nail on the floor'
story3 = 'The men outside the door are discussing the latest football game'
story4 = 'You open the door and are immediatley struck down by the men outide'

story_array = [
    [
        "You do nothing,and nothing happens",
        'You look around and find a dirty nail on the floor',
        'The men outside the door are discussing the latest football game',
        'You open the door and are immediatley struck down by the men outide'
    ],
    [
        '1 longer text',
        '2 longer text',
        '3 longer text',
        '4 longer text'
    ],
    [
        '1-2 longer text',
        '2-2 longer text',
        '3-2 longer text',
        '4-2 longer text'
    ]
]


#Dummy choices for testing choice functionality
initial_choices = ['Do nothing', 'Look around', 'Listen at the door', 'Open the door']
#Choices after initial Choices
#April 4th, So the choices and text work on a multidimensional array pulls from incrementing arrays
#This way I'm able to use the same function recursively as to not over clutter and over complicate the project
choices_array = [
    [
        ['Do nothing', 'Look around', 'Listen at the door', 'Open the door'],
        ['1','2','3','4'],
        ['one','two','three','four'],
        ['ein','zwei','drei','weir']
    ],
    [
        ['Dance','Go for brunch', 'Thrive', 'Trivia night'],
        ['1','2','3','4'],
        ['one','two','three','four'],
        ['ein','zwei','drei','weir']
    ],
    [
        ['test1','test2','test3'],
        ['turtles','orange','money','roosters'],
        ['one','two','three','four'],
        ['ein','zwei','drei','weir']
    ],
    [
        ['Taako Taco','text','text','whoop'],
        ['Magnus Burnsides','Julia','Johnson','Jwoo'],
        ['Merle Highchurch','Goober','sweedle','hoot hoot'],
        ['Captain Captain Bane','The Raven','Harley','Yeah true']
    ]
]
choices_number = 0
story_number = 0

#clears the console/terminal to keep from cluttering
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def display_menu(story, choice):
#Displays the menu with access to character information and game quit
    print('Menu Items\n')
    print('-'*25+'\n')
    print('C) Character screen')
    print('E) Exit Menu')
    print('Q) Quit game')

    menu_input = raw_input('[C/E/Q]: ').upper()

    if menu_input == "C":
        character_info(Merlyn)
    elif menu_input =="E":
        clear()
        display_no_scroll(story, choice)
    elif menu_input =="Q":
        clear()
        exit()


def character_info(player):
    """Overview of character HP, status effects, inventory items, and currently equiped weapons"""
    clear()
    print('-'*75+'\n')
    print('HP:{}'.format(player.hp)+'\n')
    print('Status:{}'.format(player.status)+'\n')
    print('Inventory Items')
    print('-'*25+'\n')
    for index, item in enumerate(player.inventory):
        print("{} ) {}"+'\n').format(index+1,item)
    for weapon in player.active_weapon:
            for weaponDmg in player.active_weapon[weapon]:
                print("You have a(n) {} as your primary weapon, it can do a max of {} damage!"+'\n').format(weapon,weaponDmg)

    #Return to the story screen
    character_info_input = raw_input('Press "B" to return to menu: ').upper()
    if character_info_input =='B':
        clear()
        display_menu(story,choices_array[choices_number][0])

def write_text_scroll(text):
    """This class is used for the scrolling text, Will only be used for the initial instance of each text screen"""
    for char in text:
        sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()

def display_no_scroll(story,choice):
    """this is used for other instances passed the first for writing story to the screen"""
    print('-'*75)
    print('\n')
    print(story)
    print('\n')
    display_choices(choice)
    initial_input = raw_input('Press "[1/2/3/4]" to enter your choice or press "M" to access the menu: ').upper()
    if initial_input == "M":
        clear()
        display_menu(story1,choices_array[choices_number][0])
    elif initial_input == "1":
        clear()
        display_screen(story1,choices_array[choices_number][0])
    elif initial_input == "2":
        clear()
        display_screen(story2,choices_array[choices_number][1])
    elif initial_input == "3":
        clear()
        display_screen(story3,choices_array[choices_number][2])
    elif initial_input == "4":
        clear()
        display_screen(story4,choices_array[choices_number][3])
    print('-'*75)


def display_choices(choice_list):
    for index, choice in enumerate(choice_list):
        print('{} ) {} \n').format(index +1,choice)

def display_screen(story, choice):
    global choices_number
    global story_number
    clear()
    write_text_scroll(story)
    print('\n')
    display_choices(choice)
    screen_input = raw_input('Press "[1/2/3/4]" to enter your choice or press "M" to access the menu: ').upper()
    if screen_input == "M":
        clear()
        display_menu(story_array[0],choices_array[choices_number][0])
    elif screen_input == "1":
        clear()
        change_story()
        change_number()
        display_screen(story_array[story_number][0],choices_array[choices_number][0])
    elif screen_input == "2":
        clear()
        change_story()
        change_number()
        display_screen(story_array[story_number][1],choices_array[choices_number][1])
    elif screen_input == "3":
        clear()
        change_story()
        change_number()
        display_screen(story_array[story_number][2],choices_array[choices_number][2])
    elif screen_input == "4":
        clear()
        change_story()
        change_number()
        display_screen(story_array[story_number][3],choices_array[choices_number][3])


def change_number():
    global choices_number
    choices_number = choices_number + 1
    return choices_number

def change_story():
    global story_number
    story_number = story_number + 1
    return story_number

def display_initial_screen():
    """
        This is the inital screen that's called when the game is booted up
        I may end up changing this one around for a more standard start screen
        with a begin game button and such
    """
    print('-'*75)
    print('\n')
    write_text_scroll(story)
    print('\n')
    display_choices(initial_choices)
    #Option to get to menu
    initial_input = raw_input('Press "[1/2/3/4]" to enter your choice or press "M" to access the menu: ').upper()
    if initial_input == "M":
        clear()
        display_menu(story, initial_choices)
    elif initial_input == "1":
        display_screen(story1,choices_array[choices_number][0])
    elif initial_input == "2":
        display_screen(story2,choices_array[choices_number][1])
    elif initial_input == "3":
        display_screen(story3,choices_array[choices_number][2])
    elif initial_input == "4":
        display_screen(story4,choices_array[choices_number][3])
    print('-'*75)

display_initial_screen()

#DONT DELETE THIS
# import sys
# from time import sleep
#
# words = "This is just a test :P"
# for char in words:
#     sleep(0.1)
#     sys.stdout.write(char)
#     sys.stdout.flush()
# This script makes it so that the text doesn't display all at once
# but will look as though it's being typed out
