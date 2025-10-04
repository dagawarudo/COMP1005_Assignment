#
# Student Name : Dayyaan Ishmael
# Student ID   : 23549654
#
# task3.py - testing simulation of rides in a showground
#
import matplotlib.pyplot as plt
from FerrisWheel import FerrisWheel

wheel1 = FerrisWheel(40,40, 20, 20,5,"purple","black")
wheel2 = FerrisWheel(90,10,40,40,8,"green","blue")
wheel3 = FerrisWheel(140,75,75,75,3,"red","gold")

wheel_list = [wheel1,wheel2,wheel3]

plt.ion()
plt.title("Showground")

for t in range(30):
    for i in wheel_list :
        i.step_changes()
        i.plot_me(plt)
    plt.xlim(0,300)
    plt.ylim(0,300)
    plt.title("Showground - Task 3")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.pause(0.5)
    plt.cla()
    plt.show()



plt.ioff()
