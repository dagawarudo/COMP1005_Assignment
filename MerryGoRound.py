from Cubicle import Cubicle
from Ride import Ride
import numpy as np
class MerryGoRound(Ride):
    def __init__(self, xpos, ypos,width, height,cubicles):
        super().__init__(xpos,ypos,width,height)
        self.cubicles = cubicles
        self.cubicles_list = []
#TODO IMPROVE THE COORDINATES
        self.x = self.xpos + self.width
        self.y = self.ypos + self.height
        
        # Coordinates for the wheel/circle
        self.center_x = (self.x + self.xpos)/2
        self.center_y = (self.y + self.ypos)/2

        self.radius = (self.x - self.center_x) #Radius 

        cubicle_size = 4
        color_list = ["red","blue","yellow", "green","orange","pink","purple","cyan"]

        for i  in range(self.cubicles): # To plot each cubicle in thr wheel
            cubicle_angle = 2 *np.pi *i/cubicles #To divide the cubicles evenly in the wheel

            cubicle_x = self.center_x + self.radius *np.cos(cubicle_angle)
            cubicle_y = self.center_y + self.radius * np.sin(cubicle_angle)

            cubicle_color = color_list[i]

            cubicle = Cubicle(cubicle_x, cubicle_y,cubicle_angle,cubicle_size,cubicle_color)

            self.cubicles_list.append(cubicle)

        
    def plot_me(self, p):
        #plot the Merry Go Roundd

        #plotting the figure
        p.plot([self.xpos, self.x, self.x, self.xpos, self.xpos],[self.ypos, self.ypos,self.y, self.y,self.ypos]) # box
        circle = p.Circle((self.center_x, self.center_y), self.radius, color="black", fill=False,linewidth  = 2) # Wheel
        ax = p.gca()
        ax.add_patch(circle)

        # SOURCE FOR CIRCLE PLOTTING : https://stackoverflow.com/a/9216646

        #plotting cubicles of the Merry go round
        for cubicle  in self.cubicles_list:
            cubicle_x = cubicle.transform_x
            cubicle_y = cubicle.transform_y
            cubicle_size = cubicle.size
            cubicle_color = cubicle.color
            p.plot(cubicle_x, cubicle_y,"^",color = cubicle_color,markersize = cubicle_size * 2)


    def step_changes(self):
        
        #Coordinates of the pivet
        a = self.center_x
        b = self.center_y

        for cubicle in self.cubicles_list:
            angle = cubicle.angle
            theta = np.radians(angle)

            cos_angle = np.cos(theta)
            sin_angle = np.sin(theta)

            # rotation matrix
            rotation_matrix =  np.array([[cos_angle, -1*sin_angle],[sin_angle,cos_angle]])



            cubicle_matrix = np.array([cubicle.x - a,cubicle.y -b])

            rotated_cubicle = (rotation_matrix @ cubicle_matrix)

            cubicle.transform_x = rotated_cubicle[0] + a
            cubicle.transform_y = rotated_cubicle[1] + b 

            cubicle.angle += 15
    def reset(self):
        #return 
        return








