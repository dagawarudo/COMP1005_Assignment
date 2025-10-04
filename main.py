
#
# Student Name : Dayyaan Ishmael
# Student ID   : 23549654
#
# showDemo.py - testing simulation of rides in a showground
#
import matplotlib.pyplot as plt
from Pirate  import Pirate
def main() :
    plot_area()

def plot_area(time_step = 10, max_x = 200, max_y = 200,fill_color = "green"):
    for time in range(time_step):
        plt.title(f"Theme Park - Time Step {time+1}")
        plt.xlim(max_x)
        plt.ylim(max_y)
        plt.fill(fill_color)
        plt.show()

def get_color(color):
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
    plt.ion()
    color_options = "\nType the relevant letter for the following colors (default is pink)\nRed\t-\tR\nBlue\t-\tB\nYellow\t-\tY"
    main()


