#
# Student Name : Dayyaan Ishmael
# Student ID   : 23549654
#
# task3.py - testing simulation of rides in a showground
#
import matplotlib.pyplot as plt
import random 
from FerrisWheel import FerrisWheel
from Pirate import Pirate
from Person import Person
wheel1 = Pirate(40,40, 50, 50,"purple","black")
wheel2 = FerrisWheel(90,10,40,40,3,"green","blue")
wheel3 = FerrisWheel(140,75,75,75,8,"red","gold")
person1 = Person(0,0,"red")
person2 = Person(0,0,"blue")
person3 = Person(0,0,"green")


wheel_list = [wheel1,wheel2,wheel3]
person_list = [person1, person2, person3]
random.seed(10)
plt.ion()
plt.title("Showground")

for t in range(50):
    for i in wheel_list :
        i.plot_me(plt)
        i.step_changes()
    for p in person_list:
        p.plot_me(plt)
        if p.no_target():
            choice = random.choice(wheel_list)
            p.insert_ride(choice)
        if p.get_destination() == True :
            p.step_change(wheel_list,5)
    plt.xlim(0,300)
    plt.ylim(0,300)
    plt.title("Showground - Task 3")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.pause(0.25)
    plt.cla()
    plt.show()



plt.ioff()
