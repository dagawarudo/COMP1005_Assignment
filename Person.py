import random
import math
class Person():
    def __init__(self,xpos,ypos,color,size = 10,step_size = 1):
        self.xpos = xpos
        self.ypos = ypos
        self.color = color
        self.size =size
        self.step_size = step_size
        self.ride_choice = None
        self.destination = False  
        self.exit = False

    def step_change(self, ride_list = []):
        #TODO Improve the collissions 
        #Source/Inspiration for unit vectors calculations : https://www.wikihow.com/Normalize-a-Vector
        ride_x, ride_y = self.ride_choice.get_target()
        change_x = ride_x - self.xpos
        change_y = ride_y - self.ypos
        distance = math.sqrt(change_x**2 +change_y**2) # Distance from ride to person 

        if distance <= 10:
            # If the person reaches the ride 
            self.reached_destination()
        #To get the unit vector 
        x = change_x/distance
        y = change_y/distance

        new_x = self.xpos + x * self.step_size
        new_y = self.ypos + y * self.step_size

        for ride in ride_list:
            if ride.is_collides(new_x, new_y):
                if ride == self.get_ride():
                    self.reached_destination()
                    return
                y *= -1.2
                new_y = self.ypos + y * self.step_size 
                new_x = self.xpos 
                if ride.is_collides(new_x, new_y):
                    y*= -1
                    x*= -1
                    new_y = self.ypos + y * self.step_size 
                    new_x = self.xpos + x * self.step_size * 1.5 
        self.xpos = new_x 
        self.ypos = new_y


    def go_destination(self):
        #Person is going towards the target/ride 
        self.destination = True 
    def get_destination(self):
        return self.destination
    
    def reached_destination(self):
        #Person is no longer going towards the target/ride 
        self.destination = False

    def plot_me(self,p):
        #Plot the person
        p.plot(self.xpos, self.ypos, "o", color = self.color, markersize= self.size)

    def insert_ride(self, ride):
        #Insert the target/ride 
        self.ride_choice = ride
        self.go_destination()
    def no_target(self):
        #If they do not have a ride
        return self.ride_choice is None 
    def get_ride(self):
        # Return the person's ride
        return self.ride_choice
    def set_exit(self):
        self.exit = True
    def get_exit(self):
        return self.exit
    def go_exit(self,exit_x,exit_y,object_list = []):
        change_x = exit_x - self.xpos
        change_y = exit_y - self.ypos
        distance = math.sqrt(change_x**2 +change_y**2)

        if distance <= 10:
            # If the person reaches the ride 
            self.set_exit()
            return 
        #To get the unit vector 
        x = change_x/distance
        y = change_y/distance

        new_x = self.xpos + x * self.step_size
        new_y = self.ypos + y * self.step_size

        for ride in object_list:
            if ride.is_collides(new_x, new_y):
                y *= -1.2
                new_y = self.ypos + y * self.step_size 
                new_x = self.xpos 
                if ride.is_collides(new_x, new_y):
                    y*= -1
                    x*= -1
                    new_y = self.ypos + y * self.step_size 
                    new_x = self.xpos + x * self.step_size * 1.5 
        self.xpos = new_x 
        self.ypos = new_y

    
        













