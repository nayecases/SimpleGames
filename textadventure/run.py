from player import Player
import world, re, time


player = Player("Mal")

runTime = { "timer":0, "exchange": False, "usedCatalyzer": False, "pressedButton": False, "error" : "I don\'t understand that", "roundsTilCapt" : 15, "secDialog": 1}

runText = {"introduction": "bla bla"} #It's better in a separated file



commands = {r'\bALIVE\b': 'isAlive', r'\bINVENTORY\b': 'printInventory', r'\bN\b':'moveNorth', r'\bNORTH\b':'moveNorth', r'\bS\b':'moveSouth', r'\bSOUTH\b':'moveSouth', r'\bE\b':'moveEast', r'\bEAST\b':'moveEast',
r'\bW\b':'moveWest', r'\bWEST\b':'moveWest', r'\bATTACK\b' : 'attack', r'\bINSULT\b':'insult', r'\bWHERE\b':'whereAmI', r'\bINVESTIGATE\b':'investigate', r'\bUSE\b':'use', r'\bTAKE\b':'take',
 r'\bSURRENDER\b':'surrender', r'\bHELP\b':'help' }

def run():
    world.load_map()
    global runTime
    global player
    global runText
    print runText["introduction"]
    player.whereAmI()
    while not player.end:
        #print "Action:\n"
        getInput(True)
        checkIfEnded()
                #print res
        if runTime.get("timer") > runTime["roundsTilCapt"] and not runTime.get("exchange"):
            print """There is someone calling"""
            player.locationX = 0
            player.locationY = 0
            print """Better check it out, I'm in the pilot cabin... Hello?"""
            time.sleep(runTime["secDialog"])
            print """CAPTAIN - Firefly Serenity... This is the private salvage
S.S. Walden. Receiving your distress beacon, do you
read?"""
            time.sleep(runTime["secDialog"])
            getInput(False)
            time.sleep(runTime["secDialog"])
            print """CAPTAIN - Right. Your mechanical trouble. Compression
coil, you say?"""
            time.sleep(runTime["secDialog"])
            getInput(False)
            time.sleep(runTime["secDialog"])
            print """CAPTAIN - Not even the coil? Catalyzer's a nothing
part, Captain."""
            time.sleep(runTime["secDialog"])
            getInput(False)
            time.sleep(runTime["secDialog"])
            print """CAPTAIN - It is possible we might have something that'd
do you. We just come from a big salvage job off
Ita Moon. Picked the bones'a half a dozen junk heaps
not unlike the one you're sittin' in.I suppose we could dock, take a look around, see
if there ain't some way we might come to terms.
That's if we have the part --"""
            time.sleep(runTime["secDialog"])
            getInput(False)
            time.sleep(runTime["secDialog"])
            print """CAPTAIN - Trouble is... how can I know for certain your
story's true? Ambush could be waiting for me and
my people on the other side."""
            time.sleep(runTime["secDialog"])
            getInput(False)
            time.sleep(runTime["secDialog"])
            print """CAPTAIN - (smiles)
I feel like maybe we can do business."""
            time.sleep(runTime["secDialog"])
            print """(Better go to the cargo bay to receive our guests...)"""
            runTime["exchange"] = True




def getInput(ext):
    global runTime
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
            runTime["timer"] +=1
            found = True
            #print "pasa"
            try:
                res = getattr(player, commands[key])(*params)
            except TypeError:
                print runTime["error"] + "," + " that's not how that's used..."
    if not found:
        print runTime["error"]



def checkIfEnded():
    global player
    global runTime
    if runTime.get("usedCatalyzer") and runTime.get("pressedButton"):
        player.end = True


run()
