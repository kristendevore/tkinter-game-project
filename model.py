import controller, sys
import model   #strange, but we need a reference to this module to pass this module to update

from ball      import Ball
from floater   import Floater
from blackhole import Black_Hole
from pulsator  import Pulsator
from hunter    import Hunter
from itertools import count, cycle
from special import Special
from posix import remove


# Global variables: declare them global in functions that assign to them: e.g., ... = or +=
cycle_count = 0
simulation_of_canvas = set()
running = False
stop_after_setup_one = False
click_on = None
  
  
#return a 2-tuple of the width and height of the canvas (defined in the controller)
def world():
    return (controller.the_canvas.winfo_width(),controller.the_canvas.winfo_height())
  
#reset all module variables to represent an empty/stopped simulation
def reset ():
    global stop_after_setup_one,running,simulation_of_canvas,cycle_count
    stop_after_setup_one = False
    running = False
    simulation_of_canvas = set()
    cycle_count = 0
    click_on = None
  
  
#start running the simulation
def start ():
    global running
    running = True
  
  
#stop running the simulation (freezing it)
def stop ():
    global running
    running = False
  
  
#tep just one update in the simulation
def step():
  #  global running, stop_after_setup_one
   # stop_after_setup_one = True
  #  running = True
    global cycle_count
   # variable = 0
    cycle_count += 1
    cycle_count -= 1
    #for i in simulation_of_canvas:
         #i.update()
    global stop_after_setup_one, running
    stop_after_setup_one = True
    running = True
      
  
  
#remember the kind of object to add to the simulation when an (x,y) coordinate in the canvas
#  is clicked next (or remember to remove an object by such a click)   
def select_object(kind):
    global click_on
    click_on = kind

  
  
#add the kind of remembered object to the simulation (or remove all objects that contain the
#  clicked (x,y) coordinate
def mouse_click(x,y):
    if click_on == 'Remove':
        v = x,y
       # for z in find()
        #if model.contains(find(v):
        for z in find(lambda z: z.contains(v)):
            simulation_of_canvas.remove(z)
    elif click_on == None:
        pass
       # print('No object has been selected, please select one now')
    else:
    #    print(x)
      #  print(y)
        new_x = str(x)
        new_y = str(y)
        simulation_of_canvas.add(eval(click_on + '(' + new_x + ',' + new_y + ')'))
  
  
#add simulton s to the simulation
def add(s):
    global simulation_of_canvas
    simulation_of_canvas.add(s)
      
  
# remove simulton s from the simulation    
def remove(s):
    global simulation_of_canvas
    simulation_of_canvas.delete(s)
  
#find/return a set of simultons that each satisfy predicate p    
def find(p):
    new_set = set()
    for i in simulation_of_canvas:
        if p(i):
            new_set.add(i)
    return new_set
  
  
#call update for every simulton in the simulation
def update_all():
    global stop_after_setup_one, running
   # global cycle_count
   # global cycle_count
#     if running:
#         global cycle_count, world
#         cycle_count += 1
#         for i in simulation_of_canvas:
#             if i in simulation_of_canvas:
#         
#                 i.update()
#         if stop_after_setup_one:
#             stop_after_setup_one = False
#             running = False
    if running == True:
        global cycle_count, world
        cycle_count += 1
        begin_simulation = set(simulation_of_canvas)
        for i in begin_simulation:
            if i in simulation_of_canvas:
                i.update()
        if stop_after_setup_one:
            stop_after_setup_one = False
            running = False
#   
  
def display_all():
    for o in controller.the_canvas.find_all():
        controller.the_canvas.delete(o)
    
    for s in simulation_of_canvas:
        s.display(controller.the_canvas)
    
    controller.the_progress.config(text=str(len(simulation_of_canvas))+" simultons/"+str(cycle_count)+" cycles")
#     if simulation_of_canvas != None:
#         for o in controller.the_canvas.find_all():
#             controller.the_canvas.delete(o)
#         for s in simulation_of_canvas:
#             s.display(controller.the_canvas)
       # for o in controller.the_canvas.find_all():
        #    controller.the_canvas.delete(o)
      
   
    #controller.the_progress.config(text=str(len(simulation_of_canvas)) + ' simultons total/' +str(cycle_count)+' cycles total')

