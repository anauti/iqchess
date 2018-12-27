#coding: utf-8
import sys, pygame, os
import numpy as np
pygame.init()
# The file for playing Connect 4. 2018, A.A.

# Handles input for putting the discs. Returns whether the game is over.
def put_disc(coords, heights, col):
    if(heights[col] >= 6):
        return False
    else:
        grid[5-heights[col]][col] = len(coords)%2+1
        coords.append((115+90*col, 600-90*heights[col]))
        is_win = check_win(grid, 5-heights[col], col)
        heights[col] += 1
    return is_win
    

# Checks if the new move creates a win condition
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

screen = pygame.display.set_mode((770, 700))
background_color = (0, 0, 255)

# Texts shown on screen 
font = pygame.font.Font(None, 32)
one = font.render('1', 1, (0, 0, 0))
two = font.render('2', 1, (0, 0, 0))
three = font.render('3', 1, (0, 0, 0))
four = font.render('4', 1, (0, 0, 0))
five = font.render('5', 1, (0, 0, 0))
six = font.render('6', 1, (0, 0, 0))
seven = font.render('7', 1, (0, 0, 0))
vuoro1 = font.render('Pelaajan 1 vuoro', 1, (255, 255, 255))
vuoro2 = font.render('Pelaajan 2 vuoro', 1, (255, 255, 255))

# Number of disks on each column
heights = np.zeros(7, dtype=np.int8)
# Locations of every disk on screen 
coords = []
# Status of every point on the playing grid
# 0: empty, 1: red disk, 2: yellow disk
grid = np.zeros((6, 7), dtype='int')
game_over = False

# Actual gameplay
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if game_over:
                    game_over = False
                    coords = []
                    grid = np.zeros((6, 7), dtype='int')
                    heights = np.zeros(7, dtype=np.int8)
        if game_over:
            continue
        # Adding disks to each column
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                game_over = put_disc(coords, heights, 0)
            if event.key == pygame.K_2:
                game_over = put_disc(coords, heights, 1)
            if event.key == pygame.K_3:
                game_over = put_disc(coords, heights, 2)
            if event.key == pygame.K_4:
                game_over = put_disc(coords, heights, 3)
            if event.key == pygame.K_5:
                game_over = put_disc(coords, heights, 4)
            if event.key == pygame.K_6:
                game_over = put_disc(coords, heights, 5)
            if event.key == pygame.K_7:
                game_over = put_disc(coords, heights, 6)
        # What to do if game is over (by win or draw)
        if game_over or len(coords) == 6*7:
            player = (len(coords)-1)%2
            if player == 0:
                color = (255,0,0)
            else:
                color = (255,255,0)
            w_font = pygame.font.Font(None, 100)
            win_text = 'Pelaaja {} voitti!'.format(player+1)
            if len(coords) == 6*7:
                win_text = 'Tasapeli!'
            winner = w_font.render(win_text, 1, (255,255,255))
            cont_text = u'Paina välilyöntiä aloittaaksesi uuden pelin.'
            cont = font.render(cont_text, 1, (255,255,255))
            pygame.draw.circle(screen, color, coords[len(coords)-1], 45, 0)
            screen.blit(winner, (140, 300))
            screen.blit(cont, (160, 650))
            pygame.display.flip()
            continue
        screen.fill(background_color)
        # Drawing disks with alternating colours
        i = 0
        for coord in coords:
            if i%2 == 0:
                color = (255,0,0)
            else:
                color = (255,255,0)
            pygame.draw.circle(screen, color, coord, 45, 0)
            i += 1
        # Drawing the grid
        for i in range(5):
            pygame.draw.line(screen, (150,150,150), (70,195+90*i), (700,195+90*i), 3)
        for i in range(8):
            pygame.draw.line(screen, (0,0,0), (70+90*i, 645), (70+90*i, 105), 3)
        pygame.draw.line(screen, (0,0,0), (70, 645), (700, 645), 3)
        # And the texts
        screen.blit(one, (45+70, 50))
        screen.blit(two, (135+70, 50))
        screen.blit(three, (225+70, 50))
        screen.blit(four, (315+70, 50))
        screen.blit(five, (405+70, 50))
        screen.blit(six, (495+70, 50))
        screen.blit(seven, (585+70, 50))
        if len(coords)%2 == 0:
            screen.blit(vuoro1, (45+70, 10))
        else:
            screen.blit(vuoro2, (45+70, 10))
            
        pygame.display.flip()
    
