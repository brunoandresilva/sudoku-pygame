from asyncio.windows_events import NULL
from cmath import rect
from msvcrt import kbhit
import sys
import pygame
from random import sample
import random
import keyboard


base  = 3
side  = base*base
width = 550
background_color = (135, 218, 149)
grid_element_color = (0, 0, 0)
inserted_elem_color = (0, 0, 255)

# grid that will be shown in the screen
display_grid = [ [0 for c in range(0, 9)] for r in range(0, 9) ]
ind_x, ind_y = 0, 0
error_count = 0


# randomize rows, columns and numbers (of valid base pattern)
def shuffle(s): 
    return sample(s,len(s)) 

# pattern for a baseline valid solution
def pattern(r,c): 
    return (base*(r%base)+r//base+c)%side

def updateGrid(win, rectangle):
    win.fill(background_color)

    for i in range(0, 10):
        if i % 3 == 0:
            pygame.draw.line(win, (0, 0, 0), (50 + 50*i, 50), (50 + 50*i, 500), 4)
            pygame.draw.line(win, (0, 0, 0), (50, 50 + 50*i), (500, 50 + 50*i), 4)
        pygame.draw.line(win, (0, 0, 0), (50 + 50*i, 50), (50 + 50*i, 500), 2)
        pygame.draw.line(win, (0, 0, 0), (50, 50 + 50*i), (500, 50 + 50*i), 2)

    pygame.draw.rect(win, (33, 232, 67), rectangle)

    grid_font = pygame.font.SysFont('Comic Sans MS', 35)
    for i in range(0, len(display_grid[0])):
        for j in range(0, len(display_grid[0])):
            if(0 < display_grid[i][j] < 10):
                value = grid_font.render(str(display_grid[i][j]), True, grid_element_color)
                win.blit(value, ((j+1)*50 + 15, (i+1)*50 ))

    # error count and timer

    ui_font = pygame.font.SysFont('Comic Sans MS', 20)
    err_count = ui_font.render(("Erros: " + str(error_count)), True, grid_element_color)
    win.blit(err_count, (30, 10))

    pygame.display.update()

def drawGrid(board, win):
    # DRAWING THE GRID
    win.fill(background_color)

    for i in range(0, 10):
        if i % 3 == 0:
            pygame.draw.line(win, (0, 0, 0), (50 + 50*i, 50), (50 + 50*i, 500), 4)
            pygame.draw.line(win, (0, 0, 0), (50, 50 + 50*i), (500, 50 + 50*i), 4)
        pygame.draw.line(win, (0, 0, 0), (50 + 50*i, 50), (50 + 50*i, 500), 2)
        pygame.draw.line(win, (0, 0, 0), (50, 50 + 50*i), (500, 50 + 50*i), 2)

    

    # POPULATING THE GRID

    # choosing what numbers are actually being displayed in the beginning
    rand_coords = []        
    while len(rand_coords) < 17:
        x = random.randint(0, 8)
        y = random.randint(0, 8)
        if (x, y) not in rand_coords:
            rand_coords.append((x, y))

    
    for x, y in rand_coords:
        display_grid[x][y] = board[x][y]
        print(x, y)    # LOGTEST
        print((str(board[x][y])))  # LOGTEST

    for line in display_grid:  # LOGTEST
        print(line)

    myfont = pygame.font.SysFont('Comic Sans MS', 35)
    for i in range(0, len(display_grid[0])):
        for j in range(0, len(display_grid[0])):
            if(0 < display_grid[i][j] < 10):
                value = myfont.render(str(display_grid[i][j]), True, grid_element_color)
                win.blit(value, ((j+1)*50 + 15, (i+1)*50 ))

    pygame.display.update()

def main():
    global error_count
    # SUDOKU SOLUTION BOARD
    rBase = range(base) 
    rows  = [ g*base + r for g in shuffle(rBase) for r in shuffle(rBase) ] 
    cols  = [ g*base + c for g in shuffle(rBase) for c in shuffle(rBase) ]
    nums  = shuffle(range(1,base*base+1))

    # produce board using randomized baseline pattern (SOLUTION)
    board = [ [nums[pattern(r,c)] for c in cols] for r in rows ]
    

    for line in board: print(line)

    pygame.init()
    win = pygame.display.set_mode((width, width))
    pygame.display.set_caption("Sudoku Rústico")    
    drawGrid(board, win)

    while True:
        for e in pygame.event.get():
            
            if e.type == pygame.QUIT:
                pygame.quit()
                return
            if e.type == pygame.MOUSEBUTTONUP:
                # MOUSE POSITION
                x, y = pygame.mouse.get_pos()
                ind_x, ind_y = int(x / 50 - 1), int(y / 50 - 1)
                rectangle = pygame.Rect(((ind_x + 1) * 50), ((ind_y + 1) * 50), 48, 48)
                updateGrid(win, rectangle)
                pygame.display.update()
                
            if e.type == pygame.KEYDOWN:
                print("A key has been pressed")
                if e.key == pygame.K_1:
                    if board[ind_y][ind_x] == 1:
                        display_grid[ind_y][ind_x] = 1
                    else: 
                        error_count += 1
                    updateGrid(win, rectangle)
                if e.key == pygame.K_2:
                    if board[ind_y][ind_x] == 2:
                        display_grid[ind_y][ind_x] = 2
                    else: 
                        error_count += 1
                    updateGrid(win, rectangle)
                if e.key == pygame.K_3:
                    if board[ind_y][ind_x] == 3:
                        display_grid[ind_y][ind_x] = 3
                    else: 
                        error_count += 1
                    updateGrid(win, rectangle)
                if e.key == pygame.K_4:
                    if board[ind_y][ind_x] == 4:
                        display_grid[ind_y][ind_x] = 4
                    else: 
                        error_count += 1
                    updateGrid(win, rectangle)
                if e.key == pygame.K_5:
                    if board[ind_y][ind_x] == 5:
                        display_grid[ind_y][ind_x] = 5
                    else: 
                        error_count += 1
                    updateGrid(win, rectangle)
                if e.key == pygame.K_6:
                    if board[ind_y][ind_x] == 6:
                        display_grid[ind_y][ind_x] = 6
                    else: 
                        error_count += 1
                    updateGrid(win, rectangle)
                if e.key == pygame.K_7:
                    if board[ind_y][ind_x] == 7:
                        display_grid[ind_y][ind_x] = 7
                    else: 
                        error_count += 1
                    updateGrid(win, rectangle)
                if e.key == pygame.K_8:
                    if board[ind_y][ind_x] == 8:
                        display_grid[ind_y][ind_x] = 8
                    else: 
                        error_count += 1
                    updateGrid(win, rectangle)
                if e.key == pygame.K_9:
                    if board[ind_y][ind_x] == 9:
                        display_grid[ind_y][ind_x] = 9
                    else: 
                        error_count += 1
                    updateGrid(win, rectangle)

                
                

    

if __name__ == "__main__":
    main()