# A Pulsator is a Black_Hole; it updates as a Black_Hole
#   does, but also by growing/shrinking depending on
#   whether or not it eats Prey (and removing itself from
#   the simulation if its dimension becomes 0), and displays
#   as a Black_Hole but with varying dimensions

import model
from blackhole import Black_Hole

class Pulsator(Black_Hole):
    shrinking_constant = 30   

    def __init__(self,x,y):   
        self._counting_object = 0
        Black_Hole.__init__(self,x,y)
       
        
        
    def update(self):#,model):#,model):#,model):#model):
        subtract_one = -1
        self._counting_object += 1
        new_variable = Black_Hole.update(self)#,model)#model)#model)#,model)
        #deleted_object = Black_Hole.update(self,model)
        if new_variable:
           # self._counting_object = 0
            self.change_dimension(len(new_variable),len(new_variable))
            self._counting_object = 0
        elif self._counting_object == 30:
            self.change_dimension(subtract_one,subtract_one)
            
            if self.get_dimension()[0] == 0:
                
                model.remove(self)
            self._counting_object = 0
        return new_variable