# (10 points): As a developer, I want a Robot to have a name, health, and active_weapon.

class Robot:

    def __init__(self, name, total_health, weapon):
        self.name = name
        self.health = total_health
        self.active_weapon = weapon

    # Create a function here to grab a random weapon from a list and set it to this robots weapon.
