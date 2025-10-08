from Cubicle import Cubicle
import numpy as np
import random
class FerrisWheel():
    def __init__(self, xpos, ypos,width, height,cubicles ,cubicle_color="red", frame_color="black"):
        self.xpos = xpos
        self.ypos = ypos
        self.width = width
        self.height = height
        self.cubicle_color = cubicle_color
        self.frame_color = frame_color
        self.cubicles = cubicles

        #Original frame coordinates
        frame_x =np.array([1,3,5,4,2])
        frame_y =np.array([1,5,1,3,3])

        #Transformed frame coordinates
        self.transform_frame_x = (frame_x - 1)/4 * width + xpos
        self.transform_frame_y = (frame_y - 1)/4 * height  + ypos

        self.cubicles_list = []
#TODO IMPROVE THE COORDINATES
        x = self.xpos + self.width
        y = self.ypos + self.height

        center_x = (x+self.xpos)/2
        center_y = (y+self.ypos)/2
        radius = (x - center_x)

        self.center_x =center_x
        self.center_y = center_y

        cubicle_size = 4
        color_list = ["red","blue","yellow", "green","orange"]

        for i  in range(self.cubicles):
            cubicle_angle = 2 *np.pi *i/cubicles

            cubicle_x = center_x + radius *np.cos(cubicle_angle)
            cubicle_y = center_y + radius * np.sin(cubicle_angle)

            cubicle_color = random.choice(color_list)

            cubicle = Cubicle(cubicle_x, cubicle_y,cubicle_angle,cubicle_size,cubicle_color)

            self.cubicles_list.append(cubicle)

        
    def plot_me(self, p):
        x = self.xpos + self.width
        y = self.ypos + self.height

        center_x = (x+self.xpos)/2
        center_y = (y+self.ypos)/2
        radius = (x - center_x)  

         #plotting the figure
        p.plot([self.xpos, x, x, self.xpos, self.xpos],[self.ypos, self.ypos,y, y,self.ypos]) # box
        p.plot(self.transform_frame_x, self.transform_frame_y, self.frame_color) #frame
        circle = p.Circle((center_x, center_y), radius, color="black", fill=False,linewidth = 3)
        ax = p.gca()
        ax.add_patch(circle)

        # SOURCE FOR CIRCLE PLOTTING : https://stackoverflow.com/a/9216646

        #plotting cubicles of the ferris wheel
        for cubicle  in self.cubicles_list:
            cubicle_x = cubicle.transform_x
            cubicle_y = cubicle.transform_y
            cubicle_size = cubicle.size
            cubicle_color = cubicle.color
            cubicle_plot = p.plot(cubicle_x, cubicle_y,"o",color = cubicle_color,markersize = cubicle_size)

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
