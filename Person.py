import random
import math
class Person():
    def __init__(self,xpos,ypos,color):
        self.xpos = xpos
        self.ypos = ypos
        self.color = color
        self.destination = False 

    def step_change(self, ride_x, ride_y, ride_list = [], step_size = 1):
        #Source/Inspiration for unit vectors calculations : https://www.wikihow.com/Normalize-a-Vector
        change_x = ride_x - self.xpos
        change_y = ride_y - self.ypos
        distance = math.sqrt(x**2 +y**2) # Distance from ride to person 

        if distance == 0:
            # If the person reaches the ride 
            self.reached_destination()
        #To get the unit vector 
        x = change_x/distance
        y = change_y/distance

        new_x = self.xpos + x * step_size
        new_y = self.ypos + y * step_size

        for ride in ride_list:
            if ride.is_collides():
                y *= -1
                new_y = self.ypos + y * step_size
        self.xpos = new_x
        self.ypos = new_y
    def reached_destination(self):
        self.destination = True 
    def get_destination(self):
        return self.destination
    def left_destination(self):
        self.destination = False
        













