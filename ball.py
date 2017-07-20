# A Ball is Prey; it updates by moving in a straight
#   line and displays as blue circle with a radius
#   of 5 (width/height 10).
from prey import Prey
import random
#import model
#import Prey from prey


class Ball(Prey):
    radius_constant = 5
    radius = 5
    
    def __init__(self,x,y):
   
        radius_constant = 5
        Prey.__init__(self,x,y, 2*radius_constant,2*radius_constant,0,radius_constant)
        self.randomize_angle()
 
                   #       pass
    def update(self):#,model):#:,model):
     #   self.randomize_angle()
        self.move()
        self.wall_bounce()
    def display(self,canvas):
       # Ball.create_random_color()
        canvas.create_oval(self._x -Ball.radius_constant, self._y -Ball.radius_constant, self._x+Ball.radius_constant, self._y +Ball.radius_constant, 
                                      fill = 'blue')