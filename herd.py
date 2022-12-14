#This class will hold 3 dinosaurs and will be utilized on the Battlefield class later

class Herd:

    def __init__(self):
        self.herd = []
        #Allow the herd to be created without anything added

    def add_to_herd(self, dino_object):
        self.herd.append(dino_object)

    def remove_from_herd(self, dino_to_remove):
        self.herd.remove(dino_to_remove)

    def get_dino_name(self):
        return_list = []
        for item in self.herd:
            return_list.append(item.name)
        return(return_list)

    def get_dino_power(self):
        return_list = []
        for item in self.herd:
            return_list.append(item.attack_power)
        return(return_list)

    def get_dino_health(self):
        return_list = []
        for item in self.herd:
            return_list.append(item.health)
        return(return_list)

