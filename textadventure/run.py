from player import Player
from utils.flavors_terminal import Flavors_terminal as term
import world, re, time


player = Player("Mal")


runText = {"introduction": "I can't believe I'm in this situation. Everything was going so well... I guess we were walking on eggshells. Now I'm here all alone, the crew left an hour ago. I'm just waiting for someone to pass by and maybe, lent my a hand. Ican't wait here any longer, it's driving me crazy. I should look around..."} #It's better in a separated file



commands = {r'\bALIVE\b': 'isAlive', r'\bINVENTORY\b': 'printInventory', r'\bN\b':'moveNorth', r'\bNORTH\b':'moveNorth', r'\bS\b':'moveSouth', r'\bSOUTH\b':'moveSouth', r'\bE\b':'moveEast', r'\bEAST\b':'moveEast',
r'\bW\b':'moveWest', r'\bWEST\b':'moveWest', r'\bATTACK\b' : 'attack', r'\bINSULT\b':'insult', r'\bWHERE\b':'whereAmI', r'\bINVESTIGATE\b':'investigate', r'\bUSE\b':'use', r'\bTAKE\b':'take',
 r'\bSURRENDER\b':'surrender', r'\bHELP\b':'help', r'\bSTATUS\b':'status' }

captainConv=[
    """There is someone calling. Better check it out, I'm in the pilot cabin... Hello?\n CAPTAIN - Firefly Serenity... This is the private salvage
S.S. Walden. Receiving your distress beacon, do you
read?\n""",
    """CAPTAIN - Right. Your mechanical trouble. Compression
coil, you say?""",
    """CAPTAIN - Not even the coil? Catalyzer's a nothing
part, Captain.""",
    """CAPTAIN - It is possible we might have something that'd
do you. We just come from a big salvage job off
Ita Moon. Picked the bones'a half a dozen junk heaps
not unlike the one you're sittin' in.I suppose we could dock, take a look around, see
if there ain't some way we might come to terms.
That's if we have the part --""",
    """CAPTAIN - Trouble is... how can I know for certain your
story's true? Ambush could be waiting for me and
my people on the other side.""",
    """CAPTAIN - (smiles)
I feel like maybe we can do business.""",
    """(Better go to the cargo bay to receive our guests...)"""
]
def run():
    world.load_map()

    global player
    global runText
    print runText["introduction"]
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
