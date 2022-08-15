# (10 points): As a developer, I want a Robot to have a name, health, and active_weapon.
import random
import time

class Robot:

    def __init__(self, name, total_health, weapons):
        self.name = name
        self.health = total_health
        self.active_weapon = ''
        self.weapon_list = weapons

    # Create a function here to grab a random weapon from a list and set it to this robots weapon.
    def grab_random_weapon(self, weapon_list):
        random_index = random.randrange(0,len(weapon_list))
        self.active_weapon = weapon_list[random_index]

    # Add a weapon to available weapons for this robot
    def add_weapon_to_availability(self, weapon):
        self.weapon_list.append(weapon)
    
    def pick_weapon_from_arsenal(self):
        self.active_weapon = self.weapon_list[random.randrange(0, len(self.weapon_list))]
        

    def attack(self, target):
        # I will get the robos's target prior to calling the function
        self.pick_weapon_from_arsenal()
        target.health -= self.active_weapon.attack_power
        print(f"{self.name} attacks {target.name} with a {self.active_weapon.weapon_name} for {self.active_weapon.attack_power} leaving {target.name} at {target.health}!")
        time.sleep(2)