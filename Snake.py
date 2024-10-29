import pygame
import random
import sys

pygame.init()
pygame.font.init()

Menu=True


black = (0, 0, 0)
red = (255, 0, 0)

sc = pygame.display.set_mode((600, 400))
sc.fill(black)

active = False
text = ''
done = False

width = 600
height = 400

dis = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake')

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 15

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

while Menu==True:
    font = pygame.font.Font(None, 32)
    input_box = pygame.Rect(10, 50, 140, 32)
    color_inactive = pygame.Color((200, 0, 0))
    color_active = pygame.Color((250, 0, 0))
    color = color_inactive

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Menu=False
            game_over = False
            game_close = False
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                sys.exit()
        pressed = pygame.mouse.get_pressed()
        pos = pygame.mouse.get_pos()
        if pos[0]>=230 and pos[0]<=370 and pos[1]>=300 and pos[1]<=350 and pressed[0] and len(text)>1:
            game_over = True
            game_close = False
            Menu = False
        elif pos[0]>=230 and pos[0]<=370 and pos[1]>=240 and pos[1]<=290 and pressed[0]:
            game_over = False
            game_close = False
            Menu = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_box.collidepoint(event.pos):
                active = not active
            else:
                active = False
            color = color_active if active else color_inactive
        if event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                    pygame.display.update()
                else:
                    text += event.unicode

        txt_surface = font.render(text, True, color)
        Width = max(200, txt_surface.get_width() + 10)
        input_box.w = Width
        sc.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        pygame.draw.rect(sc, color, input_box, 2)

        pygame.display.update()


    pygame.draw.rect(sc, (255, 0, 0), ((230, 300), (140, 50)))
    f1 = pygame.font.SysFont('serif', 48)
    text1 = f1.render("Start", False, (0, 0, 0))
    pygame.draw.rect(sc, (255, 0, 0), ((230, 240), (140, 50)))
    f2 = pygame.font.SysFont('serif', 48)
    text2 = f2.render("Exit", False, (0, 0, 0))
    sc.blit(text1, (250, 300))
    sc.blit(text2, (255, 240))

    pygame.display.update()


clock.tick(60)
pygame.display.update()

def Your_score(score):
    global text
    global dis
    value = score_font.render(text +' '+ 'Score:' + str(score), True, red)
    dis.blit(value, [0, 0])


def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, red, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [width / 10.5, height / 3])

def gameLoop():
    global game_over
    global game_close


    x1 = width / 2
    y1 = height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    while game_over==True:

        while game_close == True:
            pygame.mixer.music.pause()
            dis.fill(black)
            message("You loss!!, Press E to return,or press Q to exit ", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_close=False
                    game_over=False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = False
                        game_close = False
                    if event.key == pygame.K_e:
                        game_over = True
                        game_close = False
                        gameLoop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = False
                game_close=False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_d:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_w:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_s:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(black)
        pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()