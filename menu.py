import sys


# Making lists which contain possible actions for any given menu.

menus = {
    "main" : ["walk", "characters", "inventory", "quit"],
    "walk" : ["north", "east", "south", "west"],
    "characters" : ["john smith", "jane smith"],
    "inventory" : ["test item", "another test item"],
    "quit" : ["yes", "no"],
    }







# Making the menus work.
# Function to obtain user actions.
def user_action(section):
    """Accepts user input andd returns it to take an action. """
    s = section
    correction = "none"
    action_inp = input("Please enter an action to take: ")
    if action_inp not in menus[section]:
        correct = "no"
        attempts = 1
        while correct != "yes":
            if attempts == 1:
                print("That is not a valid option. Please try again")
            elif attempts > 1 and attempts <= 3:
                print("Sorry, this option is also incorrect. Please try again.")
            else:
                print("Ok, you must be joking. Please enter a VALID option.")
            display_menu(section)
            attempts += 1
            action_inp = input("Please enter an action to take: ")
            if action_inp in menus[section]:
                correct = 'yes'
                return action_inp
    #elif correction in menus[section]:
    #    return correction
    else:
        return action_inp


# function to display the menus when needed.
def display_menu(name):
    """displays your menu to the user."""
    menuvalues = menus[name]
    if name == "main":
        print("What would you like to do? ")
    elif name == "walk":
        print("Which direction would you like to go?")
    elif name == "characters":
        print("Which character would you like to interact with?")
    elif name == "inventory":
        print("Which item would you like to interact with?")
    elif name == "quit":
        print("Are you sure you want to quit?")
    [print(action.title()) for action in menuvalues]


# Function to go back to the main menu.
def main_menu():
    """For within other functions. Goes back to main menu."""
    display_menu("main")
    m = user_action("main")
    return m

def menu_actions(menu):
    """Allows the user to act in the menus."""
    menuvalues = menus[menu]
    if menu == "walk":
            display_menu("walk")
            direction = user_action("walk")
            if direction in menuvalues:
                print(f"You walk {direction}.")
            else:
                print("That is not a valid option. Please try again.")
                menu_actions("walk")
    elif menu == "characters":
        display_menu("characters")
        char = user_action()
        if char in menuvalues:
            print(f"You try and talk to {char}, but they are only a test character. So, you technically just talked to air.")
        else:
            print("Sorry, this is not a valid option. Please try again.")
            menu_actions("characters")
    elif menu == "inventory":
        display_menu("inventory")
        inv_inp = user_action("inventory")
        if inv_inp in menuvalues:
            print(f"You try to use {inv_inp}, but it isn't a real item.")
        else:
            print("Sorry, that's not an item in your inventory. Please try again.")
            menu_actions("inventory")
    elif menu == "quit":
        display_menu("quit")
        q = user_action("quit")
        if q == "yes":
            print("Ok, goodbye!")
            sys.exit()
        else:
            print("Ok, mission abort.")
            newAct = main_menu()
            menu_actions(newAct)
            
                

# Coding the endlesss menu.
while True:
    act = main_menu()
    menu_actions(act)