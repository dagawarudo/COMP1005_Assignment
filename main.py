
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
import sys
import matplotlib.pyplot as plt
import random  

def main() :
    if len(sys.argv) < 2:
        sys.exit("For interactive mode type in \'-i\' , for batch mode type in \'-f\' and the relevant CSV file ")
    elif sys.argv[1] == "-i":
        interactive_mode()
    elif sys.argv[1] == "-f":
        batch_mode()
    else:
        sys.exit("For interactive mode type in \'-i\' , for batch mode type in \'-f\' and the relevant CSV file ")
def get_int(text, less, greater):
    while True:
        try:
            n = int(input(text))
            if n < less or n > greater:
                raise ValueError
        except ValueError:
            print("Please select the valid inputs")
        else:
            return n 
        
def get_ride(ride_options, ride_input):
    while True:
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
    color_list = ["red","blue","yellow", "green","orange","purple","gold","lightblue","pink","cyan"]
    positions = [[25,200,50,50],[150,200,50,50],[275,200,50,50],[25,50,50,50],[150,50,50,50],[275,50,50,50]]
    ride_list = []
    patron_list = []
    patron_exit_list = []
    
    no_of_rides = get_int("How many rides would you like (a minimum of 2  and a maximum of 6 rides) ",2,6)
    
    for i in range(no_of_rides):
        ride_options = "\nHot Air Balloon     -   B\n" \
        "Ferris Wheel   -   W\n" \
        "Pirate Ship    -   P\n"
        ride = get_ride(ride_options, positions[i])
        ride_list.append(ride)
    
    no_of_people = get_int("How many people would you like (a minimum of 20 and a maximum of 60 people) ",20,60)
    
    for _ in range(no_of_people):
        step_size = random.randint(10,15)
        size = random.randint(1,2)
        color = random.choice(color_list)
        person = Person(0,150,color,size,step_size)
        patron_list.append(person)
    
    for person in patron_list:
        #Initially asign a ride to a person
        ride_choice = random.choice(ride_list)
        person.insert_ride(ride_choice)
    #TODO 


    plt.ion()
    for i in range(100):
        #TODO update transformation once patrons exit
        plot_area(i)
        for ride in ride_list:
            ride.plot_me(plt)
            if ride.ride_full() and ride.is_animated() == False:
                ride_max = ride.get_limit()
                for _ in range(ride_max):
                    patron = ride.remove_queue()
                    ride.insert_person(patron)
                ride.set_animated(True)
            if ride.is_animated() ==  True:
                ride_count = ride.get_count()
                ride.step_changes()
                if ride_count < 10:
                    ride_count += 1
                    ride.set_count(ride_count)
                
                else:
                    ride_count = 0
                    ride.set_count(ride_count)
                    ride.set_animated(False)
                    ride_max = ride.get_limit()
                    for _ in range(ride_max):
                        passenger = ride.remove_passenger()
                        ride_choice = random.choice(ride_list)
                        passenger.insert_ride(ride_choice)
                        patron_list.append(passenger)
                    ride.reset()
                    
            ride_queue = ride.get_queue()    
            for patrons in ride_queue:
                patrons.plot_me(plt)
        for person in patron_list:
            person.plot_me(plt)
            if person.get_destination():
                person.step_change(ride_list)
            if person.get_destination() == False:
                person_ride = person.get_ride()
                person_ride.insert_queue(person)
                patron_list.remove(person)

        print(f"{i+1} th attempt ")
        plt.pause(0.005)
    plt.ioff()
    sys.exit()

def batch_mode():
    print("Batch mode")
    sys.exit()

def plot_area(i):
    plt.xlim(0,400)
    plt.ylim(0,300)
    plt.title("Showground")
    if i >= 5:
        plt.gca().set_facecolor('lightgreen') 
    else:
        plt.gca().set_facecolor("lightgreen")
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
    

if __name__ == "__main__":
    random.seed(1)
    main()


