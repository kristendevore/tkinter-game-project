# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage


from PIL.ImageTk import PhotoImage
from prey import Prey
from random import random, randint 

#import model
class Floater(Prey):
    radius_constant = 5
    def __init__(self,x,y):#,angle, speed):
        #radius_constant = 5
        
        self._gif = PhotoImage(file = 'ufo.gif')
        Prey.__init__(self,x,y, self._gif.width(), self._gif.height(), 0, Floater.radius_constant)
        
    def update(self):#,model):#,model):#,model):
        a = self.get_angle()
        b =  self.get_speed()
      #  new 
        
        if randint(1,10) <= 3:
            a = self.get_angle()
            variable_five  = .5
            fixed_variable_int = 7
            fixed_variable_int_two = 3
            b = self.get_speed()
            final_movement = min(fixed_variable_int,max(fixed_variable_int_two,b + random()-variable_five))
            self.set_velocity(final_movement, a + random()-variable_five)
    
        self.move()
        self.wall_bounce()
       # self.move()
    def display(self,canvas):
        canvas.create_image(self._x, self._y, image=self._gif)