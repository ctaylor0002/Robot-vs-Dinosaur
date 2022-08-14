# This class will hold 3 robots and be utilized in the Battlefield class later

class Fleet:

    def __init__(self):
        self.fleet = []

    def add_to_fleet(self, robo_object):
        self.fleet.append(robo_object)