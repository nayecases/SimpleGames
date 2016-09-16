from player import Player
import utils.flavors_terminal as fla
from utils.read_text_file import read_firefly
from utils.custom_timer import CustomTimer as ct
import world, re, config, time


player = Player('Mal')

text_file = {'cap_conv_2':'resources/captain_conv_shoot.txt','end':'resources/ending.txt','cap_conv_1':'resources/introduce_captain.txt','intro':'resources/introduction.txt','mal_react':'resources/mal_reaction.txt',}

commands = {r'\bALIVE\b': 'isAlive', r'\bINVENTORY\b': 'printInventory', r'\bN\b':'moveNorth', r'\bNORTH\b':'moveNorth', r'\bS\b':'moveSouth', r'\bSOUTH\b':'moveSouth', r'\bE\b':'moveEast', r'\bEAST\b':'moveEast',
r'\bW\b':'moveWest', r'\bWEST\b':'moveWest', r'\bATTACK\b' : 'attack', r'\bINSULT\b':'insult', r'\bWHERE\b':'whereAmI', r'\bINVESTIGATE\b':'investigate', r'\bUSE\b':'use', r'\bTAKE\b':'take',
 r'\bSURRENDER\b':'surrender', r'\bHELP\b':'help', r'\bSTATUS\b':'status' }


def run():
    #Loads initial resources
    world.load_map()
    global player
    global runText

    #First intructions to player
    print_firefly_conv(text_file['intro'])

    player.whereAmI()

    #Start cycle
    while not player.runTime.get("END"):
        #print "Action:\n"
        getInput(True)


        #Checks if reached mid-game
        if player.runTime.get("TIMER") > player.runTime.get("ROUNDS_TIL_CAP") and not player.runTime.get("EXCHANGE"):
            print_firefly_conv(text_file['cap_conv_1'])
            print fla.con_y('Better go to the Cargo Bay to receive our guests...')
            #Comprobar que player esta en la bodega entonces exchange true
            if room_exists(player.locationX,player.locationY).__class__.__name__ == 'CargoBay':
                print_firefly_conv(text_file['cap_conv_2'])
                player.runTime["EXCHANGE"] = True
                if player.runTime["GUN"] :
                    print_firefly_conv(text_file['mal_react'])
                else:
                    player.health = 0

        if player.runTime['EXCHANGE']:
            loose_health()

        checkIfEnded()


    if player.runTime["RESULT"]:
        for line in read_firefly(text_file['end']): print line
    else:
        print fla.con_gray('Sorry... I tried')
        player.surrender()
        print "You collapse on the floor, forever drifting in space..."

def loose_health():
    global player
    player.cry()
    player.health = player.health - 30

def print_firefly_conv(file_path):
    for text in read_firefly(file_path):
        print text
        time.sleep(player.runTime.get("DIALOG_SLEEP"))
        getInput(False)


def getInput(ext):

    global player
    userActionRaw = raw_input(":  ")
    userAction = userActionRaw.split(" ")
    params= []
    found = False
    if len(userAction)>1:
        params = userAction[1:]
    #if re.match("t", userAction):
    for key in commands:
        if re.match(key, userAction[0].upper()) and ext:
            player.runTime["TIMER"] +=1
            found = True
            #print "pasa"
            try:
                res = getattr(player, commands[key])(*params)
            except TypeError:
                print fla.con_red( player.runTime.get("ERROR") + "," + " that's not how that's used...")
    if not found and ext:
        print fla.con_gray(player.runTime.get("ERROR"))



def checkIfEnded():
    global player
    if player.runTime.get("USED_CATALYZER") and player.runTime.get("BIG_DAMN_RED_BUTTON"):
        player.runTime["END"] = True
        player.runTime["RESULT"] = True
    elif player.health <=0 :
        player.runTime["END"] = True
        player.runTime["RESULT"] = False


run()
