from machines.display import *
from machines.character import *
from machines.map_nav import *
from machines.room_nav import *
from machines.battlestate import *
from machines.inventory import *
from machines.abilities import *
from machines.challenges import *
from machines.curiosities import *
from machines.allies import *
from machines.storyteller import *





def main():
    battlestate = 0
    shopstate = 0

    choiceA = mainMenu()
    if choiceA == 1:
        newGameIntro()
        classChoice = newPlayer()
        if classChoice == 1:
            player = character("Knight", 1, 20, 20, 5, 5, 5, 3, 1, 7, 3, 1, 1, 1, 1, 1, 1, 1, "", "", "", [], [], 0, 0, 11, 0, [], [])
        elif classChoice == 2:
            player = character("Hunter", 1, 16, 16, 8, 8, 3, 7, 3, 1, 5, 1, 1, 1, 1, 1, 1, 1, "", "", "", [], [], 0, 0, 11, 0, [], [])
        elif classChoice == 3:
            player = character("Scholar", 1, 12, 12, 12, 12, 1, 1, 7, 3, 3, 5, 1, 1, 1, 1, 1, 1, "", "", "", [], ["Blast Bolt"], 0, 0, 11, 0, [], [])
        starterKit(player)
        navigate(player)
        while battlestate == 0:
            if player.progress == 10 or player.progress == 20 or player.progress == 30 or player.progress == 40:
                    print(str(" _______________________________________________________________________ ").center(140))
                    print(str("|                                                                       |").center(140))
                    print(str("|     You've discovered a new map. Go to ' Travel ' to change maps.     |").center(140))
                    print(str("|_______________________________________________________________________|").center(140))
                    player.location = player.location + 1
            action = roomMenu(player)
            if action == "1":
                player.progress = player.progress + 1
                act = explore()
                if act == 0:
                    battlestate = 1
                elif act == 1:
                    challenge(player)
                elif act == 2:
                    conflict = curiosity(player)
                    if conflict == 1:
                        battlestate = 1
                elif act == 3:
                    ally(player)
                    # ALLY
                elif act == 4:
                    print("Quest")
                    # QUEST
            elif action == "2":
                showInventory(player)
                useInventory(player)
            elif action == "3":
                showAbilities(player)
                useAbilities(player)
            elif action == "4":
                showCharacter(player)
            elif action == "5":
                mapMenu(player)
            elif action == "6":
                battlestate = 1
            while battlestate == 1:
                result = battle(player, 1)
                if result == 0:
                    battlestate = 0
                else:
                    gameOver()


main()