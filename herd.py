#This class will hold 3 dinosaurs and will be utilized on the Battlefield class later

class Herd:

    def __init__(self):
        self.herd = []
        #Allow the herd to be created without anything added

    def add_to_herd(self, dino_object):
        self.herd.append(dino_object)
