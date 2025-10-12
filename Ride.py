class Ride():
    def __init__(self,xpos,ypos,width,height,ride_limit = 8):
        self.xpos = xpos
        self.ypos = ypos
        self.width = width
        self.height = height
        self.ride_limit = ride_limit
        self.count = 0
        self.queue = []
        self.passengers = []
        self.animating = False

    def is_collides(self, x,y):
        # Compares the coordinates of an object and rides and checks if the object would be inside the ride 
        return (self.xpos < x < self.xpos + self.width) and (self.ypos < y < self.ypos + self.height)

    def insert_person(self, person):
        self.passengers.append(person)

    def ride_full(self):
        return len(self.queue) >= self.ride_limit
    
    def insert_queue(self, person):
        self.queue.append(person)
    def remove_queue(self):
        return self.queue.pop(0)
    def remove_passenger(self):
        return self.passengers.pop(0)
    def get_target(self):
        return self.xpos-2,self.ypos-2
    def get_exit(self):
        return self.xpos + self.width, self.ypos + self.height
    def get_limit(self):
        return self.ride_limit
    def get_queue(self):
        return self.queue
    def get_count(self):
        return self.count 
    
    def set_count(self, count):
        self.count = count 
    def is_animated(self):
        return self.animating
    
    def set_animated(self, value):
        self.animating = value


