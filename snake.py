import random
import pygame

pygame.init()

blue = (0, 100, 255)
red = (255, 100, 0)
white = (255, 255, 255)
black = (0, 0, 0)
green = (34, 139, 24)

dis_width = 800
dis_height = 600

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption("snake game v1.0")

block_size = 25
snake_speed = 15

clock = pygame.time.Clock()

font_style = pygame.font.Font('freesansbold.ttf', 20)

def our_snake(blockSize, snake_list): # Creates the snake image from the dynamic snake_list
    for block in snake_list:
        pygame.draw.rect(dis, blue, [int(block[0]), int(block[1]), blockSize, blockSize])

def get_score(score): # Gets player score from length of snake
    printed_score = font_style.render("Score: " + str(score), True, black)
    dis.blit(printed_score, [int(dis_width/50), int(dis_height/50)])

def get_locations(food, snake):
    printed_food = font_style.render(str(food), True, black)
    dis.blit(printed_food, [10, 300])
    printed_snake = font_style.render("Snake locs: " + str(snake), True, black)
    dis.blit(printed_snake, [10, 200])

def message(msg, color): # Shows message for game_close
    mesg = font_style.render(msg, True, color)
    dis.fill(white)
    dis.blit(mesg, [int(dis_width/3), int(dis_height/3)])

def gameLoop():
    game_over = False
    game_close = False

    x1 = dis_width/2
    y1 = dis_height/2  
    x1_change = 0
    y1_change = 0

    snake_list = []
    snake_length = 1

    xgrid = []
    ygrid = []
    for row in range(1, int(dis_height / block_size) - 1):
        ygrid.append(row)
    for col in range(1, int(dis_width / block_size) - 1):
        xgrid.append(col)

    xfood = xgrid[random.randint(0, len(xgrid) - 1)] * block_size
    yfood = ygrid[random.randint(0, len(ygrid) - 1)] * block_size

    print(xgrid)
    print(ygrid)

    while not game_over:
        #while not playing
        while game_close == True:
            message("You suck. Press C to play again or Q to quit", green)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
                elif event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
        #buttons
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = block_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -block_size
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = block_size
            elif event.type == pygame.QUIT:
                game_over = True
        x1 += x1_change
        y1 += y1_change

        # close if hits sides
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        # create initial food
        dis.fill(white)
        pygame.draw.rect(dis, green, [xfood, yfood, block_size, block_size])

        #stores location of snake head, then adds it to the back of snake list
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        #Deletes added part if snake_length hasn't change
        if len(snake_list) > snake_length:
            del snake_list[0]

        # close if hits head
        for body in snake_list[:-1]:
            if body == snake_head:
                game_close = True
        
        our_snake(block_size, snake_list)
        get_score(snake_length - 1)
        pygame.display.update()

        if x1 == xfood and y1 == yfood:
            snake_length += 1
            xfood = xgrid[random.randint(0, len(xgrid) - 1)] * block_size
            yfood = ygrid[random.randint(0, len(ygrid) - 1)] * block_size
            
        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()