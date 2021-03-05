# assets by <a href="https://www.vecteezy.com/free-vector/tic-tac-toe">Tic Tac Toe Vectors by Vecteezy</a>
# <a href='https://pngtree.com/so/game'>game png from pngtree.com</a>

import random
import pygame
import os


pygame.font.init()
pygame.display.set_caption('TIC TAC TOE')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
WIDTH, HEIGHT = 700, 700
HEIGHT_PLUS, WIDTH_PLUS = 900, 900
SIGN_WIDTH, SIGN_HEIGHT = 140, 140
BUTTON_WIDTH, BUTTON_HEIGHT = 400, 100
MAIN_BUTTON_WIDTH, MAIN_BUTTON_HEIGHT = 700, 200
WINNER_FONT = pygame.font.SysFont('dubai', 100)
XO_FONT = pygame.font.SysFont('dubai', 75)
BUTTON_FONT = pygame.font.SysFont('dubai', 50)
MAIN_BUTTON_FONT = pygame.font.SysFont('dubai', 90)

WIN = pygame.display.set_mode((WIDTH_PLUS, HEIGHT_PLUS))
BOARD = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'Board.jpg')), (WIDTH, HEIGHT))
X_SIGN = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'X_sign.jpg')), (SIGN_WIDTH, SIGN_HEIGHT))
O_SIGN = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'O_sign.jpg')), (SIGN_WIDTH, SIGN_HEIGHT))
BUTTON = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'button.png')), (BUTTON_WIDTH, BUTTON_HEIGHT))
MAIN_BUTTON = pygame.transform.scale(pygame.image.load(os.path.join(
    'Assets', 'button.png')), (MAIN_BUTTON_WIDTH, MAIN_BUTTON_HEIGHT))
main_rect = pygame.Rect(WIDTH_PLUS//2-WIDTH//2,
                        HEIGHT_PLUS//2-HEIGHT//2, WIDTH, HEIGHT)

state = ['', '', '', '', '', '', '', '', '']
line1 = [0, 1, 2]
line2 = [3, 4, 5]
line3 = [6, 7, 8]
line4 = [0, 3, 6]
line5 = [1, 4, 7]
line6 = [2, 5, 8]
line7 = [2, 4, 6]
line8 = [0, 4, 8]
lines = [line1, line2, line3, line4, line5, line6, line7, line8]
x_win_line = ['x', 'x', 'x']
o_win_line = ['o', 'o', 'o']

def draw_window():
    WIN.fill(WHITE)
    WIN.blit(BOARD, (main_rect.x, main_rect.y))
    pygame.display.update()

def draw_start_window():
    WIN.fill(WHITE)
    main_button_rect = pygame.Rect(WIDTH_PLUS//2-MAIN_BUTTON_WIDTH//2, HEIGHT_PLUS //
                                   3 - 2*MAIN_BUTTON_HEIGHT//3, MAIN_BUTTON_WIDTH, MAIN_BUTTON_HEIGHT)
    WIN.blit(MAIN_BUTTON, (main_button_rect.x, main_button_rect.y))
    main_draw_text = MAIN_BUTTON_FONT.render('TIC TAC TOE', 1, BLACK)
    WIN.blit(main_draw_text, (main_button_rect.x + main_button_rect.width//2 - main_draw_text.get_width() //
                              2, main_button_rect.y + main_button_rect.height//2 - main_draw_text.get_height()//2))
    button_rect1 = pygame.Rect(WIDTH_PLUS//2-BUTTON_WIDTH - 50,
                               HEIGHT_PLUS//2+BUTTON_HEIGHT//2, BUTTON_WIDTH, BUTTON_HEIGHT)
    WIN.blit(BUTTON, (button_rect1.x, button_rect1.y))
    draw_text1 = BUTTON_FONT.render('Player vs Player', 1, BLACK)
    WIN.blit(draw_text1, (button_rect1.x + button_rect1.width//2 - draw_text1.get_width() //
                          2, button_rect1.y + button_rect1.height//2 - draw_text1.get_height()//2))
    button_rect2 = pygame.Rect(
        WIDTH_PLUS//2 + 50, HEIGHT_PLUS//2+BUTTON_HEIGHT//2, BUTTON_WIDTH, BUTTON_HEIGHT)
    WIN.blit(BUTTON, (button_rect2.x, button_rect2.y))
    draw_text2 = BUTTON_FONT.render('Player vs AI', 1, BLACK)
    WIN.blit(draw_text2, (button_rect2.x + button_rect2.width//2 - draw_text2.get_width() //
                          2, button_rect2.y + button_rect2.height//2 - draw_text2.get_height()//2))
    pygame.display.update()

def draw_end_window():
    WIN.fill(WHITE)
    button_rect1 = pygame.Rect(WIDTH_PLUS//2-BUTTON_WIDTH - 50,
                               HEIGHT_PLUS//2+BUTTON_HEIGHT//2, BUTTON_WIDTH, BUTTON_HEIGHT)
    WIN.blit(BUTTON, (button_rect1.x, button_rect1.y))
    draw_text1 = BUTTON_FONT.render('Play again', 1, BLACK)
    WIN.blit(draw_text1, (button_rect1.x + button_rect1.width//2 - draw_text1.get_width() //
                          2, button_rect1.y + button_rect1.height//2 - draw_text1.get_height()//2))
    button_rect2 = pygame.Rect(
        WIDTH_PLUS//2 + 50, HEIGHT_PLUS//2+BUTTON_HEIGHT//2, BUTTON_WIDTH, BUTTON_HEIGHT)
    WIN.blit(BUTTON, (button_rect2.x, button_rect2.y))
    draw_text2 = BUTTON_FONT.render('MENU', 1, BLACK)
    WIN.blit(draw_text2, (button_rect2.x + button_rect2.width//2 - draw_text2.get_width() //
                          2, button_rect2.y + button_rect2.height//2 - draw_text2.get_height()//2))
    pygame.display.update()

def draw_bot_window():
    WIN.fill(WHITE)
    button_rect1 = pygame.Rect(WIDTH_PLUS//2-BUTTON_WIDTH - 50,
                               HEIGHT_PLUS//2+BUTTON_HEIGHT//2, BUTTON_WIDTH, BUTTON_HEIGHT)
    WIN.blit(BUTTON, (button_rect1.x, button_rect1.y))
    draw_text1 = BUTTON_FONT.render('EASY', 1, BLACK)
    WIN.blit(draw_text1, (button_rect1.x + button_rect1.width//2 - draw_text1.get_width() //
                          2, button_rect1.y + button_rect1.height//2 - draw_text1.get_height()//2))
    button_rect2 = pygame.Rect(
        WIDTH_PLUS//2 + 50, HEIGHT_PLUS//2+BUTTON_HEIGHT//2, BUTTON_WIDTH, BUTTON_HEIGHT)
    WIN.blit(BUTTON, (button_rect2.x, button_rect2.y))
    draw_text2 = BUTTON_FONT.render('MEDIUM', 1, BLACK)
    WIN.blit(draw_text2, (button_rect2.x + button_rect2.width//2 - draw_text2.get_width() //
                          2, button_rect2.y + button_rect2.height//2 - draw_text2.get_height()//2))
    button_rect3 = pygame.Rect(WIDTH_PLUS//2 - BUTTON_WIDTH//2,
                               HEIGHT_PLUS//2-2*BUTTON_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT)
    WIN.blit(BUTTON, (button_rect3.x, button_rect3.y))
    draw_text3 = BUTTON_FONT.render('HARD', 1, BLACK)
    WIN.blit(draw_text3, (button_rect3.x + button_rect3.width//2 - draw_text3.get_width() //
                          2, button_rect3.y + button_rect2.height//2 - draw_text3.get_height()//2))
    pygame.display.update()

def draw_sign(space, mark):
    if mark == 'x':
        sign = X_SIGN
    else:
        sign = O_SIGN
    if space == 6:
        WIN.blit(sign, (main_rect.x + 15, main_rect.y+30))
    elif space == 7:
        WIN.blit(sign, (main_rect.x + main_rect.width//3 + 30, main_rect.y+30))
    elif space == 8:
        WIN.blit(sign, (main_rect.x + 2*main_rect.width//3 + 45, main_rect.y+30))
    elif space == 3:
        WIN.blit(sign, (main_rect.x + 15, main_rect.width//3+(main_rect.y+30)))
    elif space == 4:
        WIN.blit(sign, (main_rect.x + main_rect.width//3 +
                        30, main_rect.width//3+(main_rect.y+30)))
    elif space == 5:
        WIN.blit(sign, (main_rect.x + 2*main_rect.width //
                        3 + 45, main_rect.width//3+(main_rect.y+30)))
    elif space == 0:
        WIN.blit(sign, (main_rect.x + 15, 2*main_rect.width//3+(main_rect.y+30)))
    elif space == 1:
        WIN.blit(sign, (main_rect.x + main_rect.width//3 +
                        30, 2*main_rect.width//3+(main_rect.y+30)))
    elif space == 2:
        WIN.blit(sign, (main_rect.x + 2*main_rect.width//3 +
                        45, 2*main_rect.width//3+(main_rect.y+30)))
    pygame.display.update()

def draw_winner(text):
    draw_rect = pygame.Rect(
        0, 0, WIDTH_PLUS, (HEIGHT_PLUS-main_rect.height)//2)
    pygame.draw.rect(WIN, WHITE, draw_rect)
    draw_text = WINNER_FONT.render(text, 1, BLACK)
    WIN.blit(draw_text, (WIDTH_PLUS/2 - draw_text.get_width() / 2, -40))
    pygame.display.update()
    pygame.time.delay(2000)

def draw_XO(mark):
    draw_rect = pygame.Rect(
        0, 0, WIDTH_PLUS, (HEIGHT_PLUS-main_rect.height)//2)
    pygame.draw.rect(WIN, WHITE, draw_rect)
    draw_text = XO_FONT.render('Move ['+mark.upper()+']', 1, BLACK)
    WIN.blit(draw_text, (WIDTH_PLUS/2 - draw_text.get_width() / 2, 0))
    pygame.display.update()

def check_win():
    for i in lines:
        line_check = [state[index] for index in i]
        if line_check == x_win_line:
            return 'X Won!!'
        elif line_check == o_win_line:
            return 'O Won!!'
    return ''

def move(mark):
    run = True
    while run:
        try:
            space = int(input('Ruch gracza ['+mark+'], Podaj gdzie [1-9]')) - 1
            if space <= 8 and space >= 0:
                run = False
                return space
            else:
                print('Ruch gracza ['+mark+'], Podaj liczbę z zakresu 1-9')
                run = True
        except:
            print('Ruch gracza ['+mark+'], Podaj liczbę z zakresu 1-9')

def move_by_mouse(mark):
    run = True
    while run:
        event = pygame.event.wait()
        if (event.type == pygame.MOUSEBUTTONDOWN and event.pos[0] > main_rect.x and event.pos[0] < (main_rect.x + main_rect.width) and event.pos[1] > main_rect.y and event.pos[1] < (main_rect.y + main_rect.height)) or event.type == pygame.QUIT:
            run = False
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        if event.pos[0] > main_rect.x and event.pos[0] < (main_rect.x + main_rect.width//3) and event.pos[1] > main_rect.y and event.pos[1] < (main_rect.y + main_rect.height/3):
            space = 6
        elif event.pos[0] > (main_rect.x + main_rect.width//3) and event.pos[0] < (main_rect.x + 2*main_rect.width//3) and event.pos[1] > main_rect.y and event.pos[1] < (main_rect.y + main_rect.height/3):
            space = 7
        elif event.pos[0] > (main_rect.x + 2*main_rect.width//3) and event.pos[0] < (main_rect.x + main_rect.width) and event.pos[1] > main_rect.y and event.pos[1] < (main_rect.y + main_rect.height/3):
            space = 8
        elif event.pos[0] > main_rect.x and event.pos[0] < (main_rect.x + main_rect.width//3) and event.pos[1] > (main_rect.y + main_rect.height/3) and event.pos[1] < (main_rect.y + 2*main_rect.height/3):
            space = 3
        elif event.pos[0] > (main_rect.x + main_rect.width//3) and event.pos[0] < (main_rect.x + 2*main_rect.width//3) and event.pos[1] > (main_rect.y + main_rect.height/3) and event.pos[1] < (main_rect.y + 2*main_rect.height/3):
            space = 4
        elif event.pos[0] > (main_rect.x + 2*main_rect.width//3) and event.pos[0] < (main_rect.x + main_rect.width) and event.pos[1] > (main_rect.y + main_rect.height/3) and event.pos[1] < (main_rect.y + 2*main_rect.height/3):
            space = 5
        elif event.pos[0] > main_rect.x and event.pos[0] < (main_rect.x + main_rect.width//3) and event.pos[1] > (main_rect.y + 2*main_rect.height/3) and event.pos[1] < (main_rect.y + 2*main_rect.height):
            space = 0
        elif event.pos[0] > (main_rect.x + main_rect.width//3) and event.pos[0] < (main_rect.x + 2*main_rect.width//3) and event.pos[1] > (main_rect.y + 2*main_rect.height/3) and event.pos[1] < (main_rect.y + 2*main_rect.height):
            space = 1
        elif event.pos[0] > (main_rect.x + 2*main_rect.width//3) and event.pos[0] < (main_rect.x + main_rect.width) and event.pos[1] > (main_rect.y + 2*main_rect.height/3) and event.pos[1] < (main_rect.y + 2*main_rect.height):
            space = 2
        return space
    elif event.type == pygame.QUIT:
        pygame.quit()
        quit()

def mouse_start_window():
    button_rect1 = pygame.Rect(WIDTH_PLUS//2-BUTTON_WIDTH - 50,
                               HEIGHT_PLUS//2+BUTTON_HEIGHT//2, BUTTON_WIDTH, BUTTON_HEIGHT)
    button_rect2 = pygame.Rect(
        WIDTH_PLUS//2 + 50, HEIGHT_PLUS//2+BUTTON_HEIGHT//2, BUTTON_WIDTH, BUTTON_HEIGHT)
    run3 = True
    while run3:
        event = pygame.event.wait()
        if ((event.type == pygame.MOUSEBUTTONDOWN and event.pos[0] > button_rect2.x and event.pos[0] < (button_rect2.x + button_rect2.width) and event.pos[1] > button_rect2.y and event.pos[1] < (button_rect2.y + button_rect2.height)) or
                (event.type == pygame.MOUSEBUTTONDOWN and event.pos[0] > button_rect1.x and event.pos[0] < (button_rect1.x + button_rect1.width) and event.pos[1] > button_rect1.y and event.pos[1] < (button_rect1.y + button_rect1.height)) or event.type == pygame.QUIT):
            run3 = False
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        if event.pos[0] > button_rect1.x and event.pos[0] < (button_rect1.x + button_rect1.width) and event.pos[1] > button_rect1.y and event.pos[1] < (button_rect1.y + button_rect1.height):
            mp = 1
        elif event.pos[0] > button_rect2.x and event.pos[0] < (button_rect2.x + button_rect2.width) and event.pos[1] > button_rect2.y and event.pos[1] < (button_rect2.y + button_rect2.height):
            mp = 0
        return mp
    elif event.type == pygame.QUIT:
        pygame.quit()
        quit()

def mouse_bot_window():
    button_rect1 = pygame.Rect(WIDTH_PLUS//2-BUTTON_WIDTH - 50,
                               HEIGHT_PLUS//2+BUTTON_HEIGHT//2, BUTTON_WIDTH, BUTTON_HEIGHT)
    button_rect2 = pygame.Rect(
        WIDTH_PLUS//2 + 50, HEIGHT_PLUS//2+BUTTON_HEIGHT//2, BUTTON_WIDTH, BUTTON_HEIGHT)
    button_rect3 = pygame.Rect(WIDTH_PLUS//2 - BUTTON_WIDTH//2,
                               HEIGHT_PLUS//2-2*BUTTON_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT)
    run3 = True
    while run3:
        event = pygame.event.wait()
        if ((event.type == pygame.MOUSEBUTTONDOWN and ((event.pos[0] > button_rect2.x and event.pos[0] < (button_rect2.x + button_rect2.width) and event.pos[1] > button_rect2.y and event.pos[1] < (button_rect2.y + button_rect2.height)) or
                                                       (event.pos[0] > button_rect1.x and event.pos[0] < (button_rect1.x + button_rect1.width) and event.pos[1] > button_rect1.y and event.pos[1] < (button_rect1.y + button_rect1.height)) or
                                                       event.pos[0] > button_rect3.x and event.pos[0] < (button_rect3.x + button_rect3.width) and event.pos[1] > button_rect3.y and event.pos[1] < (button_rect3.y + button_rect3.height) or event.type == pygame.QUIT))):
            run3 = False
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        if event.pos[0] > button_rect1.x and event.pos[0] < (button_rect1.x + button_rect1.width) and event.pos[1] > button_rect1.y and event.pos[1] < (button_rect1.y + button_rect1.height):
            lv = 'e'
        elif event.pos[0] > button_rect2.x and event.pos[0] < (button_rect2.x + button_rect2.width) and event.pos[1] > button_rect2.y and event.pos[1] < (button_rect2.y + button_rect2.height):
            lv = 'm'
        elif event.pos[0] > button_rect3.x and event.pos[0] < (button_rect3.x + button_rect3.width) and event.pos[1] > button_rect3.y and event.pos[1] < (button_rect3.y + button_rect3.height):
            lv = 'h'
        return lv
    elif event.type == pygame.QUIT:
        pygame.quit()
        quit()

def change(space, mark):
    state.pop(space)
    state.insert(space, mark)
    return state

def listToString(s):
    str1 = ""
    for ele in s:
        str1 += ele
    return str1

def bot(lv, mark):
    tmp = -2
    if mark == 'x':
        mark_in = 'oo'
    else:
        mark_in = 'xx'
    space = int(round(random.random()*8, 0))
    if lv == 'h' and len(listToString(state)) < 3:
        tmp = int(round(random.random()*5, 0))
        if tmp == 1:
            space = 0
        elif tmp == 2:
            space = 2
        elif tmp == 3:
            space = 6
        elif tmp == 4:
            space = 8
        elif tmp == 5:
            space = 4

    if (lv == 'm' or 'h'):
        for i in lines:
            line_check = [state[index] for index in i]
            if listToString(line_check) == mark + mark or listToString(line_check) == mark_in:
                tmp = int(round(random.random()*2, 0))
                space = i[tmp]
    return space

def main(mp, lv=''):
    tmp = 1
    i = 0
    ran = int(round(random.random()*1, 0))
    z = 1 - ran
    while i < 9:
        if i % 2 == 0:
            mark = 'x'
        else:
            mark = 'o'
        draw_XO(mark)
        if mp == 1 or (mp == 0 and z % 2 != 0):
            tmp = 0
            move1 = move_by_mouse(mark)
        elif mp == 0:
            tmp += 1
            move1 = bot(lv, mark)
        if state[move1] == '':
            draw_sign(move1, mark)
            change(move1, mark)
            i += 1
            z += 1
        if z == 10 - ran and check_win() == '':
            winner = 'TIE'
            draw_winner(winner)
        elif check_win() != '':
            i = 100
            winner = check_win()
            draw_winner(winner)

lv = ''
button = 0
run_main = True
while run_main:
    if button == 0:
        draw_start_window()
        lv = ''
        mp = mouse_start_window()
    if mp == 1:
        draw_window()
        main(mp)
    elif mp == 0 and lv == '':
        draw_bot_window()
        lv = mouse_bot_window()
        draw_window()
        main(mp, lv)
    elif mp == 0:
        draw_window()
        main(mp, lv)
    draw_end_window()
    button = mouse_start_window()
    state = ['', '', '', '', '', '', '', '', '']
