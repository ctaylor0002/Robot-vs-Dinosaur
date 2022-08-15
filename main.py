
# (5 points): As a developer, I want to make at least 7 commits with good, descriptive messages.

# (5 points): As a developer, I want to make a class for each of the following: Robot, Dinosaur, Weapon, Battlefield.

# (10 points): As a developer, I want a Dinosaur to have a name, health, and attack power.

# (10 points): As a developer, I want a Robot to have a name, health, and active_weapon.

# (10 points): As a developer, I want a Weapon to have a name and attack_power.

# (10 points): As a developer, I want a Dinosaur to have the ability to attack a Robot on a Battlefield. This attack method should lower a Robot’s health by the value of the Dinosaur’s attack_power.

# (10 points): As a developer, I want a Robot to have the ability to attack a Dinosaur on a Battlefield. This attack method should lower the Dinosaur’s health by the attack_power of the Robot’s active_weapon.

# (10 points): As a developer, I want the battle to conclude once either the robot or the dinosaur has its health points reduced to zero.

# Bonus Points:

# (5 points): As a developer, I want to choose from a List of 3 possible weapons before a robot makes an attack.

# (5 points): As a developer, I want to create Fleet and Herd classes, allowing for a list of 3 Robots to battle against a list of 3 Dinosaurs.

# The start of this game will have hard coded values for robot and dinosaur names that will be randomly selected and used with random health to create a random game. 
# I will do the same thing with the weapons on the robots as well as damage on the dinosaurs

import random
from battlefield import Battlefield
from dinosaur import Dinosaur
from herd import Herd
from fleet import Fleet
from robot import Robot
from weapon import Weapon

# List of Dinosaur Names
dinosaur_names = ['Tyrannosaurus Rex', 'Stegosaurus', 'Triceratops', 'Velociraptor', 'Spinosaurus', 'Allosaurus', 'Archaeopteryx']

#List of Robot Names
robot_names = ['Cyborg', 'Android', 'Intelligent Toaster Oven', 'Drone', 'Transformer', 'Battle Roomba', 'Rover', 'Furbee']

#Weapon name list
weapon_names = ['Death Laser', 'Buzz-saw', 'Flamethrower', 'Grenade Launcher', 'Spiked Bat', 'Rail Gun', 'Anti Dinosaur Cats']

#Active list for herd

def create_dinosaurs_for_herd(dinosaur_names):
    picked_name_index = random.randrange(0, len(dinosaur_names))
    picked_name = dinosaur_names[picked_name_index]

    #Give a random ammount of health to create some variance in the game
    health = random.randrange(50,100)

    #Give a random ammount of attack power to create some variance in the game
    attack_power = random.randrange(10,20)

    return([picked_name, health, attack_power])

def create_robots_for_fleet(robot_names):
    picked_name_index = random.randrange(0, len(robot_names))
    picked_name = robot_names[picked_name_index]

    #Give a random ammount of health to create some variance in the game
    health = random.randrange(50,100)

    #I will be adding the weapons after the robot is created


    return([picked_name, health])
    


the_herd = Herd()           #Create the Herd Object

# This runs through creating dinosaurs until I have 3 within the Herd
while len(the_herd.herd) < 3:
    dino_values = create_dinosaurs_for_herd(dinosaur_names)

    the_herd.add_to_herd(Dinosaur(dino_values[0], dino_values[1], dino_values[2]))

the_fleet = Fleet()         #Create the Fleet Object

# This runs to create 3 Robots to add to the fleet as well as 3 unique weapons for each of the robots
while len(the_fleet.fleet) < 3:
    robo_values = create_robots_for_fleet(robot_names)
    weapons = []
    while len(weapons) < 3:
        weapon_name_index = random.randrange(0,len(weapon_names))
        weapon_name = weapon_names[weapon_name_index]
        weapon_attack_power = random.randrange(5,25)
        weapons.append(Weapon(weapon_name, weapon_attack_power))

    the_fleet.add_to_fleet(Robot(robo_values[0], robo_values[1], weapons))

the_battlefield = Battlefield(the_herd, the_fleet)

# The game is ran here
display_msg = the_battlefield.display_welcome()
battle_phase = the_battlefield.battle_phase(display_msg[0], display_msg[1], display_msg[2], display_msg[3], display_msg[4])
the_battlefield.display_winners(battle_phase[0],battle_phase[1])





