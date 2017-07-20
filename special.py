# I really liked the idea of the less known, kinda odd named colors in the tkinkter class so I decided for my special
#class to make a program that would create squares and change colors, randomizing each still from a list of odd named
#but similar looking colors. Basically, the special button should be able to create a square that changes colors even
#when the button is on stop, as well as the outline should change colors ( from a second list)
# and should behave much like a prey and the ball class
# square moves and behaves like a circle, animating changing colors of outline and inner square 
from prey import Prey
import random
#import model

class Special(Prey):
    
   
    #radius_constant = 5
    #radius = 5
    def __init__(self,x,y):
        radius_constant = 5
        Prey.__init__(self,x,y, 2*radius_constant,2*radius_constant,0,radius_constant)
        self.randomize_angle()
        #self.randomize_angle()
       # def create_random_color(self):
        #self.int_one = random.randint(0,255)
       # self.int_two = random.randint(0,255)
       # self.int_three = random.randint(0,255)
       
       # self.variable = ('#{}02X{}02X{}02X'.format(self.int_one, self.int_two, self.int_three))
    def update(self):#,model):#model):#, model):#:,model):
     #   self.randomize_angle()
       # self.randomize_angle()
        self.move()
        self.wall_bounce()
        #self.randomize_angle()
    def display(self,canvas):
        #self.randomize_angle()
        new_list = ['linen', 'antique white', 'blanched almond', 'bisque', 'peach puff', 'lemon chiffon', 'mint cream',
                    'azure', 'alice blue', 'lavender', 'lavender blush', 'misty rose','snow']
        newer_list = ['powder blue', 'pale turquoise',  'turquoise',
    'cyan', 'light cyan', 'cadet blue', 'aquamarine', 'sea green', 'light sea green']
        
        canvas.create_rectangle(self._x - 8, self._y - 8, self._x + 8, self._y + 8, fill = random.choice(new_list), outline = random.choice(newer_list)) #random.randint(25,50), random.randint(120,150), random.randint(70, 100), fill = random.choice(new_list))
                                # 150, 75, fill="blue")
      #  canvas.create_oval(self._x -Special.radius_constant, self._y -Special.radius_constant, self._x+Special.radius_constant, self._y +Special.radius_constant, 
      #                                fill = random.choice(new_list))