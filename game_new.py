import sys, pygame, os
import numpy as np
pygame.init()

# The file for playing IQ Chess (Connect 4)

screen = pygame.display.set_mode((770, 700))
background_color = 0, 0, 255

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
heights = np.zeros(7)
# Locations of every disk on screen 
coords = []
# Status of every point on the playing grid
# 0: empty, 1: red disk, 2: yellow disk
grid = np.zeros((7, 6))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print np.transpose(grid)
            sys.exit()
        # Adding disks to each column
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                if(heights[0] < 6):
                    grid[0, 5-heights[0]] = len(coords)%2+1
                    coords.append((45+70, int(600-90*heights[0])))
                    heights[0] += 1
            if event.key == pygame.K_2:
                if(heights[1] < 6):
                    grid[1, 5-heights[1]] = len(coords)%2+1
                    coords.append((135+70, int(600-90*heights[1])))
                    heights[1] += 1
            if event.key == pygame.K_3:
                if(heights[2] < 6):
                    grid[2, 5-heights[2]] = len(coords)%2+1
                    coords.append((225+70, int(600-90*heights[2])))
                    heights[2] += 1
            if event.key == pygame.K_4:
                if(heights[3] < 6):
                    grid[3, 5-heights[3]] = len(coords)%2+1
                    coords.append((315+70, int(600-90*heights[3])))
                    heights[3] += 1
            if event.key == pygame.K_5:
                if(heights[4] < 6):
                    grid[4, 5-heights[4]] = len(coords)%2+1
                    coords.append((405+70, int(600-90*heights[4])))
                    heights[4] += 1
            if event.key == pygame.K_6:
                if(heights[5] < 6):
                    grid[5, 5-heights[5]] = len(coords)%2+1
                    coords.append((495+70, int(600-90*heights[5])))
                    heights[5] += 1
            if event.key == pygame.K_7:
                if(heights[6] < 6):
                    grid[6, 5-heights[6]] = len(coords)%2+1
                    coords.append((585+70, int(600-90*heights[6])))
                    heights[6] += 1
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
            pygame.draw.line(screen, (150,150,150), (70, 195+90*i), (700, 195+90*i), 3)
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
        
