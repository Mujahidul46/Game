import sys, time, os

# This function creates a 'slow' typing effect.
def typewriter(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)

# This function asks the user if they want to restart.
def continue_prompt():
    print('\nDo you want to restart? (yes/no)')
    restart = input()
    return restart.lower() == 'yes'

# Welcome the user.
print('###################################################################################################################################')
print('#  Welcome to the island! You are the only survivor after your ship has sunk! Your goal is simply to survive until help arrives!  #')
print('###################################################################################################################################')

# Game variables
health = 10
wants_to_play = input('Do you want to play? (yes/no) ').lower()


# Main game loop
if wants_to_play == 'yes':
    while True:
        health = 10 # This reassigns 10 health to the user at the start of each game (so the previous health is not recorded if they decide to restart)
        # Question 1
        print()
        typewriter('You start with 10 health. \nFirst choice... You are on the lifeboat and you are slowly drifting towards the island in the distance... Just as you start to get close, a storm comes and pushes you in the other direction. \nDo you wait for the storm to calm down or do you swim towards the island? (wait/swim) ')
        ans = input()
        if ans.lower() == 'wait':
            print()
            typewriter('The storm lasts for days and you have run out of food and water. You\'re lifeboat capsizes and you drown! \n')
            health -= 10
            typewriter('You now have 0 health and lose the game.')
            if health <= 0 and continue_prompt():
                continue
            else:
                break
        elif ans.lower() == 'swim':
            print()
            typewriter('You use your last ounces of energy to swim towards the island. \n')

        # Question 2
        print()
        typewriter('You are soaking wet, hungry and exhausted but you\'re alive! You need to stay protected from the storm. Do you go into the forest or the cave? (forest/cave) ')
        ans = input()
        if ans.lower() == 'forest':
            print()
            typewriter('ZAP!!! You take shelter under some trees and get struck by lightning. That was not a good idea. You lose 10 health.')
            health -= 10
            typewriter('You now have 0 health and lose the game.')
            if health <= 0 and continue_prompt():
                continue
            else:
                break
        elif ans.lower() == 'cave':
            print()
            typewriter('You avoid the storm by taking shelter in the cave. You also find a knife. Someone has been here before... \nYou fall asleep and are suddenly awoken by a loud CRASH!! A large boulder has blocked you\'re exit. \nYou are too weak to move it so look for another exit by going deeper into the cave. ')
            typewriter('There are 3 paths. Which do you choose? (1/2/3) ')
            ans = input()
            if ans == '1':
                typewriter('\nAfter walking for what seemed like hours, you see a bright light at the end of the tunnel! FREEDOM!\n')
            elif ans == '2':
                typewriter('\nYou get lost in the darkness and wish you chose another path! You died.')
                health -= 10
                typewriter(' You now have 0 health and lose the game.')
                if health <= 0 and continue_prompt():
                    continue
                else:
                    break
            elif ans == '3':
                typewriter('\nYou walk down the path into the darkness... You can\'t see much and fall over lots of times, leaving you with cuts all over your body! You lose 3 health. \nEventually, you see a bright light at the end of the tunnel! FREEDOM!\n')
                health -= 3

        # Question 3
        print()
        typewriter('You are hungry and remember seeing rabbits in the forest. However, you find a bush full of suspicious looking wild berries on your way there. \nDo you eat the berries or keep going to the forest to hunt? (berries/hunt) ')
        ans = input()
        if ans.lower() == 'berries':
            print()
            typewriter('You gobble down the berries. Nom nom. They tasted okay... \n')
        elif ans.lower() == 'hunt':
            print()
            typewriter('You hunt a rabbit and cook it. You ate some of it but suddenly hear a growling noise behind you!! You get attacked by a tiger but use your knife just in time to defend yourself. You lose 7 health. \n')
            health -= 7
            typewriter('You now have 0 health and lose the game.')
            if health <= 0 and continue_prompt():
                continue
            elif health > 0:
                pass
            else:
                break

        # Question 4
        print()
        typewriter('It\'s the next day and you start to build a shelter with some wood you collected. However, you see a ship in the distance which could rescue you! \nDo you light a fire or continue building your shelter? (fire/shelter) ')
        ans = input()
        if ans.lower() == 'fire':
            print()
            typewriter('The people on the ship don\'t see you and you lose lots of energy (and hope). You faint from exhaustion, losing 3 health. \n')
            health -= 3
            typewriter('You now have 0 health and lose the game.')
            if health <= 0 and continue_prompt():
                continue
            elif health > 0:
                pass
            else:
                break
        elif ans.lower() == 'shelter':
            print()
            typewriter('You build a cosy shelter and stay safe. \n')

        # Question 5
        print()
        typewriter('You managed to survive another day and are hungry again. \nWhilst exploring the island, you see some tribesmen at a distance. Do you approach them for food or do you go hunt in the forest? (approach/hunt) ')
        ans = input()
        if ans.lower() == 'approach':
            print()
            typewriter('On your way to the people, you get bitten by a venemous snake and lose 10 health!! ')
            health -= 10
            typewriter('You now have 0 health and lose the game.')
            if health <= 0 and continue_prompt():
                continue
            else:
                break
        elif ans.lower() == 'hunt':
            print()
            typewriter('You successfully hunt a rabbit and survive the day. \nYou hear a rescue helicopter above and quickly light a fire. They come and rescue you. Congratulations! You survived with ' + str(health) + ' health remaining! \n')
            print('Thank you for playing! \n')
            if continue_prompt():
                continue
            else: 
                break
else:
    print()
    print('Okay, bye then... \n')
input('Press ENTER to exit')
