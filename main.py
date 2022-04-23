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


# randomize rows, columns and numbers (of valid base pattern)
def shuffle(s): 
    return sample(s,len(s)) 

# pattern for a baseline valid solution
def pattern(r,c): 
    return (base*(r%base)+r//base+c)%side

def main():
    # SUDOKU SOLUTION BOARD
    rBase = range(base) 
    rows  = [ g*base + r for g in shuffle(rBase) for r in shuffle(rBase) ] 
    cols  = [ g*base + c for g in shuffle(rBase) for c in shuffle(rBase) ]
    nums  = shuffle(range(1,base*base+1))

    # produce board using randomized baseline pattern
    board = [ [nums[pattern(r,c)] for c in cols] for r in rows ]

    for line in board: print(line)

    #DRAWING THE GRID
    pygame.init()
    win = pygame.display.set_mode((width, width))
    pygame.display.set_caption("Sudoku Rústico")
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
        print(x, y)
        print((str(board[x][y])))


    myfont = pygame.font.SysFont('Comic Sans MS', 35)
    for i in range(0, len(board[0])):
        for j in range(0, len(board[0])):
            for x, y in rand_coords:
                if x == i and y == j:
                    if(0 < board[i][j] < 10):
                        value = myfont.render(str(board[i][j]), True, grid_element_color)
                        win.blit(value, ((j+1)*50 + 15, (i+1)*50 ))

    pygame.display.update()


    
    while True:
        
        
        for e in pygame.event.get():
            ind_x, ind_y = 0, 0
            flag = False
            if e.type == pygame.QUIT:
                pygame.quit()
                return
            if e.type == pygame.MOUSEBUTTONUP:
                flag = True
                x, y = pygame.mouse.get_pos()
                ind_x, ind_y = int(x / 50 - 1), int(y / 50 - 1)
                print(x, y)
                print(ind_x, ind_y)
                # value = myfont.render(str(board[ind_y][ind_x]), True, inserted_elem_color)
                # win.blit(value, ((ind_x+1)*50 + 15, (ind_y+1)*50 ))
                # pygame.display.update()
                
            if flag:
                print("ENTREI")
                keys = pygame.key.get_pressed()
                if keys[pygame.K_1]:
                    value = myfont.render('1', True, inserted_elem_color)
                    win.blit(value, ((ind_x+1)*50 + 15, (ind_y+1)*50 ))
                    pygame.display.update()
                    flag = False
                elif keys[pygame.K_2]:
                    value = myfont.render('2', True, inserted_elem_color)
                    win.blit(value, ((ind_x+1)*50 + 15, (ind_y+1)*50 ))
                    pygame.display.update()
                    flag = False
                elif keys[pygame.K_3]:
                    value = myfont.render('3', True, inserted_elem_color)
                    win.blit(value, ((ind_x+1)*50 + 15, (ind_y+1)*50 ))
                    pygame.display.update()
                    flag = False
                elif keys[pygame.K_4]:
                    value = myfont.render('4', True, inserted_elem_color)
                    win.blit(value, ((ind_x+1)*50 + 15, (ind_y+1)*50 ))
                    pygame.display.update()
                    flag = False
                elif keys[pygame.K_5]:
                    value = myfont.render('5', True, inserted_elem_color)
                    win.blit(value, ((ind_x+1)*50 + 15, (ind_y+1)*50 ))
                    pygame.display.update()
                    flag = False
                elif keys[pygame.K_6]:
                    value = myfont.render('6', True, inserted_elem_color)
                    win.blit(value, ((ind_x+1)*50 + 15, (ind_y+1)*50 ))
                    pygame.display.update()
                    flag = False
                elif keys[pygame.K_7]:
                    value = myfont.render('7', True, inserted_elem_color)
                    win.blit(value, ((ind_x+1)*50 + 15, (ind_y+1)*50 ))
                    pygame.display.update()
                    flag = False
                elif keys[pygame.K_8]:
                    value = myfont.render('8', True, inserted_elem_color)
                    win.blit(value, ((ind_x+1)*50 + 15, (ind_y+1)*50 ))
                    pygame.display.update()
                    flag = False
                elif keys[pygame.K_9]:
                    value = myfont.render('9', True, inserted_elem_color)
                    win.blit(value, ((ind_x+1)*50 + 15, (ind_y+1)*50 ))
                    pygame.display.update()
                    flag = False

                

    

if __name__ == "__main__":
    main()