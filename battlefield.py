from herd import Herd
from fleet import Fleet
from dinosaur import Dinosaur
from robot import Robot
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
        return([picked_winner, dino_power, robo_weapons, dino_health, robo_health])

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


        while dino_team_health and robo_team_health != 0:
            print("\nDinosaur's Turn!")
            for dino in self.herd.herd:
                # Pick a target (Also determine if it has health left)
                got_target = False
                
                while got_target != True:
                    picked_target = self.fleet.fleet[random.randrange(0,len(self.fleet.fleet))]

                    if picked_target.health > 0:
                        got_target = True
                
                dino.attack(picked_target)
                
                if picked_target.health <= 0:
                    print(f"{picked_target.name} is unable to battle!")
                    self.fleet.remove_from_fleet(picked_target)

                robo_health = self.fleet.get_robo_health()
                robo_team_health = sum(robo_health)

                if robo_team_health == 0:
                    print("The Fleet has been destroyed!")
                    break
            print("\nRobot's Turn!")
            for robo in self.fleet.fleet:
                
                got_target = False

                while got_target != True:
                    picked_target = self.herd.herd[random.randrange(0,len(self.herd.herd))]

                    if picked_target.health > 0:
                        got_target = True

                robo.attack(picked_target)

                if picked_target.health <= 0:
                    print(f"{picked_target.name} is unable to battle!")
                    self.herd.remove_from_herd(picked_target)

                dino_health = self.herd.get_dino_health()
                dino_team_health = sum(dino_health)

                if dino_team_health == 0:
                    print('The Herd has been wiped out!')
                    break

        if dino_team_health <= 0:
            winning_team = 'Robots'
        elif robo_team_health <= 0:
            winning_team = 'Dinosaurs'

        return([winning_team, picked_winner])
    
    def display_winners(self, winning_team, picked_team):
        print(f"\n{winning_team} has won the fight!")

        if picked_team == winning_team[4:].title():
            print(f"Congratulations on picking {winning_team}!")
        else:
            print("Your picked team has lost!")

                


        
       
        