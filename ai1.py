import numpy as np
import random
# Connect four "AI". Checks if wins by one move, otherwise plays randomly.

def play_move1(grid, heights, coords):
    for i in range(7):
        grid_copy = np.copy(grid)
        if heights[i] < 6:
            grid_copy[5-heights[i]][i] = len(coords)%2+1
            is_win = check_win(grid_copy, 5-heights[i], i)
            if is_win:
                return i
    while True:
        rand = random.randint(0, 6)
        if heights[rand] < 6:
            return rand

def check_win(grid, move_x, move_y):
    player = grid[move_x, move_y]
    length = 1
    i = 1
    while True:
        if (move_x+i >= len(grid)): break
        if grid[move_x+i, move_y] != player: break
        i += 1
        length += 1
        if length == 4: return True
    i = 1
    while True:
        if (move_x-i < 0): break
        if grid[move_x-i, move_y] != player: break
        i += 1
        length += 1
        if length == 4: return True
    length = 1
    i = 1
    while True:
        if (move_y+i >= len(grid[1])): break
        if grid[move_x, move_y+i] != player: break
        i += 1
        length += 1
        if length == 4: return True
    i = 1
    while True:
        if (move_y-i < 0): break
        if grid[move_x, move_y-i] != player: break
        i += 1
        length += 1
        if length == 4: return True
    length = 1
    i = 1
    while True:
        if (move_x+i >= len(grid) or move_y+i >= len(grid[1])): break
        if grid[move_x+i, move_y+i] != player: break
        i += 1
        length += 1
        if length == 4: return True
    i = 1
    while True:
        if (move_x-i < 0 or move_y-i < 0): break
        if grid[move_x-i, move_y-i] != player: break
        i += 1
        length += 1
        if length == 4: return True
    length = 1
    i = 1
    while True:
        if (move_x+i >= len(grid) or move_y-i < 0): break
        if grid[move_x+i, move_y-i] != player: break
        i += 1
        length += 1
        if length == 4: return True
    i = 1
    while True:
        if (move_x-i < 0 or move_y+i >= len(grid[1])): break
        if grid[move_x-i, move_y+i] != player: break
        i += 1
        length += 1
        if length == 4: return True
    return False
            
    
