
#
# Student Name : Dayyaan Ishmael
# Student ID   : 23549654
#
# showDemo.py - testing simulation of rides in a showground
#

from Pirate  import Pirate
from HotAirBalloon import HotAirBalloon as Balloon
from FerrisWheel import FerrisWheel as Wheel
from Person import Person
from Ride import Ride
import sys
import matplotlib.pyplot as plt
import random  
import csv 
import matplotlib.image as pimg
import matplotlib.patches as patches

def main() :
    if len(sys.argv) < 2:
        sys.exit("For interactive mode type in \'-i\' , for batch mode type in \'-f\' and the relevant CSV file ")
    elif sys.argv[1] == "-i":
        interactive_mode()
    elif sys.argv[1] == "-f":
        batch_mode(sys.argv)
    else:
        sys.exit("For interactive mode type in \'-i\' , for batch mode type in \'-f\' and the relevant CSV file ")
def get_int(text, less, greater):
    """
    Function is used to vaidate integer from the user 
    """
    n = None 
    while n is None:
        try:
            n = int(input(text))
            if n < less or n > greater:
                n = None 
                raise ValueError
        except ValueError:
            print("Please select the valid inputs")
        else:
            return n 
        
def get_ride(ride_options, ride_input):
    """
    Function is used to get rides from the user.
    """
    ride = None
    while ride is None:
        ride = input(f"Select your rides by typing the relevant letters \n{ride_options} ")
        xpos = ride_input[0]
        ypos = ride_input [1]
        width = ride_input [2]
        height = ride_input [3]
        match ride.upper():
            case "B":
                print("Input color of the balloon's box")
                frame_color = get_color()
                print("Input color of the balloon")
                balloon_color = get_color()
                return Balloon(xpos,ypos,width,height,balloon_color,frame_color)
            case "W":
                cubicles = get_int("Input the number of cubicles (minimum 4 maximum 8) ",4,8)
                print("Input color of the frame")
                frame_color = get_color()
                return Wheel(xpos,ypos,width,height,cubicles,frame_color)
            case "P":
                print("Input color of Pirate Sheep ")
                ship_color = get_color()
                print("Input color of the frame ")
                frame_color = get_color()
                return Pirate(xpos,ypos,width,height,ship_color,frame_color)
            case _:
                print("Please follow the relevant instructions ")


def interactive_mode():
    """
    Interactive mode which allows the user to put their inputs to simulate the rides 
    """
    color_list = ["red","blue","yellow", "green","orange","purple","gold","lightblue","pink","cyan"]
    positions = [[25+1,200,50,50],[150+2,210,50,50],[300,200,50,50],[25+1,50,50,50],[150+2,30,50,50],[300,50,50,50]]
    object_positions = [[150,110,100,80]]
    ride_list = []
    patron_list = []
    object_list = []
    patron_exit_list = []
    
    no_of_rides = get_int("How many rides would you like (a minimum of 2  and a maximum of 6 rides) ",2,6)
    ride_options = "\nHot Air Balloon     -   B\n" \
        "Ferris Wheel   -   W\n" \
        "Pirate Ship    -   P\n"
    for i in range(no_of_rides):
        ride = get_ride(ride_options, positions[i])
        ride_list.append(ride)
    
    no_of_people = get_int("How many people would you like (a minimum of 20 and a maximum of 60 people) ",20,60)

    for i in range(len(object_positions)):
        object_input = object_positions[i]
        xpos = object_input[0]
        ypos = object_input [1]
        width = object_input [2]
        height = object_input [3]
        object = Ride(xpos,ypos,width,height)
        object_list.append(object)

    for i in range(len(ride_list)):
        ride = ride_list[i]
        object_list.append(ride)

    patron_list = assign_patron_list(patron_list,no_of_people,color_list,ride_list)

    simulate(ride_list,patron_list,object_list,patron_exit_list)

def assign_patron_list(patron_list,no_of_people,color_list,ride_list):
    for _ in range(no_of_people):
        #Assign initial inputs to people
        step_size = random.randint(10,15)
        size = random.randint(2,5)
        color = random.choice(["blue","pink"])
        person = Person(0,150,color,size,step_size)
        patron_list.append(person)
    
    for person in patron_list:
        #Initially asign a ride to a person
        ride_choice = random.choice(ride_list)
        person.insert_ride(ride_choice)
    return patron_list

def batch_mode(arguments):
    color_list = ["red","blue","yellow", "green","orange","purple","gold","lightblue","pink","cyan"]
    positions = [[25+1,200,50,50],[150+2,210,50,50],[300,200,50,50],[25+1,50,50,50],[150+2,30,50,50],[300,50,50,50]]
    object_positions = [[150,110,100,80]]
    ride_list = []
    patron_list = []
    object_list = []
    patron_exit_list = []
    csv_list = []
    file_name = arguments[2]
    with open(file_name) as file:
        reader = csv.DictReader(file)
        for row in reader:
            csv_list.append({"balloon_no": row["balloon_no"],"wheel_no" : row["wheel_no"],"pirate_no": row["pirate_no"],"person_no" : row["person_no"]})
    
    balloon_no = csv_list[0]["balloon_no"]
    wheel_no = csv_list[0]["wheel_no"]
    pirate_no = csv_list[0]["pirate_no"]
    person_no = csv_list[0]["person_no"]

    balloon_no = validate_int(balloon_no, "balloon_no")
    wheel_no = validate_int(wheel_no,"wheel_no")
    pirate_no = validate_int(pirate_no, "pirate_no")
    person_no = validate_int(person_no, "person_n")

    no_of_rides = balloon_no + wheel_no +pirate_no
    if no_of_rides > 6 or no_of_rides < 2:
        sys.exit("Please ensure that their is a minimum number of 2 rides and a maximum of 6 rides.")
    if person_no > 60 or person_no < 20:
        sys.exit("Please ensure that the maximum number of people is 60 and the minimum number is 20.")

    balloon_count =  wheel_count = pirate_count = person_count = 0
    for i in range(no_of_rides):
        ride_input = positions[i]
        xpos = ride_input[0]
        ypos = ride_input [1]
        width = ride_input [2]
        height = ride_input [3]
        
        if balloon_count < balloon_no:
            balloon_color = random.choice(color_list)
            frame_color = random.choice(color_list)
            balloon = Balloon(xpos,ypos,width,height,balloon_color,frame_color)
            ride_list.append(balloon)
            balloon_count += 1
            
        elif wheel_count < wheel_no:
            cubicles = random.randint(4,8)
            frame_color = random.choice(color_list)
            wheel = Wheel(xpos,ypos,width,height,cubicles,frame_color)
            ride_list.append(wheel)
            wheel_count += 1

        elif pirate_count < pirate_no:
            ship_color = random.choice(color_list)
            frame_color = random.choice(color_list)
            pirate = Pirate(xpos,ypos,width,height,ship_color,frame_color)
            ride_list.append(pirate)
            pirate_count += 1
    
    for i in range(len(object_positions)):
        object_input = object_positions[i]
        xpos = object_input[0]
        ypos = object_input [1]
        width = object_input [2]
        height = object_input [3]
        object = Ride(xpos,ypos,width,height)
        object_list.append(object)

    for i in range(len(ride_list)):
        ride = ride_list[i]
        object_list.append(ride)


    patron_list = assign_patron_list(patron_list,person_no,color_list,ride_list)
    simulate(ride_list,patron_list,object_list,patron_exit_list)

    
    
    


    print("Batch mode")
    sys.exit()
    
def validate_int(number, variable):
    try:
        return int(number)
    except ValueError:
        sys.exit(f"Please ensure that '{variable}' is an integer")
def plot_area(i,noon,night):
    """
    Used to plot the terrain.
    """
    #object_positions = [[150,110,90,70]]
    ax = plt.gca()
    img = pimg.imread("background.png")
    img = img[::-1]
    plt.xlim(0,400)
    plt.ylim(0,300)
    plt.title(f"Showground, Timestep {i}")
    if i >= night:
        ax.add_patch(patches.Rectangle((0, 0), 400, 300, facecolor='black', alpha=0.4))
    elif i >= noon:
        ax.add_patch(patches.Rectangle((0, 0), 400, 300, facecolor='yellow', alpha=0.2))
    plt.imshow(img, origin="upper")

    plt.plot([150,150+90,150+90,150,150],[110,110,110+70,110+70,110])
    plt.pause(0.25)
    plt.cla()
    plt.show()

def get_color():
    color_options = "\nType the relevant letter for the following colors (default/invalid is pink)" \
    "\n Red     -   R" \
    "\n Blue    -   B" \
    "\nYellow   -   Y" \
    "\nPink     -   P" \
    "\nGreen    -   G" \
    "\nBlack    -   K" \
    "\nOrange   -   O\n"
    color = input(color_options).upper()
    match color:
        case "R":
            return "red"
        case "B":
            return "blue"
        case "Y":
            return "yellow"
        case "G":
            return "green"
        case "P":
            return "pink"
        case "K":
            return "black"
        case "O":
            return "orange"
        case _:
            return "pink"
    
def simulate(ride_list,patron_list,object_list,patron_exit_list):
    n = 100
    noon = n/2
    night = 3 *n/4
    exit_pos = [400,150]
    plt.ion()
    for i in range(n): #Simulation 
        plot_area(i,noon,night) #plot the terrain
        for ride in ride_list: # plot the rides 
            ride.plot_me(plt)
            if ride.ride_full() and ride.is_animated() == False: # If the queue is full and the ride isnt animated
                ride_max = ride.get_limit()
                for _ in range(ride_max): #Input the people in the queue inside the ride
                    patron = ride.remove_queue()
                    ride.insert_person(patron)
                ride.set_animated(True) #  set ride.animating to be True 
            if ride.is_animated() ==  True: 
                ride_count = ride.get_count()
                ride.step_changes() # Update animation of the ride 
                if ride_count < 10: 
                    ride_count += 1
                    ride.set_count(ride_count)
                
                else: # initialize count back to zero and set make ride.animating = false
                    ride_count = 0
                    ride.set_count(ride_count)
                    ride.set_animated(False)
                    ride_max = ride.get_limit()
                    for _ in range(ride_max):
                        #put the patrons back into the world map
                        passenger = ride.remove_passenger()
                        ride_choice = random.choice(ride_list)
                        passenger.insert_ride(ride_choice)
                        patron_list.append(passenger)
                    ride.reset() # Put the ride back to its original state
                    
            ride_queue = ride.get_queue()    
            for patrons in ride_queue:
                #plot patrons inside the queue
                patrons.plot_me(plt)
        if i >= night:
            for person in patron_list:
                patron_exit_list.append(person)
                patron_list.remove(person)
            for ride in ride_list:
                ride_queue = ride.get_queue()
                for person in ride_queue:
                    patron_exit_list.append(person)
                    ride_queue.remove(person)
        for person in patron_list:
            #plot patrons inside the world map
            person.plot_me(plt)
            if person.get_destination():
                #update the person's position if they havent reached their ride/destination
                person.step_change(object_list)
            if person.get_destination() == False:
                #insert the person into their relevant ride queue if they have reached their destination
                person_ride = person.get_ride()
                person_ride.insert_queue(person)
                patron_list.remove(person)
        for person in patron_exit_list:
            if person.get_exit():
                patron_exit_list.remove(person)
            else:
                person.plot_me(plt)
                person.go_exit(exit_pos[0],exit_pos[1],object_list)

        
        plt.pause(0.005)
    plt.ioff()
    sys.exit()

if __name__ == "__main__":
    random.seed(1)
    main()


