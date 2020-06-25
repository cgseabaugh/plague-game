

def tellerLoc(player):
    location = player.location
    if location == 11 or location == 12 or location == 13 or location == 14 or location == 15:
        woodsTellerTree(player)
    elif location == 22 or location == 23 or location == 24 or location == 25:
        print("Teller")
    elif location == 33 or location == 34 or location == 35:
        print("Teller")
    elif location == 44 or location == 45:
        print("Teller")
    elif location == 55:
        print("Teller")

def woodsTellerTree(player):
    teller = 1
    while teller == 1:
        woodsTeller()
        a = input(str(":  ").rjust(60))
        if a == "1":
            woodsTeller1()
            b = input(str(":  ").rjust(60))
            if b == "1":
                woodsTeller1a()
                woodsTellerEnd()
                tellerInsight(player)
                teller = 0
            elif b == "2":
                woodsTeller1b()
                woodsTellerEnd()
                tellerInsight(player)
                teller = 0
            elif b == "3":
                woodsTeller1c()
                woodsTellerEnd()
                tellerInsight(player)
                teller = 0
            elif b == "4":
                woodsTellerEnd()
        elif a == "2":
            woodsTeller2()
            c = input(str(":  ").rjust(60))
            if c == "1":
                woodsTeller2a()
                woodsTellerEnd()
                tellerInsight(player)
                teller = 0
            elif c == "2":
                woodsTeller2b()
                woodsTellerEnd()
                tellerInsight(player)
                teller = 0
            elif c == "3":
                woodsTeller2c()
                woodsTellerEnd()
                tellerInsight(player)
                teller = 0
            elif c == "4":
                woodsTellerEnd()
        elif a == "3":
            woodsTeller3()
            d = input(str(":  ").rjust(60))
            if d == "1":
                woodsTeller3a()
                woodsTellerEnd()
                tellerInsight(player)
                teller = 0
            elif d == "2":
                woodsTeller3b()
                woodsTellerEnd()
                tellerInsight(player)
                teller = 0
            elif d == "3":
                woodsTeller3c()
                woodsTellerEnd()
                tellerInsight(player)
                teller = 0
            elif d == "4":
                woodsTellerEnd()
        elif a == "4":
            woodsTellerEnd()

def tellerInsight(player):
    print(str(" __________________________________________________________________________________ ").center(140))
    print(str("|                                                                                  |").center(140))
    print(str("|     By listening to the blind man, your knowledge of the world has deepened.     |").center(140))
    print(str("|                                 _________________                                |").center(140))
    print(str("|                                |   + 1 Insight   |                               |").center(140))
    print(str("|                                 `````````````````                                |").center(140))
    print(str("|__________________________________________________________________________________|").center(140))
    player.insight = player.insight + 1

def woodsTeller():
    print(str(" ________________________________________________________________________________________ ").center(140))
    print(str("|                                                                                        |").center(140))
    print(str("|          You spot an old man perched meditatively atop a petrified stump. He wears     |").center(140))
    print(str("|     soiled, matted robes, ornamented with strange bobbles and charms. The man turns    |").center(140))
    print(str("|     to you, instantly aware of your presence. A bloodied cloth wrapped tightly         |").center(140))
    print(str("|     around his eyes tells of his blindness.                                            |").center(140))
    print(str("|                                                                                        |").center(140))
    print(str("|                                                                                        |").center(140))
    print(str("|       '' And so, another arrives from some distant land, just like the others. ''      |").center(140))
    print(str("|                                                                                        |").center(140))
    print(str("|                 '' Have you, too, come to put an end to the madness? ''                |").center(140))
    print(str("|                                                                                        |").center(140))
    print(str("|             '' At last, my body fails me. I am not long for this world... ''           |").center(140))
    print(str("|                                                                                        |").center(140))
    print(str("|            '' I could have done more. Though I may be of some use yet. ''              |").center(140))
    print(str("|                                                                                        |").center(140))
    print(str("|          '' I have knowledge, many centuries worth, if you care to ask. ''             |").center(140))
    print(str("|                                                                                        |").center(140))
    print(str("|            _______________________________________________________________             |").center(140))
    print(str("|           |                                                               |            |").center(140))
    print(str("|           |     Is there anything you care to ask the old, blind man?     |            |").center(140))
    print(str("|           |          ____________________________________________         |            |").center(140))
    print(str("|           |         | 1 |   What is the Pale Plague?             |        |            |").center(140))
    print(str("|           |         | 2 |   What do you know about the cure?     |        |            |").center(140))
    print(str("|           |         | 3 |   Who are you, and why are you here?   |        |            |").center(140))
    print(str("|           |         | 4 |   Ask nothing.                         |        |            |").center(140))
    print(str("|           |          ````````````````````````````````````````````         |            |").center(140))
    print(str("|           |_______________________________________________________________|            |").center(140))
    print(str("|                                                                                        |").center(140))
    print(str("|________________________________________________________________________________________|").center(140))

def woodsTeller1():
    print(str(" ________________________________________________________________________________________ ").center(140))
    print(str("|                                                                                        |").center(140))
    print(str("|      '' An insideous creature. It clings to the fould winds and to everything ''       |").center(140))
    print(str("|                                                                                        |").center(140))
    print(str("|       '' it touches. You have lost loved ones to the fiend? As have we all. ''         |").center(140))
    print(str("|                                                                                        |").center(140))
    print(str("|      '' It eats the spirit and makes a home in its absence. Surely you've seen ''      |").center(140))
    print(str("|                                                                                        |").center(140))
    print(str("|      '' what remains? If it cannot be stopped, there will be nothing left. ''          |").center(140))
    print(str("|                                                                                        |").center(140))
    print(str("|     '' No further cycles. No second chances. For mankind, it will be the end. ''       |").center(140))
    print(str("|                           __________________________________                           |").center(140))
    print(str("|                          | 1 |   Where does it come from?   |                          |").center(140))
    print(str("|                          | 2 |   What remains?              |                          |").center(140))
    print(str("|                          | 3 |   The end?                   |                          |").center(140))
    print(str("|                          | 4 |   Ask nothing else.          |                          |").center(140))
    print(str("|                           ``````````````````````````````````                           |").center(140))
    print(str("|________________________________________________________________________________________|").center(140))

def woodsTeller2():
    print(str(" ________________________________________________________________________________________ ").center(140))
    print(str("|                                                                                        |").center(140))
    print(str("|     '' Oh, that wretched thing. Do seek it, if you must. The very bravest have. ''     |").center(140))
    print(str("|                                                                                        |").center(140))
    print(str("|        '' But when you reach the city, you will behold many a brave corpse. ''         |").center(140))
    print(str("|                                                                                        |").center(140))
    print(str("|     '' The Ministry of Medicine worked in secret with the Church and found... ''       |").center(140))
    print(str("|                                                                                        |").center(140))
    print(str("|     '' Something. A cure? I do not know, but if such a thing existed, it could ''      |").center(140))
    print(str("|                                                                                        |").center(140))
    print(str("|                           '' save us from the end. ''                                  |").center(140))
    print(str("|                                                                                        |").center(140))
    print(str("|                     ___________________________________________                        |").center(140))
    print(str("|                    | 1 |   What is the Ministry of Medicine?   |                       |").center(140))
    print(str("|                    | 2 |   What role did the Church play?      |                       |").center(140))
    print(str("|                    | 3 |   The end?                            |                       |").center(140))
    print(str("|                    | 4 |   Ask nothing else?                   |                       |").center(140))
    print(str("|                     ```````````````````````````````````````````                        |").center(140))
    print(str("|________________________________________________________________________________________|").center(140))

def woodsTeller3():
    print(str(" ________________________________________________________________________________________ ").center(140))
    print(str("|                                                                                        |").center(140))
    print(str("|                                                                                        |").center(140))
    print(str("|       '' I am a wavering light in these dark times. Too long have I held this ''       |").center(140))
    print(str("|                                                                                        |").center(140))
    print(str("|       '' sorry flame. Centuries? Millenia? Time has become convoluted to me. ''        |").center(140))
    print(str("|                                                                                        |").center(140))
    print(str("|       '' At last, I can forstall the end no longer. I will be swallowed soon. ''       |").center(140))
    print(str("|                                                                                        |").center(140))
    print(str("|      '' How pitiful, my fire. Perhaps I might yet be able to ignite another's. ''      |").center(140))
    print(str("|                                                                                        |").center(140))
    print(str("|                            ____________________________                                |").center(140))
    print(str("|                           | 1 |   How old are you?     |                               |").center(140))
    print(str("|                           | 2 |   The end?             |                               |").center(140))
    print(str("|                           | 3 |   Swallowed by what?   |                               |").center(140))
    print(str("|                           | 4 |   Ask nothing else.    |                               |").center(140))
    print(str("|                            ````````````````````````````                                |").center(140))
    print(str("|________________________________________________________________________________________|").center(140))

def woodsTeller1a():
    print(str(" ________________________________________________________________________________________ ").center(140))
    print(str("|                                                                                        |").center(140))
    print(str("|      '' It rose from a deep and dark place, a consequence of the sins of your ''       |").center(140))
    print(str("|                                                                                        |").center(140))
    print(str("|    '' forefathers. We stood so tall, our meek species. Tall enough, we believed, ''    |").center(140))
    print(str("|                                                                                        |").center(140))
    print(str("|     '' to break the cycle. Death had lost meaning, and this plague came to fill ''     |").center(140))
    print(str("|                                                                                        |").center(140))
    print(str("|                 '' the void. Afterall, nature abhores a vacuum.  ''                    |").center(140))
    print(str("|                                                                                        |").center(140))
    print(str("|________________________________________________________________________________________|").center(140))

def woodsTeller1b():
    print(str(" ________________________________________________________________________________________ ").center(140))
    print(str("|                                                                                        |").center(140))
    print(str("|      '' Those withered things, hollowed of everything but the flesh. They are ''       |").center(140))
    print(str("|                                                                                        |").center(140))
    print(str("|        '' vessels now, expired of spirit and pulled along by unseen forces. ''         |").center(140))
    print(str("|                                                                                        |").center(140))
    print(str("|        '' How they stare listlessly into the sky, devoid of want and will. ''          |").center(140))
    print(str("|                                                                                        |").center(140))
    print(str("|       '' I can only say that they are listening to something deep within the ''        |").center(140))
    print(str("|                                                                                        |").center(140))
    print(str("|                    '' cosmos. To what? I hope never to know. ''                        |").center(140))
    print(str("|                                                                                        |").center(140))
    print(str("|________________________________________________________________________________________|").center(140))

def woodsTeller1c():
    print(str(" ________________________________________________________________________________________ ").center(140))
    print(str("|                                                                                        |").center(140))
    print(str("|     '' The end of it all; the running empty of the cycles of man. A great flood ''     |").center(140))
    print(str("|                                                                                        |").center(140))
    print(str("|     '' that took many forms, bringing a transcending humanity back to its roots. ''    |").center(140))
    print(str("|                                                                                        |").center(140))
    print(str("|    '' We so feared its coming once we learned of it that we broke the very cycle ''    |").center(140))
    print(str("|                                                                                        |").center(140))
    print(str("|    '' that ushered it in. And look where we are not! The end comes with no regard ''   |").center(140))
    print(str("|                                                                                        |").center(140))
    print(str("|    '' for our protests. All we learned was that the cycle did not bring the end, ''    |").center(140))
    print(str("|                                                                                        |").center(140))
    print(str("|                                    '' but our rebirth. ''                              |").center(140))
    print(str("|                                                                                        |").center(140))
    print(str("|________________________________________________________________________________________|").center(140))

def woodsTeller2a():
    print(str(" ________________________________________________________________________________________ ").center(140))
    print(str("|                                                                                        |").center(140))
    print(str("|     '' A carnival of good intentions. They play with sciences for which they are ''    |").center(140))
    print(str("|                                                                                        |").center(140))
    print(str("|  '' ill-suited. Their antiquated practices have little utility beyond the ritual. ''   |").center(140))
    print(str("|                                                                                        |").center(140))
    print(str("|       '' They have amassed a wealth of knowledge, stolen from the dead cities. ''      |").center(140))
    print(str("|                                                                                        |").center(140))
    print(str("|          '' It has lead to as many tragedies as victories over the years. ''           |").center(140))
    print(str("|                                                                                        |").center(140))
    print(str("|        '' Whether or not they've done humanity any favors remains to be seen. ''       |").center(140))
    print(str("|                                                                                        |").center(140))
    print(str("|________________________________________________________________________________________|").center(140))

def woodsTeller2b():
    print(str(" ________________________________________________________________________________________ ").center(140))
    print(str("|                                                                                        |").center(140))
    print(str("|      '' Their role has always been the same. Cherished rescuers of humanity. ''        |").center(140))
    print(str("|                                                                                        |").center(140))
    print(str("|     '' Or so they have insisted. Their attempts are noble, but have often taken ''     |").center(140))
    print(str("|                                                                                        |").center(140))
    print(str("|     '' dark turns. Each cycle, they risk becoming the demons that they battle. ''      |").center(140))
    print(str("|                                                                                        |").center(140))
    print(str("|      '' True enough that this dying world was delivered to man by the church. ''       |").center(140))
    print(str("|                                                                                        |").center(140))
    print(str("| '' Truer still, man would not have made it so long without their... interventions. ''  |").center(140))
    print(str("|                                                                                        |").center(140))
    print(str("|________________________________________________________________________________________|").center(140))
    
def woodsTeller2c():
    woodsTeller1c()

def woodsTeller3a():
    print(str(" ________________________________________________________________________________________ ").center(140))
    print(str("|                                                                                        |").center(140))
    print(str("|      '' I wonder that myself, sometimes. The years fold together so seamlessly. ''     |").center(140))
    print(str("|                                                                                        |").center(140))
    print(str("|      '' Once I measured time by the rising and falling of nations. And then by ''      |").center(140))
    print(str("|                                                                                        |").center(140))
    print(str("|         '' the very cycles of humanity itself. But we broke those long ago. ''         |").center(140))
    print(str("|                                                                                        |").center(140))
    print(str("|                          '' Now, how am I ever to know? ''                             |").center(140))
    print(str("|                                                                                        |").center(140))
    print(str("|________________________________________________________________________________________|").center(140))

def woodsTeller3b():
    woodsTeller1c()

def woodsTeller3c():
    print(str(" ________________________________________________________________________________________ ").center(140))
    print(str("|                                                                                        |").center(140))
    print(str("|     '' You and I are not alike. We fear a very different oblivion. If you are, ''      |").center(140))
    print(str("|                                                                                        |").center(140))
    print(str("|      '' then your death is not, and when your death is, you are not. Mine is a ''      |").center(140))
    print(str("|                                                                                        |").center(140))
    print(str("|     '' slow and insideous thing. Each day my very being is more foreign to me. ''      |").center(140))
    print(str("|                                                                                        |").center(140))
    print(str("|  '' But a deep and dark thing has gripped me, and it must be fed if I am to remain ''  |").center(140))
    print(str("|                                                                                        |").center(140))
    print(str("|    '' more than just a vessel. It hungers, even now. And it will devour me, as I ''    |").center(140))
    print(str("|                                                                                        |").center(140))
    print(str("|    '' haven't the stomach to keep it fed any longer. One day, I will cease to be. ''   |").center(140))
    print(str("|                                                                                        |").center(140))
    print(str("|________________________________________________________________________________________|").center(140))

def woodsTellerEnd():
    print(str(" ________________________________________________________________________________________ ").center(140))
    print(str("|                                                                                        |").center(140))
    print(str("|      '' I know not who you are, ye hapless pilgrim, and I have little faith in ''      |").center(140))
    print(str("|                                                                                        |").center(140))
    print(str("|      '' your mission, but I do hope for it. Man is naught for this world without ''    |").center(140))
    print(str("|                                                                                        |").center(140))
    print(str("|     '' the sacrifice of your efforts. We may meet again, though I will not know ''     |").center(140))
    print(str("|                                                                                        |").center(140))
    print(str("|         '' it. My mind slips even now. Go then, and see your quest through. ''         |").center(140))
    print(str("|                                                                                        |").center(140))
    print(str("|________________________________________________________________________________________|").center(140))




