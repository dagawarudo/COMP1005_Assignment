class Ride():
    def __init__(self,xpos,ypos,width,height,ride_limit = 5):
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
        #Insert person into the ride
        self.passengers.append(person)

    def ride_full(self):
        #If the ride queue is full return True else return False
        return len(self.queue) >= self.ride_limit
    
    def insert_queue(self, person):
        #Insert person into the queue
        self.queue.append(person)
    def remove_queue(self):
        #Return top most person inside 
        return self.queue.pop(0)
    def remove_passenger(self):
        #remove and return a  person from their  ride
        return self.passengers.pop(0)
    def get_target(self):
        #return coordinates 
        return self.xpos-2,self.ypos-2
    def get_exit(self):
        #return exit coordinates 
        return self.xpos + self.width, self.ypos + self.height
    def get_limit(self):
        #return ride limit 
        return self.ride_limit
    def get_queue(self):
        #return queue
        return self.queue
    def get_count(self):
        #return animation count
        return self.count 
    
    def set_count(self, count):
        #set the relevant count
        self.count = count 
    def is_animated(self):
        #return the animated state
        return self.animating
    
    def set_animated(self, value):
        # set the animated state
        self.animating = value


