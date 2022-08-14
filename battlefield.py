from herd import Herd
from fleet import Fleet
import random

class Battlefield:
    
    def __init__(self, herd, fleet):
        self.herd = herd
        self.fleet = fleet

    # Later I would like to add health pools, attack power and weapons to this display message
    def display_welcome(self):
        dino_names = self.herd.get_dino_name()
        dino_power = self.herd.get_dino_power()
        dino_health = self.herd.get_dino_health()
        robo_names = self.fleet.get_robo_name()
        robo_weapons = self.fleet.get_robo_weapons()
        robo_health = self.fleet.get_robo_health()

        print('Today our contestants for the Herd vs the Fleet are as follows:')
        print(f"{dino_names[0]}\n{dino_names[1]}\n{dino_names[2]}")
        print('VS!')
        print(f"{robo_names[0]}\n{robo_names[1]}\n{robo_names[2]}")
        picked_winner = input('Please pick who you would like to win. dino/robo ')

        Battlefield.battle_phase(picked_winner, dino_power, robo_weapons)

    def battle_phase(self, picked_winner, dino_power, robo_weapons, dino_health, robo_health):
        # I want a to start by picking a random team to start.

        choice = random.randrange(0,1)
        starter = ''
        if choice == 1 :
            starter = 'Robo'
        else:
            starter = 'Dino'

        # Now that I have the first fighter I will have to create a while statement to check health of the total teams. If they are 0 then the other team wins.

        dino_team_health = sum(dino_health)
        robo_team_health = sum(robo_health)

        while dino_team_health or robo_team_health > 0:
            


        
       
        