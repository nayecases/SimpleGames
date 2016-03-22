from player import Player
from utils.flavors_terminal import Flavors_terminal as term
from utils.read_text_file import read_firefly
import world, re, time


player = Player("Mal")

text_file = {'cap_conv_2':'resources/captain_conv_shoot.txt','end':'resources/ending.txt','cap_conv_1':'resources/introduce_captain.txt','intro':'resources/introduction.txt','mal_react':'resources/mal_reaction.txt',}

commands = {r'\bALIVE\b': 'isAlive', r'\bINVENTORY\b': 'printInventory', r'\bN\b':'moveNorth', r'\bNORTH\b':'moveNorth', r'\bS\b':'moveSouth', r'\bSOUTH\b':'moveSouth', r'\bE\b':'moveEast', r'\bEAST\b':'moveEast',
r'\bW\b':'moveWest', r'\bWEST\b':'moveWest', r'\bATTACK\b' : 'attack', r'\bINSULT\b':'insult', r'\bWHERE\b':'whereAmI', r'\bINVESTIGATE\b':'investigate', r'\bUSE\b':'use', r'\bTAKE\b':'take',
 r'\bSURRENDER\b':'surrender', r'\bHELP\b':'help', r'\bSTATUS\b':'status' }


def run():
    world.load_map()

    global player
    global runText
        
    for l in read_firefly(text_file['intro']):
        print l

    player.whereAmI()
    while not player.runTime.get("end"):
        #print "Action:\n"
        getInput(True)
        checkIfEnded()
                #print res
        if player.runTime.get("timer") > player.runTime.get("roundsTilCapt") and not player.runTime.get("exchange"):
            player.locationX = 0
            player.locationY = 0
            for text in captainConv:
                print text
                time.sleep(player.runTime.get("secDialog"))
                getInput(False)

            player.runTime["exchange"] = True





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
            player.runTime["timer"] +=1
            found = True
            #print "pasa"
            try:
                res = getattr(player, commands[key])(*params)
            except TypeError:
                print term.ERROR + player.runTime.get("error") + "," + " that's not how that's used..." + term.ENDC
    if not found and ext:
        print player.runTime.get("error")



def checkIfEnded():
    global player
    if player.runTime.get("usedCatalyzer") and player.runTime.get("pressedButton"):
        player.runTime["end"] = True



run()
