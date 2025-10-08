import numpy as np
class HotAirBalloon():
    def __init__(self,xpos,ypos,width,height,balloon_color, frame_color):
        self.xpos = xpos
        self.ypos = ypos
        self.width = width 
        self.height = height
        self.balloon_color = balloon_color
        self.frame_color = frame_color
        self.forward = True

        #Setting up the box

        x = self.xpos + self.width
        y = self.ypos + self.height

        self.box_x = np.array([self.xpos, x, x, self.xpos, self.xpos])
        self.box_y = np.array([self.ypos, self.ypos,y, y,self.ypos])

        x_mid = self.xpos + self.width/2
        y_mid = self.ypos + self.height/4

        self.radius = self.height/8


        self.cubicle_x = np.array([x_mid-x_mid*0.05,x_mid+x_mid*0.05,x_mid+x_mid*0.05,x_mid-x_mid*0.05,x_mid-x_mid*0.05])
        self.cubicle_y = np.array([self.ypos,self.ypos,y_mid,y_mid,self.ypos])

        self.rope_x = np.array([x_mid, x_mid])
        self.rope_y = np.array([y_mid, y_mid + self.radius])
  
        self.center_x = x_mid
        self.center_y = y_mid + 2 * self.radius

    
         



        



    def plot_me(self,p):
        x = self.xpos + self.width
        y = self.ypos + self.height


        #plotting the figure
        p.plot(self.box_x,self.box_y) # box
        p.plot(self.cubicle_x,self.cubicle_y)
        p.plot(self.rope_x,self.rope_y)

        circle = p.Circle((self.center_x, self.center_y), self.radius, color="black", fill=True,linewidth = 3)
        ax = p.gca()
        ax.add_patch(circle)

        

    def step_change(self):
        stepchange = 5 
        if self.center_y + self.radius>= self.ypos + self.height:
            self.forward = False
        elif self.cubicle_y[0] <= self.ypos:
            self.forward = True
        if self.forward == True:
            self.cubicle_y += stepchange
            self.center_y += stepchange
            self.rope_y += stepchange
        else:
            self.cubicle_y -= stepchange
            self.center_y -= stepchange
            self.rope_y -= stepchange


