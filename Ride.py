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

    def is_collides(self, x,y,margin = 5):
        """
        Compares the coordinates of an object and rides and checks if the object would be inside the ride 
        """
        
        return (self.xpos - margin < x < self.xpos + self.width +margin) and (self.ypos -margin < y < self.ypos + self.height+margin)

    def insert_person(self, person):
        """
        Insert the person in their ride 
        """
        
        self.passengers.append(person)

    def ride_full(self):
        """
        Checks if ride is full
        """
        #If the ride queue is full return True else return False
        return len(self.queue) >= self.ride_limit
    
    def insert_queue(self, person):
        """
        Insert the person in the ride's queue  
        """
        #Insert person into the queue
        self.queue.append(person)
        position = len(self.queue) # Get position of the queue 
        #Update the people's position at the queue
        person.xpos = self.xpos -4
        person.ypos = self.ypos + position*2
    def remove_queue(self):
        """
        Removes person from a queue 
        """
        #Return top most person inside 
        return self.queue.pop(0)
    def remove_passenger(self):
        """
        Removes a person from their ride 
        """
        #remove and return a  person from their  ride
        return self.passengers.pop(0)
    def get_target(self):
        """
        get coordinates 
        """
        #return coordinates 
        return self.xpos-2,self.ypos-2
    def get_exit(self):
        """
        return exit coordinates
        """
        #return exit coordinates 
        return self.xpos + self.width, self.ypos + self.height
    def get_limit(self):
        """
        return ride limit 
        """
        return self.ride_limit
    def get_queue(self):
        #return queue
        return self.queue
    def get_count(self):
        #return animation count
        return self.count 
    def get_width(self):
        return self.width
    def get_height(self):
        return self.height
    
    def set_count(self, count):
        #set the relevant count
        self.count = count 
    def is_animated(self):
        #return the animated state
        return self.animating
    
    def set_animated(self, value):
        # set the animated state
        self.animating = value


