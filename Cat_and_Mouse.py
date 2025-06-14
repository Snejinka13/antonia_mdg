# -*- coding: utf-8 -*-
"""
Cat and Mouse Chase Game 

Created on Sat Jun 14 07:32:02 2025

@author: Antonia Doncheva
"""

import random
import time

GRID_SIZE = 5 # define the grid size
cat = [0, 0]
mouse = [random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1)]

def main():
    print("Welcome to the 🐱 and 🐭 chase game!")
    while cat != mouse:
        clear_screen()
        print("🐱 Cat is chasing the 🐭 mouse!\n")
        print_grid()
        move_mouse()
        move_cat()
        time.sleep(0.5)
        
    clear_screen()
    print_grid()
    print("The cat caught the mouse! =^.^=")

def clear_screen():
    print("\033[H\033[J", end="") 

# create the grid for the game
def print_grid():
    # loop over rows in the greid
    for i in range(GRID_SIZE):
        row = ''
        # loop over columns in the grid
        for j in range(GRID_SIZE):
            if [i, j] == cat:
                row += '😺 '
            elif [i, j] == mouse:
                row += '🐭 '
            else:
                row += '.  '
        print(row)
    print()

# define the mouse's random moves in the grid
def move_mouse():
    directions = [[0,1], [1,0], [0,-1], [-1,0]]
    dx, dy = random.choice(directions)
    mouse[0] = max(0, min(GRID_SIZE - 1, mouse[0] + dx))
    mouse[1] = max(0, min(GRID_SIZE - 1, mouse[1] + dy))

# define the cat's moves so that it is following the mouse
def move_cat():
    if cat[0] < mouse[0]: cat[0] += 1
    elif cat[0] > mouse[0]: cat[0] -= 1
    if cat[1] < mouse[1]: cat[1] += 1
    elif cat[1] > mouse[1]: cat[1] -= 1

if __name__ == '__main__':
    main()