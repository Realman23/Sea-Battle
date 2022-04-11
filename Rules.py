from termcolor import colored
class Rules:
    def notes(self):
        print("\nWelcome to the rules and designations of our game, they are pretty simple")
        print("\n----------------------")
        print(colored("Rules:", "green"))
        print("----------------------\n")
        print("1) Given two fields with randomly placed ships for both players, players will not be able to see both their own ships and the enemy (for more interest).")
        print("2) Each player has ten ships (1x4 pixels, 2x3 pixels, 3x2 pixels, 4x1 pixels).")
        print("3) The coordinates are selected by first typing the coordinates on the x-axis" + colored(" (A-J) ","blue") + "then on the y-axis " + colored("(1-9)", "green") + ". Coordinates must be written with a space between x and y values. For example, the coordinates might look like this: " + colored("E 9","blue")  + ".")
        print("4) Each player takes turns hitting the enemy field, choosing the necessary coordinates.")
        print("5) If the player hit some enemy ship, then this place is shown on the field with " + colored("X", "magenta") + ". So the player beats until he misses, then the turn passes to another player.")
        print("6) A ship is considered sunk if all places around it at a distance of one pixel along the perimeter are painted over with a white circle " + colored("(0)", "white") + ".")
        print("7) The winner is the player who first sinks all enemy ships, that is, scores 20 " + colored("X", "magenta") + "'s.")
        print("8) Enjoy!")
        print("9) For any questions, bugs, new ideas: Realman#4585, Андрюшка#8543\n")
        print("\n----------------------")
        print(colored("Designations:", "green"))
        print("----------------------\n")
        print(colored("A-J", "blue") + " - x-axis coordinates of ships")
        print(colored("1-9", "green") + " - y-axis coordinates of ships")
        print(colored("X", "magenta") + " - damaged place of the ship")
        print(colored("O", "white") + " - missed place")
        return "* - field`s untouched place\n"
        
    