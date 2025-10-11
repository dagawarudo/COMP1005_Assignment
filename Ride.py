class Ride():
    def __init__(self,xpos,ypos,width,height):
        self.xpos = xpos
        self.ypos = ypos
        self.width = width
        self.height = height

    def is_collides(self, x,y):
        # Compares the coordinates of an object and rides and checks if the object would be inside the ride 
        return (self.xpos <= x <= self.xpos + self.width) and (self.ypos <= y <= self.ypos + self.height)

