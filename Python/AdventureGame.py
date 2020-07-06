import random

import time


def display_message(instructions):

    # delaying the displaying of message by 1 second
    print(instructions)
    time.sleep(1.00)


def delayed_message(instructions):

    # delaying the displaying of message by 2 second
    print(instructions)
    time.sleep(2.00)


def beginning(item, villain, hunter):

    # things that happen when the game begins
    delayed_message("Alright! Hunter " + hunter + ". Now let me continue")
    display_message("This game timeline dates back in the ancient greeks.\n")
    display_message("You find yourself standing in a graveyard,"
                    " filled with graves and dead leaves.\n")
    delayed_message("\nRumor has it that a " + villain + " is hunting people,"
                    " hiding somewhere around here, and has been terrifying"
                    " the nearby villagers.\n")
    display_message("The little girl inside you got pretty scared.\n")
    delayed_message("In front of you is a church.\n")
    display_message("To your left is an old watchtower.\n")
    display_message("In your hand you hold your trusty (but not much of a big"
                    " hitter) spear.\n")


def graveyard(inv, villain, hunter):

    # things happen when the player is in the graveyard
    delayed_message("Enter 1 to knock on the door of the church.")
    display_message("Enter 2 to peer into the watchtower.")
    display_message("What would you like to do? Hunter " + hunter + ".")
    while True:
        opt = input()
        if(opt == '1'):
            church(inv, villain, hunter)
            break
        elif(opt == '2'):
            watchtower(inv, villain, hunter)
            break
        else:
            print("(Please enter 1 or 2.)\n")
            graveyard(inv, villain, hunter)
            break


def watchtower(item, villain, hunter):

    # things happen when the player enters the watchtower
    if "sword" in item:
        display_message("\nYou peer cautiously into the watchtower.")
        display_message("\nYou've been here before, you idiot, and gotten all"
                        " the good stuff. It's just an empty disgusting"
                        " watchtower now.")
        delayed_message("\nYou walk back to the graveyard with doubts in mind"
                        " about your memory, poor " + hunter + ".\n")
    else:
        display_message("\nYou peer cautiously into the watchtower.")
        display_message("\nIt turns out to be only a very deserted place.")
        delayed_message("\nYour eye catches a glint of metal behind"
                        " staircase.")
        delayed_message("\nYou have found a japanese sword!")
        display_message("\nAnd you figured out this sword belongs to the"
                        " greatest ever ninja, Hatori Honzo.")
        display_message("\nGenius! " + hunter + ".")
        delayed_message("\nYou know the sword's power.")
        display_message("\nYou discard your silly old spear and take the"
                        " sword with you.")
        delayed_message("\nYou walk back out to the graveyard.\n")
        item.append("sword")
    graveyard(item, villain, hunter)


def church(item, villain, hunter):

    # things happen when the players enters the church
    display_message("\nYou approach the door of the church.")
    display_message("\nYou are about to knock when the door opens and out"
                    " steps a " + villain + ".")
    display_message("\nHoly moly! This is the " + villain + " occupied"
                    " church!")
    display_message("\nThe " + villain + " attacks you!\n")
    if "sword" not in item:
        delayed_message("The little girl I mentioned earlier, screams out"
                        " loud. Puny " + hunter + ".\n")
        display_message("You feel a bit under-prepared for this, "
                        "what with only having a tiny spear. You're a joke on"
                        " the face of hunters, " + hunter + "!\n")
    while True:
        print("Would you like to (1) fight like a knight or (2) run away like"
              " a clown, Mighty " + hunter + "?")
        opt = input()
        if(opt == '1'):
            if "sword" in item:
                delayed_message("\nThe sword of Hatori Honzo shines brightly"
                                " in your hand as you brace yourself for the"
                                " attack.")
                display_message("\nBut the " + villain + " takes one look at"
                                " your shiny new monster killer"
                                " and runs away!")
                delayed_message("\nYou have rid the town of the " + villain +
                                ". You are victorious but lucky, that"
                                " coward " + villain + " could have killed you"
                                " easily.\n")
                delayed_message("Ha...Ha...Ha...just kidding(no, I'm not ;))")
            else:
                delayed_message("\nYou do your best...")
                delayed_message("but your spear is no match for"
                                " the " + villain + ".")
                display_message("The " + villain + " torn you apart.")
                display_message("\nNow what?...")
                delayed_message("\nYou have been defeated! You pathetic"
                                " piece of waste!\n")
            restart(hunter, villain)
            break
        elif(opt == '2'):
            delayed_message("\nYou run back like a namby-pamby into the"
                            " graveyard.\nLuckily, you been spared on the"
                            " mercy of " + villain + ".\n")
            graveyard(item, villain, hunter)
            break


def restart(hunter, villain):

    # messages displayed when the player chooses to play again or quit the game
    print("Would you like to risk your life again? (y/n)")
    a = str(input())
    a = a.lower()
    while True:
        if a == 'y':
            display_message("\nDelicious! I'd love to see you die again!"
                            " Ha...Ha...Ha ...\n")
            playgame()
        elif a == 'n':
            display_message("\nRun away you coward, hide in your"
                            " Mumma's lap.\n")
            delayed_message("\nWords used in the game are just for fun, don't"
                            " take it seriously.")
            display_message("But what can you do? Hahaha")
            display_message("GoodBye " + hunter + "!")
            display_message(" You better pray, not to encounter"
                            " the " + villain + " in the middle of the night.")
            delayed_message("Take care " + hunter + "!")
            delayed_message("")
            delayed_message("")
            delayed_message("")
            break
        else:
            restart(hunter, villain)
            break


def playgame():

    # when the game start, the villain is chosen at random
    # also the name of player is assigned through player input
    villain = random.choice(["zombie", "pirate", "dragon", "gorgon", "dracula",
                            "frankestien", "witch", "bigfoot"])
    hunter = input("What should I call you...? ")
    beginning([], villain, hunter)
    graveyard([], villain, hunter)


if __name__ == "__main__":
    playgame()
