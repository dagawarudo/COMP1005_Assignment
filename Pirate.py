from Ride import Ride 
import numpy as np
class Pirate(Ride): 
    """Class to represent Pirate rides in showground"""

    def __init__(self, xpos, ypos,width, height, ship_color="red", frame_color="black"):
        super().__init__(xpos,ypos,width,height) 
        self.ship_color = ship_color
        self.frame_color = frame_color

        #Original frame coordinates
        frame_x =np.array([1,3,5,4,2])
        frame_y =np.array([1,5,1,3,3])

        #Transformed frame coordinates
        self.transform_frame_x = (frame_x - 1)/4 * width + xpos
        self.transform_frame_y = (frame_y - 1)/4 * height + ypos

        #Original ship coordinates
        ship_x = np.array([1,3,5,4,2,1,2,4,5])
        ship_y = np.array([3,5,3,1.5,1.5,3,2.5,2.5,3])

        #Transformed ship coordinates
        self.transform_ship_x = (ship_x-1)/4 * width + xpos
        self.transform_ship_y = (ship_y -1)/4 * height + ypos 

        self.angle = 0
        self.forward = True

        self.plot_ship_x = self.transform_ship_x
        self.plot_ship_y = self.transform_ship_y
        

    def plot_me(self, p):
        #box
        x = self.xpos + self.width
        y = self.ypos + self.height


        #plotting the figure 
        p.plot([self.xpos, x, x, self.xpos, self.xpos],[self.ypos, self.ypos,y, y,self.ypos]) # box
        p.plot(self.plot_ship_x, self.plot_ship_y, self.ship_color) # ship
        p.plot(self.transform_frame_x, self.transform_frame_y, self.frame_color) #frame
        



    def step_changes(self):

        
        #getting the angle in radians 
        theta = np.radians(self.angle)

        #getting the coordinates of the pivet 
        a = self.transform_ship_x[1]
        b = self.transform_ship_y[1]

            
        #getting the coordinates from the pivet 
        pivet_x = self.transform_ship_x - a
        pivet_y = self.transform_ship_y  - b

        
        
        

        cos_angle = np.cos(theta)
        sin_angle = np.sin(theta)
        # rotation matrix 
        rotation_matrix =  np.array([
                                    [cos_angle,-1 *sin_angle],
                                    [sin_angle, cos_angle]])

        #matrix of the ship from the pivet  
        ship_matrix = np.array([pivet_x,pivet_y])


        #the transformed ship coordinates from pivet 
        rotated_ship_matrix  = (rotation_matrix  @  (ship_matrix) )

        #updating the plotted coordinates 
        self.plot_ship_x = rotated_ship_matrix[0] + a
        self.plot_ship_y  = rotated_ship_matrix[1] + b




        # If the boat is moving forward 
        if self.forward == True:
            self.angle += 30
            if self.angle >= 90: # when the angle exceeds 90 degree,  the boat would go backwards 
                self.forward = False  
        # If the boat is going backwards 
        else:
            self.angle -= 30
            if self.angle == -90: # once it reaches -90 degrees make it go forward
                self.forward = True 

            
