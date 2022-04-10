import random
import math
from termcolor import colored

v = 0


def main():

    letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    player1, player2 = [], []
    player1_hits, player1_misses, player2_hits, player2_misses = [], [], [], []

    def create_game(lst):

        def check(cell):
            if not 0 < cell[0] < 10 or not 0 < cell[1] < 10:
                return False
            potential_cells = [[cell[0], cell[1]],
                               [cell[0] - 1, cell[1] + 1],
                               [cell[0], cell[1] + 1],
                               [cell[0] + 1, cell[1] + 1],
                               [cell[0] - 1, cell[1]],
                               [cell[0] + 1, cell[1]],
                               [cell[0] - 1, cell[1] - 1],
                               [cell[0], cell[1] - 1],
                               [cell[0] + 1, cell[1] - 1]]
            for w in potential_cells:
                if w in lst:
                    return False
            return True

        def create_cell():
            cell = [random.randint(1, 10), random.randint(1, 10)]

            while not check(cell):
                cell = [random.randint(1, 10), random.randint(1, 10)]

            return cell

        def next_cell(cell, n):
            next_part = [[cell[0] - n, cell[1]],
                         [cell[0], cell[1] - n],
                         [cell[0] + n, cell[1]],
                         [cell[0], cell[1] + n]]

            a = random.choice(next_part)

            if check(a):
                return a

            for w in next_part:
                if check(w):
                    return w

        def create_ship(length):

            if length == 1:
                cell1 = create_cell()
                lst.append(cell1)

            elif length == 2:

                cell1 = create_cell()
                cell2 = next_cell(cell1, 1)

                lst.append(cell1)
                lst.append(cell2)

            elif length == 3:

                cell1 = create_cell()
                cell2 = next_cell(cell1, 2)
                cell3 = [int((cell1[0] + cell2[0]) / 2), int((cell1[1] + cell2[1]) / 2)]

                lst.append(cell1)
                lst.append(cell2)
                lst.append(cell3)

            elif length == 4:

                cell1 = create_cell()
                cell2 = next_cell(cell1, 3)
                cell3 = [math.ceil((cell1[0] + cell2[0]) / 2), math.ceil((cell1[1] + cell2[1]) / 2)]
                cell4 = [math.floor((cell1[0] + cell2[0]) / 2), math.floor((cell1[1] + cell2[1]) / 2)]

                lst.append(cell1)
                lst.append(cell2)
                lst.append(cell3)
                lst.append(cell4)

        try:
            create_ship(4)
            create_ship(3)
            create_ship(3)
            create_ship(2)
            create_ship(2)
            create_ship(2)
            create_ship(1)
            create_ship(1)
            create_ship(1)
            create_ship(1)

        except Exception:
            print("Didn't find place for all ships!")

    def show(player):
        print()
        print("Player 1") if player == player1 else print("Player 2")
        print()

        print("  ", end="")
        for i in range(10):
            print(colored(i, 'green'), end=" ")

        for i in range(1, 11):
            print()
            print(colored(letters[i - 1], 'blue'), end=" ")
            for j in range(1, 11):

                if [j, i] in player:
                    print("\33[95;1;5mX \33[0m", end="")
                else:
                    print(colored("* ", "white"), end="")

        print()

    def show_field(x, y):
        print()
        print("  ", end="")
        for i in range(10):
            print(colored(i, 'green'), end=" ")

        for i in range(1, 11):
            print()
            print(colored(letters[i - 1], 'blue'), end=" ")
            for j in range(1, 11):

                if [j, i] in x:
                    print("\33[95;1;5mX \33[0m", end="")
                elif [j, i] in y:
                    print("\33[37;1;5mO \33[0m", end="")
                else:
                    print(colored("* ", "white"), end="")
        print()
        print()

    def play():
        global player1_hits, player1_misses, player2_hits, player2_misses, v
        RED = "\x1b[1;31;40m"

        print()
        print("The game has stared, choose your nicknames")
        print()
        p1 = input("Enter first player's nickname : ")
        p2 = input("Enter second player's nickname : ")
        p1 = "Anonymus_1" if not p1 else p1
        p2 = "Anonymus_2" if not p2 else p2

        player1_hits, player1_misses = [], []
        player2_hits, player2_misses = [], []

        while True:

            def chk():

                for p in x:
                    close_ceil = [[p[0] - 1, p[1]],
                                  [p[0], p[1] - 1],
                                  [p[0] + 1, p[1]],
                                  [p[0], p[1] + 1]]
                    for i in close_ceil:
                        if i in z and i not in x:
                            return True
                return False

            def erase():
                for r in x:
                    pot_cells = [[r[0] - 1, r[1] + 1],
                                 [r[0], r[1] + 1],
                                 [r[0] + 1, r[1] + 1],
                                 [r[0] - 1, r[1]],
                                 [r[0], r[1]],
                                 [r[0] + 1, r[1]],
                                 [r[0] - 1, r[1] - 1],
                                 [r[0], r[1] - 1],
                                 [r[0] + 1, r[1] - 1]]
                    for i in pot_cells:
                        if i not in z:
                            y.append(i)

            def pass_cell(player):

                turn = input(f"{player}'s turn:")
                while len(turn) != 3 or not turn[0].isalpha() or turn[0].upper() not in letters \
                        or turn[1] != " " or not turn[2].isdigit():
                    turn = input(f"{player}'s turn:")
                turn = turn.split(" ")
                a = [int(turn[1]) + 1, letters.index(turn[0].upper()) + 1]
                return a

            x, y, z, a = player1_hits, player1_misses, player2, [1, 1]

            if v % 2 == 0:
                x, y, z = player1_hits, player1_misses, player2
                print()
                print("-----------------------------------------------")
                print()
                print(colored(f"{p2}`s", "red") + " field")
                show_field(x, y)
                a = pass_cell(p1)

            elif v % 2 == 1:
                x, y, z = player2_hits, player2_misses, player1
                print()
                print("-----------------------------------------------")
                print()
                print(colored(f"{p1}`s", "red") + " field")
                show_field(x, y)
                a = pass_cell(p2)

            if a in z:
                if a not in x:
                    x.append(a)

            else:
                y.append(a)
                show_field(x, y)
                # time.sleep(3)
                v += 1
            if not chk():
                erase()

            if len(player1_hits) == 1:
                show_field(player1_hits, player1_misses)
                print(colored(f"{p1}","red") + " won!")
                print()
                break

            if len(player2_hits) == 1:
                show_field(player2_hits, player2_misses)
                print(colored(f"{p2}","red") + " won!")
                print()
                break

    create_game(player1)
    create_game(player2)

    def rules():
        pass

    # STARTING GAME
    print("-------------------------------------------------------------------------")
    print(" .|'''|                      ||'''|,            ||      ||    '||`")
    print(" ||                          ||   ||            ||      ||     ||")    
    print("`|'''|,  .|''|,   '''|.      ||;;;;    '''|.  ''||''  ''||''   ||  .|''|,")   
    print(" .   ||  ||..||  .|''||      ||   ||  .|''||    ||      ||     ||  ||..||")      
    print(" |...|'  `|...   `|..||      ||...|'  `|..||.   `|..'   `|..'  ||  `|...")
    print("-------------------------------------------------------------------------")       

    print('Welcome to our self-build Console Game "SEA BATTLE"!')
    print()
    inp = input("Choose an action: 'Play' / 'Show' / 'Rules' / 'Quit' : ").lower()

    while inp not in ["show", "play", "rules", "quit"]:
        print("Wrong command!")
        inp = input("Enter action: 'Play' / 'Show' / 'Quit' : ").lower()

    if inp == "show":
        show(player1)
        show(player2)

    elif inp == "play":
        play()
        if input("Do you want to play again? (Y/N): ").lower() == "y":
            main()

    elif inp == "rules":
        rules()

    elif inp == "quit":
        print("Thanks for playing! Enjoy the day!")
        quit()


if __name__ == "__main__":
    main()    
    