# Making a game using TechwithTim's youtube videos

health = 10

print('Welcome to my first game. You are the only survivor after the shipwreck. Your goal is to survive on the island.')
wants_to_play = input('Do you want to play? (yes/no) ').lower()
if wants_to_play == 'yes':
    while True:
        ans = input('You start with 10 health. \nFirst choice... There is a heavy storm. Do you go into the forest or the cave? (forest/cave) ').lower()
        if ans == 'forest':
            print('You take shelter under some trees and get struck by lightning. That was not a good idea. You lose 10 health.')
            health -= 10
            if health <= 0:
                print('You now have 0 health and lose the game.')
                break
        elif ans == 'cave':
            print('You avoid the storm by taking shelter in a cave. You also find a knife. Someone has been here before...')

            ans = input('You are hungry. You spot some tribes men on the island. Do you approach their house or go into the forest? (house/forest) ').lower()
            if ans == 'house':
                print('The people give you some food and you go on your way.')
            elif ans == 'forest':
                print('You get attacked by a tiger but use your knife to defend yourself. You lose 7 health.')
                health -= 7

            ans = input('It\'s the next day and you start to build a shelter with some wood you collected. However, you see a ship in the distance. \n Do you light a fire or continue building your shelter? (fire/shelter) ').lower()
            if ans == 'fire':
                print('The people on the ship don\'t see you and you lose lots of energy. You faint from exhaustion, losing 3 health.')
                health -= 3
                if health <= 0:
                    print('You now have 0 health and lose the game.')
                    break
            elif ans == 'shelter':
                print('You build a cosy shelter and stay safe.')
            ans = input('You managed to survive another day and you are hungry again. \nDo you go back to the people by walking for 2 hours or do you hunt your own food in the dangerous forest? (go back/hunt) ').lower()
            if ans == 'go back':
                print('On your way back to the people, you get bitten by a venemous snake and lose 10 health. ')
                health -= 10
                if health <= 0:
                    print('You now have 0 health and lose the game.')
                    break
            elif ans == 'hunt':
                    print('You successfully hunt a rabbit and survive the day. \nYou hear a rescue helicopter above and quickly light a fire. They come and rescue you. Congratulations! You survived!')
                    break
else:
    print('Okay, bye then...')


