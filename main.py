from asyncio.windows_events import NULL
from random import sample
import pygame, random, math


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

# DIFFICULTY
difficulty = 80      # (IMPORTANT!) ALWAYS KEEP THIS VARIABLE BETWEEN 17-80 (17 IS THE HARDEST, 80 IS THE EASIEST)


# randomize rows, columns and numbers (of valid base pattern)
def shuffle(s): 
    return sample(s,len(s)) 

# pattern for a baseline valid solution
def pattern(r,c): 
    return (base*(r%base)+r//base+c)%side

def updateGrid(win, ind_x, ind_y):
    win.fill(background_color)

    selected_number = display_grid[ind_y][ind_x]

    rect_vertical = pygame.Rect(((ind_x + 1) * 50), 50, 50, 450)
    rect_horizontal = pygame.Rect(50, ((ind_y + 1) * 50), 450, 50)

    # higlight the clicked cell and all cells with the same number
    if selected_number != 0:
        for x in range(0, len(display_grid)):
            for y in range(0, len(display_grid)):
                if selected_number == display_grid[y][x]:
                    pygame.draw.rect(win, (0, 255, 0), pygame.Rect(((x + 1) * 50), ((y + 1) * 50), 50, 50)) # all the numbers equal to the number selected
    pygame.draw.rect(win, (118, 118, 118), rect_vertical) # vertical line highlighting
    pygame.draw.rect(win, (118, 118, 118), rect_horizontal) # horizontal line highlighting
    pygame.draw.rect(win, (0, 255, 0), pygame.Rect(((ind_x + 1) * 50), ((ind_y + 1) * 50), 50, 50)) # clicked cell highlighting

    for i in range(0, 10):
        if i % 3 == 0:
            pygame.draw.line(win, (0, 0, 0), (50 + 50*i, 50), (50 + 50*i, 500), 4)
            pygame.draw.line(win, (0, 0, 0), (50, 50 + 50*i), (500, 50 + 50*i), 4)
        pygame.draw.line(win, (0, 0, 0), (50 + 50*i, 50), (50 + 50*i, 500), 2)
        pygame.draw.line(win, (0, 0, 0), (50, 50 + 50*i), (500, 50 + 50*i), 2)

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
    global difficulty
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
    while len(rand_coords) < difficulty:
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


def end_game(win):
    global error_count
    global display_grid
    print("Congratulations! You finished with " + str(error_count) + " errors.")
    error_count = 0
    display_grid = [ [0 for c in range(0, 9)] for r in range(0, 9) ]

    # Changing opacity of screen
    s = pygame.Surface((width, width))
    s.set_alpha(210)
    s.fill((background_color))
    win.blit(s, (0, 0))

    # Text in the center screen
    myfont = pygame.font.SysFont('Comic Sans MS', 35)
    text = myfont.render(("You win with " + str(error_count) + " errors!"), True, (0, 0, 0))
    text_rect = text.get_rect(center=(width/2, width/2))
    win.blit(text, text_rect)
    image = pygame.image.load(r'assets\refresh.png')
    image = pygame.transform.scale(image, (50, 50))
    pygame.draw.circle(win, (0, 0, 0), ((width / 2), (width / 2) + 55), 25)
    win.blit(image, ((width / 2) - 25, (width / 2) + 30))
    pygame.display.update()
    
    flag = True

    while flag:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
            # checks if mouse is clicked
            if e.type == pygame.MOUSEBUTTONUP:
                # check the coordinates
                mouse = pygame.mouse.get_pos()
                x = mouse[0]
                y = mouse[1]
                sqx = (x - (width / 2))**2
                sqy = (y - ((width / 2) + 55))**2
                if math.sqrt(sqx + sqy) < 25:
                    flag = False
                    main()

def solution_board():
    # SUDOKU SOLUTION BOARD
    rBase = range(base) 
    rows  = [ g*base + r for g in shuffle(rBase) for r in shuffle(rBase) ] 
    cols  = [ g*base + c for g in shuffle(rBase) for c in shuffle(rBase) ]
    nums  = shuffle(range(1,base*base+1))

    # produce board using randomized baseline pattern (SOLUTION)
    board = [ [nums[pattern(r,c)] for c in cols] for r in rows ]
    return board

def main():
    global error_count
    win = pygame.display.set_mode((width, width))
    pygame.display.set_caption("Sudoku Rústico")
    
    board = solution_board()

    for line in board: print(line)

    drawGrid(board, win)

    flag = True

    while flag:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                return
            if e.type == pygame.MOUSEBUTTONUP:
                # MOUSE POSITION
                x, y = pygame.mouse.get_pos()
                ind_x, ind_y = int(x / 50 - 1), int(y / 50 - 1)
                updateGrid(win, ind_x, ind_y)
                pygame.display.update()
                
            if e.type == pygame.KEYDOWN:
                print("A key has been pressed")
                if e.key == pygame.K_1:
                    if board[ind_y][ind_x] == 1:
                        display_grid[ind_y][ind_x] = 1
                        if display_grid == board:
                            updateGrid(win, ind_x, ind_y)
                            end_game(win)
                            flag = False
                    else: 
                        error_count += 1
                    updateGrid(win, ind_x, ind_y)
                if e.key == pygame.K_2:
                    if board[ind_y][ind_x] == 2:
                        display_grid[ind_y][ind_x] = 2
                        if display_grid == board:
                            updateGrid(win, ind_x, ind_y)
                            end_game(win)
                            flag = False
                    else: 
                        error_count += 1
                    updateGrid(win, ind_x, ind_y)
                if e.key == pygame.K_3:
                    if board[ind_y][ind_x] == 3:
                        display_grid[ind_y][ind_x] = 3
                        if display_grid == board:
                            updateGrid(win, ind_x, ind_y)
                            end_game(win)
                            flag = False
                    else: 
                        error_count += 1
                    updateGrid(win, ind_x, ind_y)
                if e.key == pygame.K_4:
                    if board[ind_y][ind_x] == 4:
                        display_grid[ind_y][ind_x] = 4
                        if display_grid == board:
                            updateGrid(win, ind_x, ind_y)
                            end_game(win)
                            flag = False
                    else: 
                        error_count += 1
                    updateGrid(win, ind_x, ind_y)
                if e.key == pygame.K_5:
                    if board[ind_y][ind_x] == 5:
                        display_grid[ind_y][ind_x] = 5
                        if display_grid == board:
                            updateGrid(win, ind_x, ind_y)
                            end_game(win)
                            flag = False
                    else: 
                        error_count += 1
                    updateGrid(win, ind_x, ind_y)
                if e.key == pygame.K_6:
                    if board[ind_y][ind_x] == 6:
                        display_grid[ind_y][ind_x] = 6
                        if display_grid == board:
                            updateGrid(win, ind_x, ind_y)
                            end_game(win)
                            flag = False
                    else: 
                        error_count += 1
                    updateGrid(win, ind_x, ind_y)
                if e.key == pygame.K_7:
                    if board[ind_y][ind_x] == 7:
                        display_grid[ind_y][ind_x] = 7
                        if display_grid == board:
                            updateGrid(win, ind_x, ind_y)
                            end_game(win)
                            flag = False
                    else: 
                        error_count += 1
                    updateGrid(win, ind_x, ind_y)
                if e.key == pygame.K_8:
                    if board[ind_y][ind_x] == 8:
                        display_grid[ind_y][ind_x] = 8
                        if display_grid == board:
                            updateGrid(win, ind_x, ind_y)
                            end_game(win)
                            flag = False
                    else: 
                        error_count += 1
                    updateGrid(win, ind_x, ind_y)
                if e.key == pygame.K_9:
                    if board[ind_y][ind_x] == 9:
                        display_grid[ind_y][ind_x] = 9
                        if display_grid == board:
                            updateGrid(win, ind_x, ind_y)
                            end_game(win)
                            flag = False
                    else: 
                        error_count += 1
                    updateGrid(win, ind_x, ind_y)
        
        

def init():
    pygame.init()
    main() 


if __name__ == "__main__":
    init()