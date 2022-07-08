from pickle import encode_long
import pygame

WHITE = (255, 255 , 255)
RED = (255, 0 , 0)
BLACK = (0, 0, 0)
PURPLE = (70, 3, 137)
WINDOW_SIZE = 550
RECT_SIZE = 150
CIRCLE_SIZE = 50
BLANK_SIZE = 25
LINE_SIZE = 3
STATUS = ['O', 'X', None]
TURNS = ['O', 'X']

pygame.init()
window =pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption('틱택토')

matrix = [[[pygame.draw.rect(window, WHITE, (BLANK_SIZE * (col + 1) + RECT_SIZE * col, BLANK_SIZE * (row + 1) + RECT_SIZE * row, RECT_SIZE, RECT_SIZE)), -1]for col in range(3)] for row in range(3)]

run = True
end_game = False
Draw_game = False
turn_value = 0
current_turn = TURNS[turn_value % 2]

while run :
    pygame.time.delay(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    if event.type == pygame.MOUSEBUTTONUP:
        pos = pygame.mouse.get_pos()
        
        for row in range(3):
            for col in range(3):
                if matrix[row][col][0].collidepoint(pos):
                    if STATUS[matrix[row][col][1]] is None:
                        current_turn = TURNS[turn_value % 2]
                        if current_turn == 'O':
                            pygame.draw.circle(window, PURPLE, matrix[row][col][0].center, CIRCLE_SIZE)
                            matrix[row][col][1] = turn_value % 2
                        elif current_turn == 'X':
                            pygame.draw.line(window, BLACK, matrix[row][col][0].topleft,
                                                matrix[row][col][0].bottomright, LINE_SIZE)
                            pygame.draw.line(window, BLACK, matrix[row][col][0].topright,
                                                matrix[row][col][0].bottomleft, LINE_SIZE)
                            matrix[row][col][1] = turn_value % 2
                            
                        turn_value += 1
                        
                        if turn_value == 9 and check <= 2:
                            print("무승부입니다!")
                            Draw_game = True
                            
                        for _row in range(3):
                            check = 0
                            for _col in range(3):
                                if STATUS[matrix[_row][_col][1]] == current_turn:
                                    check += 1
                                if check == 3:
                                    end_game = True
                                    
                        for _col in range(3):
                            check = 0
                            for _row in range(3):
                                if STATUS[matrix[_row][_col][1]] == current_turn:
                                    check += 1
                                if check == 3:
                                    end_game = True
                        
                        check = 0
                        for _col, _row in zip(range(3), range(3)):
                            if STATUS[matrix[_row][_col][1]] == current_turn:
                                check += 1
                            if check == 3:
                                end_game = True
                                
                        check = 0
                        for _col, _row in zip(range(3), range(2, -1, -1)):
                            if STATUS[matrix[_row][_col][1]] == current_turn:
                                check += 1
                            if check == 3: 
                                end_game = True   
                                
                        
    pygame.display.update()
    if end_game:
        print(f'{current_turn} 승리 !!')
        pygame.time.delay(1500)
        run = False
    elif Draw_game:
        print("무승부입니다!")
        pygame.time.delay(1500)
        run = False
    
pygame.quit()