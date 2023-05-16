def render_introduction():
    '''
    Create the message to be displayed at the start of your game.

    Returns:
        str: The introductory text of your game to be displayed.
    '''
    return ''' Your a vetran police officer sent to Lifted Acorn Elderly
care to investigate a missing patient.
    According to the report, the convealesent put everyone to bed
at the regular 7pm, and as far as the employees were concerned the night wen without issue. However the
next morning Ms.Poof was not in her bed. The was no note or signs of struggle and furthmore
the doors and windows remained locked throughout the night. The closed off wing of the home
has three rooms currently occupied, visit each and fill out your report. You can return to the precienct
from the lobby when you are ready.'''

def create_player():
    return {"location":"lobby",
            "inventory": []
            }
def create_map():
    return {
            "lobby":{
                "neighbors": ["room 206","room 209","room 207","precinct"],
                "about":'''You walk into the lobby, the employee from the night before
                    is there looking nervous, standing by a messy desk''',
                "stuff": ["speak to employee","search desk"]
                },
            "room 206":{
                "neighbors": ["room 209","room 207","lobby"],
                "about":'''Two elderly ladies sit on there beds, Ms.Starg looking blankly into space
                    while Ms.Eckers mumbles at her.''',
                "stuff": ["speak to Ms.Starg","speak to Ms.Eckers","search the room",]
                },
            "room 209":{
                "neighbors": ["room 206","room 207","lobby","outside"],
                "about":'''This is the room of the missing woman.
                    Her roomate, Ms.Braker, now sits in bed with the TV blaring a Shirly Temple movie.
                    The window is open and you can see the groundskeeper raking up leaves. As you were coming
                    in you noticed a exit, next door, that led to were he was at and took note''',
                "stuff": ["speak to Ms.Braker","search Ms.Poof's bed","turn off the tv"]
                },
            "outside":{
                "neighbors": ["room 206","room 207","room 209" "lobby"],
                "about":'''You aproach the groundskeeper, he sees you
                and he tries to go about his business, prettending not to notice''',
                "stuff": ["chase him down","yell for him","say STOP POLICE!"]
                },
            "room 207":{
                "neighbors": ["room 206","room 209","lobby"],
                "about":'''Inside the room is Mrs.Gubler , sobbing, and her roomate, Ms.Neffer
                    who is laying down, with pillows covering her ears''',
                "stuff": ["speak to Mrs.Gubler","speak to Ms.Neffer","look around"]
                }
            }
def create_world():
    '''
    Creates a new version of the world in its initial state.

    Returns:
        World: The initial state of the world
    '''
    return {
        "status": "playing",
        "map": create_map(),
        'player':create_player(),
        }
    
def render(world):
    '''
    Consumes a world and produces a string that will describe the current state
    of the world. Does not print.

    Args:
        world (World): The current world to describe.

    Returns:
        str: A textual description of the world.
    '''
    player_location = world['player']['location']
    return world["map"][player_location]["about"]
def get_options(world):
    '''
    Consumes a world and produces a list of strings representing the options
    that are available to be chosen given this state.

    Args:
        world (World): The current world to get options for.

    Returns:
        list[str]: The list of commands that the user can choose from.
    '''
    commands = ["quit"]
    player_location = world['player']['location']
    player_inventory = world["player"]["inventory"]
    stuff = world ["map"][player_location]["stuff"]
    neighbors = world ["map"][player_location]['neighbors']
    for neighbor in neighbors:
        commands.append("goto "+neighbor)
    for item in stuff:
        commands.append(item)
    return commands

def update(world, command):
    '''
    Consumes a world and a command and updates the world according to the
    command, also producing a message about the update that occurred. This
    function should modify the world given, not produce a new one.

    Args:
        world (World): The current world to modify.

    Returns:
        str: A message describing the change that occurred in the world.
    '''
    player_location = world['player']['location']
    player_inventory = world['player']['inventory']
    stuff = world['map'][player_location]['stuff']
    if command == "quit":
        world ['status'] = 'quit'
        return "You gave up!"
    if command == "goto room 206":
        world['player']['location']='room 206'
    if command == 'speak to Ms.Starg':
        stuff.remove('speak to Ms.Starg')
        player_inventory.append('speak to Ms.Starg')
        return("""Ms. Starg informs you that she heard a low bass, that she assumed was
        a kids car. She then trails off about her grandkids.
    You add Ms.Stargs statement to your report!""")
    if command == 'speak to Ms.Eckers':
        stuff.remove('speak to Ms.Eckers')
        player_inventory.append('speak to Ms.Eckers')
        return("""Ms. Eckers turn her attention to you and continues her train of thought about
    the type of pudding the food hall.
        She is no help.""")
    if command == 'search the room':
        stuff.remove('search the room')
        player_inventory.append('search the room')
        return("""You find nothing but some soggy pills.""")
    
    if command == "goto room 207":
        world['player']['location']='room 207'
    if command == 'speak to Mrs.Gubler':
        stuff.remove('speak to Mrs.Gubler')
        player_inventory.append('speak to Mrs.Gubler')
        return("""Mrs.Gubler cries over your questions, when she does answer
        you learn although she didnt know the missing women, she is just sad about the situition...
        and probely just wants attention""")
    if command == 'speak to Ms.Neffer':
        stuff.remove('speak to Ms.Neffer')
        player_inventory.append('speak to Ms.Neffer')
        return("""Ms.Neffer didnt see or hear anything, she is however sure Mrs.Gubler is
        just starved for attention""")
    if command == "look around":
        stuff.remove("look around")
        player_inventory.append("look around")
        return("""You find nothing but a returned letter originally sent to Mrs.Gublers grandkids""")
    
    if command == "goto room 209":
        world['player']['location']='room 209'
    if command == 'speak to Ms.Braker':
        stuff.remove('speak to Ms.Braker')
        player_inventory.append('speak to Ms.Braker')
        return("""You have to yell over the tv, but you are able to learn that Braker though she saw
        saw the missing patient jumping on the bed, however she didnt have her glasses on, and
        and she could have swore she was jumping in slow motion
        You add Ms.Braker's statement to your report!""")
    if command == "turn off the tv":
        stuff.remove('speak to Ms.Braker')
        stuff.remove('turn off the tv')
        player_inventory.append('turn off the tv')
        return("""As soon as you turn off Animal Crackers Ms.Braker starts screaming.
    You better leave!""")
    if command == "search Ms.Poof's bed":
        stuff.remove("search Ms.Poof's bed")
        player_inventory.append("search Ms.Poof's bed")
        return("""You find nothing, but it smells like sulfer.""")
    if command == "goto outside":
        world['player']['location']='outside'
    if command == 'chase him down':
        stuff.remove('say STOP POLICE!')
        stuff.remove('chase him down')
        stuff.remove('yell for him')
        player_inventory.append('chase him down')
        return("""when you chase him down, cornered He says : If I tell you, you can't tell anyone else here!
                    ok you say, confused
                    He begins confessing to have witnessed a large craft above the home during the night
                    which emmitted a blue and green light, it woke him from his bunk across from the home.
                    He thought maybe he was losing or his meds were acting up.
                    You add that to the report""")
    if command == 'yell for him':
        stuff.remove('yell for him')
        player_inventory.append('yell for him')
        return("""The groundskeeper picks up a leafblower and turns it on, drowning out your lazy
        commands""")
    if command == "say STOP POLICE!":
        stuff.remove('chase him down')
        stuff.remove('yell for him')
        stuff.remove('say STOP POLICE!')
        player_inventory.append('say STOP POLICE!')
        return("""The groundskeeper jumps, comes towards you and asks if he is under arrest
        you answer no
        he says: then im not saying anything
        and walks away""")
    if command == "goto lobby":
        world['player']['location']='lobby'
    
    if command == 'speak to employee':
        stuff.remove('speak to employee')
        player_inventory.append('speak to employee')
        return("""The underpaid worker doesnt have much to say and
                    is mostly worried about being fired""")
    if command == 'search desk':
        stuff.remove('search desk')
        player_inventory.append('search desk')
        return("""You find a bunch of medical records, pens,
        a doodle of a... rocket ship...I think and a newspaper.
        The newspapers headline reads Lights over town, Airforce says an investigation is
        underway, lets add that to the report.
                """)
    if command == "goto precinct":
        if 'speak to Ms.Starg' and 'search desk' and 'chase him down' and "speak to Ms.Braker" in player_inventory:
            world['status'] = 'win'
            return("""You leave the home, knowing your report is going to turn some heads.
            Sure enough the boss isnt happy you blamed the whole thing on aliens, and you spend the rest
            of your career in a basement closet they converted to an office, and are only given the strange
            cases. However you now have a life quest to dedicate yourself to: proving that space aliens are among us.
             (and answering the question of Why would they want old people?)""")
        else:
            world['status'] = 'lose'
            return("""You turn in your report with no conclusive reason for the disapearence.
            The family eventually sues the home, and your career goes belly up because of your shoddy work.
            Your marrige falls apart, (and your kid call you by your first name, when they do call you)""")
    return "unkown command: "+command
    
def render_ending(world):
    '''
    Create the message to be displayed at the end of your game.

    Args:
        world (World): The final world state to use in describing the ending.

    Returns:
        str: The ending text of your game to be displayed.
    '''
    return "Thanks for Playing! The Truth is Out There!"
     

def choose(options):
    '''
    Consumes a list of commands, prints them for the user, takes in user input
    for the command that the user wants (prompting repeatedly until a valid
    command is chosen), and then returns the command that was chosen.

    Note:
        Use your answer to Programming Problem #42.3

    Args:
        options (list[str]): The potential commands to select from.

    Returns:
        str: The command that was selected by the user.
    '''
    print ("You can: ")
    for option in options:
        print(option)
    choice = ""
    while choice not in options:
        choice = input("What will you do? ")
    return(choice)  
############# Main Function ##############
# Do not modify anything below this line #
##########################################
def main():
    '''
    Run your game using the Text Adventure console engine.
    Consumes and produces nothing, but prints and indirectly takes user input.
    '''
    print(render_introduction())
    world = create_world()
    
    while world['status'] == 'playing':
        print(render(world))
        options = get_options(world)
        command = choose(options)
        print(update(world, command))
    print(render_ending(world))

if __name__ == '__main__':
    main()
