# A Black_Hole is derived from only a Simulton; it updates by removing
#   any Prey whose center is contained within its radius
#  (returning a set of all eaten simultons), and
#   displays as a black circle with a radius of 10
#   (width/height 20).
# Calling get_dimension for the width/height (for
#   containment and displaying) will facilitate
#   inheritance in Pulsator and Hunter

from simulton import Simulton
from prey import Prey
import model
from simulton import Simulton
from prey import Prey
#import model
#import model
class Black_Hole(Simulton):
    radius_constant = 10
    def __init__(self,x,y):
        self._new_x = x
        self._new_y = y
        new_x = 2*Black_Hole.radius_constant
        new_y = 2*Black_Hole.radius_constant
       # Simulton.__init__(self,x,y, new_x, new_y)
        Simulton.__init__(self,x,y,new_x,new_y)
    def update(self):#,model):#:,model):# model): #,model):#, model): #,model):
        #variable = 10
       # self.set_location(self._new_x, self._new_y)
        #v = ((self._new_x, self._new_y))
        new_items = model.find(lambda u : isinstance(u,Prey) and self.contains(u.get_location()))
        for x in new_items:
            model.remove(x)
        return new_items
    def contains(self, object):
        new = self.get_dimension()[0]/2
        return self.distance(object) <= new
  
    def display(self, canvas):
        new_width,new_height = self.get_dimension()
        canvas.create_oval(self._x-new_width/2, self._y-new_height/2, self._x+new_width/2, self._y+new_height/2, fill='black')
         
  
# class Black_Hole(Simulton):
#     radius_constant = 10
#     def __init__(self,x,y):
#         new_x = 2*Black_Hole.radius_constant
#         new_y = 2*Black_Hole.radius_constant
#         #self.set_location(x, y)
#         self._new_x = x
#         self._new_y = y
#       #  self._variabl
#        # Simulton.__init__(self,x,y, new_x, new_y)
#         Simulton.__init__(self,x,y,new_x,new_y)
#     def update(self):#:,model):# model): #,model):#, model): #,model):
#         #variable = 10
#      #   def objects(x):
#         #self.set_location(self._new_x, self._new_y)
#       #      return 
#        # final_new = set()
#         variable_x = ((self._new_x, self._new_y))
#       #  new = u.get_location()
#         final_new = model.find(lambda u : isinstance(u,Prey) and self.contains(u.get_location()))#u.get_location()))
#         #new = model.simulation_of_canvas
#      #   for x in model.simulation_of_canvas:
#          #   new_location = x.get_location()
#          #   if self.contains(new_location) and isinstance(x,Prey):
#            #     final_new.add(x)
#         for v in final_new:
#             model.remove(v)
#         
#         return final_new   
#                 
#        # new_items = model.find(lambda u : isinstance(u,Prey) and self.contains(u.get_location()))
#        # for x in new_items:
#         #    model.remove(x)
#        # return new_items
#     def contains(self, object):
#         new = self.get_dimension()[0]/2
#         return self.distance(object) <= new
#   
#     def display(self, canvas):
#         new_width,new_height = self.get_dimension()
#         canvas.create_oval(self._x-new_width/2, self._y-new_height/2, self._x+new_width/2, self._y+new_height/2, fill='black')
#          
  