# (10 points): As a developer, I want a Dinosaur to have a name, health, and attack power.

class Dinosaur:

    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, target):
        # I will get the dino's target prior to calling the function
        print(f"{self.name} attacks {target.name} for {self.attack_power} leaving {target.name} at {target.health}!")
        target.health = target.health - self.attack_power

    