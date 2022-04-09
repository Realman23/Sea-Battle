import random
import math

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

player1 = []
player2 = []

def create_game(lst):

    def check(cell):
        if not 0 < cell[0] < 10 or not 0 < cell[1] < 10:
            return False
        potential_cells = [[cell[0], cell[1]],
                           [cell[0] - 1, cell[1] + 1],
                           [cell[0], cell[1] + 1],
                           [cell[0] + 1, cell[1] + 1],
                           [cell[0] - 1, cell[1]],
                           [cell[0], cell[1]],
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

create_game(player1)
create_game(player2)

def show(player):

    print("  ", end="")
    for i in range(10):
        print(i, end=" ")

    for i in range(1, 11):
        print()
        print(letters[i - 1], end=" ")
        for j in range(1, 11):

            if [j, i] in player:
                print("\33[95mX \33[0m", end="")
            else:
                print("* ", end="")

    print()
    print()

show(player1)
show(player2)