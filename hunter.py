# A Hunter is derived from both a Mobile_Simulton and a Pulsator; it updates
#   like a Pulsator, but it also moves (either in a straight line
#   or in pursuit of Prey), and displays as a Pulsator.


from prey import Prey
from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from math import atan2
import model

class Hunter(Pulsator,Mobile_Simulton):
  #  radius_constant = 200  
    def __init__(self,x,y):   
        Pulsator.__init__(self,x,y)
        width,height = self.get_dimension()
        variable_one = 0
        variable_two = 5
        Mobile_Simulton.__init__(self,x,y,width,height,variable_one,variable_two)
        self.randomize_angle()
        #self._new_x = x
        #self._new_y = y
        
    def update(self):#,model):
        new_list = []
        m = Pulsator.update(self)
       # self.set_location(self._new_x, self._new_y)
       # v = ((self._new_x, self._new_y))
      #  new_thing = model.find(lambda u : isinstance(u,Prey) and self.distance(u.get_location()) <= 200)#.contains((v)))
        new_thing  = model.find(lambda object : self.distance(object.get_location()) <= 200 and isinstance(object,Prey))
        if new_thing:
            for x in new_thing:
                new_list.append((self.distance(x.get_location()),x))
            new = min(new_list)
            first = self.get_location()
            second = new[1].get_location()
            first_variable = second[1] - first[1]
            second_variable = second[0] -first[0]
        
            self.set_angle(atan2(first_variable,second_variable))
        self.move()
        return m
                
                