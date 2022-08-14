from herd import Herd
from fleet import Fleet

class Battlefield:
    
    def __init__(self, herd, fleet):
        self.herd = herd
        self.fleet = fleet

    def display_welcome(self):
        dino_names =self.herd.get_dino_name()
        print('Today our contestants for the Herd are as follows:')
        print(f"{dino_names[0]}\n{dino_names[1]}\n{dino_names[2]}")
        
       
        