class Ride():
    def __init__(self,xpos,ypos,width,height,ride_limit = 8):
        self.xpos = xpos
        self.ypos = ypos
        self.width = width
        self.height = height
        self.ride_limit = ride_limit
        self.queue = []
        self.passengers = []

    def is_collides(self, x,y):
        # Compares the coordinates of an object and rides and checks if the object would be inside the ride 
        return (self.xpos < x < self.xpos + self.width) and (self.ypos < y < self.ypos + self.height)

    def insert_ride(self, person):
        if self.ride_full():
            return 
        self.passengers.append(person)
        self.remove_queue(person)
        return

    def ride_full(self):
        return len(self.queue) >= self.ride_limit
    
    def insert_queue(self, person):
        self.queue.append(person)
    def remove_queue(self, person):
        self.queue.remove(person)
    def get_target(self):
        return self.xpos-2,self.ypos-2
    def get_exit(self):
        return self.xpos + self.width, self.ypos + self.height


