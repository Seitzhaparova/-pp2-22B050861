import pygame
import time
import random
from pygame.locals import *
pygame.init()

score = 0
global level
level = 1
snake_speed = 15
widht = 720
height = 480
square_size = 25

black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)


pygame.display.set_caption('Snake')
game_window = pygame.display.set_mode((widht, height))
fps = pygame.time.Clock()

snake_position = [10, 150]

snake_body = [[100, 50],
              [90, 50],
              [80, 50],
              [70, 50]
              ]

# creating an apple class
class Apple:
    def __init__(self):
        self.x = square_size*(random.randrange(1, (widht // 10)) * 10)
        self.y = square_size*(random.randrange(1, (height) // 10) * 10)
        self.rect = pygame.Rect(self.x, self.y, square_size, square_size)
    def new(self):
        pygame.draw.rect(screen, 'orange', self.rect)
apple = Apple()


direction = 'RIGHT'
change_to = direction

# отображение функции Score
def show_score(choice, color, font, size) :
    score_font = pygame.font.SysFont("Verdana", 20)
    score_surface = score_font.render('Score : ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    game_window.blit(score_surface, score_rect)


# функция завершения игры
def game_over() :
    my_font = pygame.font.SysFont('times new roman', 50)
    # creating a text surface on which text
    # will be drawn
    game_over_surface = my_font.render(
        'Your Score is : ' + str(score), True, red)
    game_over_surface2 = my_font.render(
        'Your level is : ' + str(level), True, red)
    game_over_rect1 = game_over_surface.get_rect()
    game_over_rect2 = game_over_surface2.get_rect()
    game_over_rect1.midtop = (widht/2, height/3.5)
    game_over_rect2.midtop = (widht/2, height/4.7)
    game_window.blit(game_over_surface, game_over_rect1)
    game_window.blit(game_over_surface2, game_over_rect2)
    pygame.display.flip()
    time.sleep(2)
    quit()


#level showing function
def show_level(choice, color, font, size):
    f1=pygame.font.SysFont("Verdana", 20)
    cur_level=f1.render("Level: "+str(level), True, color)
    game_window.blit(cur_level, (620,0))

def level_up(score, snake_speed):
    if (score % 30 == 0 and score!=0):
        global level
        level += 1

# Main Function
while True :
    for event in pygame.event.get() : 
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_UP :
                change_to = 'UP'
            if event.key == pygame.K_DOWN :
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT :
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT :
                change_to = 'RIGHT'
    if change_to == 'UP' and direction != 'DOWN' :
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP' :
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT' :
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT' :
        direction = 'RIGHT'

    if direction == 'UP' :
        snake_position[1] -= 10
    if direction == 'DOWN' :
        snake_position[1] += 10
    if direction == 'LEFT' :
        snake_position[0] -= 10
    if direction == 'RIGHT' :
        snake_position[0] += 10

     # collision of snake's head and an apple
    collision = snake.head.colliderect(apple)
    if collision:
        a = random.choice([True, False])
        if a:
            snake.body.append(pygame.Rect(square.x, square.y, square_size, square_size))
            snake.body.append(pygame.Rect(square.x, square.y, square_size, square_size))
        if not a:
            snake.body.append(pygame.Rect(square.x, square.y, square_size, square_size))
        apple = Apple()

    game_window.fill(black)

    for pos in snake_body :
        pygame.draw.rect(game_window, green,
                         pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(game_window, white, pygame.Rect(
        apple_position[0], apple_position[1], 10, 10))

    # Game Over conditions
    if snake_position[0] < 0 or snake_position[0] > widht - 10 :
        game_over()
    if snake_position[1] < 0 or snake_position[1] >height - 10 :
        game_over()

    # Touching the snake body
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1] :
            game_over()

    # displaying score, level countinuously
    show_score(1, white, 'times new roman', 20)
    show_level(1, white, 'times new roman', 20)
    
    pygame.display.update()
    fps.tick(snake_speed)