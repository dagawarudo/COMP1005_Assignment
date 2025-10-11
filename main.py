
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
    color_list = ["red","blue","yellow", "green","orange"]
    positions = [[25,200,50,50],[100,200,50,50],[175,200,50,50],[25,50,50,50],[100,50,50,50],[175,50,50,50]]
    ride_list = []
    patron_list = []
    patron_exit_list = []
    
    no_of_rides = get_int("How many rides would you like (a minimum of 2  and a maximum of 6 rides) ",2,6)
    
    for i in range(no_of_rides):
        ride_options = "Hot Air Balloon     -   B\n" \
        "Ferris Wheel   -   W\n" \
        "Pirate Ship    -   P\n"
        ride = get_ride(ride_options, positions[i])
        ride_list.append(ride)
    
    no_of_people = get_int("How many people would you like (a minimum of 10 and a maximum of 50 people) ",10,50)
    
    for _ in range(no_of_people):
        step_size = random.randint(5,10)
        size = random.randint(5,10)
        color = random.choice(color_list)
        person = Person(0,0,color,size,step_size)
        patron_list.append(person)
    
    for person in patron_list:
        #Initially asign a ride to a person
        ride_choice = random.choice(ride_list)
        person.insert_ride(ride_choice)
    #TODO 


    plt.ion()
    for i in range(100):
        plot_area(i)
        for ride in ride_list:
            ride.plot_me(plt)
        for person in patron_list:
            person.plot_me(plt)
            if person.get_destination():
                person.step_change(ride_list)
        print(f"{i} th attempt ")
        plt.pause(0.005)
    plt.ioff()
    sys.exit()

def batch_mode():
    print("Batch mode")
    sys.exit()

def plot_area(i):
    plt.xlim(0,300)
    plt.ylim(0,300)
    plt.title("Showground")
    if i >= 5:
        plt.gca().set_facecolor('lightyellow') 
    else:
        plt.gca().set_facecolor("lightgreen")
    plt.pause(0.25)
    plt.cla()
    plt.show()

def get_color():
    color_options = "\nType the relevant letter for the following colors (default is pink)\nRed\t-\tR\nBlue\t-\tB\nYellow\t-\tY"
    color = input(color_options)
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


