#
# Student Name : Dayyaan Ishmael
# Student ID   : 23549654
#
# task3.py - testing simulation of rides in a showground
#
import matplotlib.pyplot as plt
from HotAirBalloon import HotAirBalloon as Balloon

wheel1 = Balloon(40,40, 20, 20,"purple","black")
wheel2 = Balloon(90,10,40,40,"green","blue")
wheel3 = Balloon(140,75,75,75,"red","gold")

wheel_list = [wheel1,wheel2,wheel3]

plt.ion()
plt.title("Showground")

for t in range(15):
    for i in wheel_list :
        i.plot_me(plt)
        i.step_changes()
    plt.xlim(0,300)
    plt.ylim(0,300)
    plt.title("Showground - Task 3")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.pause(0.5)
    plt.cla()
    plt.show()



plt.ioff()
