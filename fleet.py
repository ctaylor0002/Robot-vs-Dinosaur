# This class will hold 3 robots and be utilized in the Battlefield class later

class Fleet:

    def __init__(self):
        self.fleet = []

    def add_to_fleet(self, robo_object):
        self.fleet.append(robo_object)

    def get_robo_name(self):
        return_list = []
        for item in self.fleet:
            return_list.append(item.name)
        return(return_list)
    
    def get_robo_weapons(self):
        return_list = []
        for item in self.fleet:
            return_list.append(item.weapons)
        return(return_list)

    def get_robo_health(self):
        return_list = []
        for item in self.fleet:
            return_list.append(item.health)
        return(return_list)