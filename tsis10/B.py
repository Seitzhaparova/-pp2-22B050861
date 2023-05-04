import sys
import psycopg2
import pygame
import random
import time

conn = psycopg2.connect(
    host ="localhost",
    database = "suppliers",
    user = "postgres",
    password = "postgre",
)

cursor = conn.cursor()

acc = input('\nDo you have account in Snake Game? \nPlease answer "yes" or "no": ')
flag = False

def sign_in(user, psw):
    cursor.execute("select * from snake_game") 
    conn.commit() 

    values = cursor.fetchall() 
    
    for value in values:
        if value[1] + value[-1] == user + psw:
            print("\nWelcome to the game !\nInfo: ")
            print(f'\n\tYour ID: {value[0]} \n\tScore: {value[2]} \n\tLevel: {value[3]}\n')
            play = input('Please write "play" to continue, if not press any button: ')
            if play == 'play':
                global flag
                flag = True 
                return
            else:
                sys.exit()

    un = input('Please try again.\n  Enter your username: ')
    pw = input('  Enter your password: ')
    sign_in(un, pw)

if acc == 'yes':
    username_yes = input('Enter your username: ')
    password_yes = input('Enter your password: ')    

    sign_in(username_yes, password_yes)

if acc == 'no':
    username_no = input('Think up your username: ')
    password_no = input('Think up your password: ')
    
    cursor.execute(f"insert into snake_game (username, user_score, user_level, password) values ('{username_no}', 0, 'Junior', '{password_no}')")
    conn.commit()
    
    print('\nYou are registered!\nNow you need to sign in')
    sign_in(username_no, password_no)



# -- pygame --
pygame.init()



WINDOW_WIDTH, WINDOW_HEIGHT = 500, 500
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# COLORS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
WHITE_2 = (100, 100, 100)
BLUE = (0, 0, 200)
GREEN = (0, 150, 0)
RED = (150, 0, 0)
YELLOW = (255, 255, 0)

BLOCK_SIZE = 20

# lvl() is converter 0 1 3 --> Junior Middle Senior
def lvl(n):
  if n == 0: return "Junior"
  elif n == 1: return "Middle"
  else: return "Senior"

# Greed 
def draw_grid():
  for i in range(0, WINDOW_WIDTH, BLOCK_SIZE):
    for j in range(0, WINDOW_HEIGHT, BLOCK_SIZE):
      pygame.draw.rect(screen, WHITE_2, (i, j, BLOCK_SIZE, BLOCK_SIZE), 1)


# WALL
class Wall:
  def __init__(self):
    self.body = []
    self.load_wall()
  def load_wall(self, level=0):
    with open(f'level{level1}.txt', 'r') as f:
      wall_body = f.readlines()
    
    for i, line in enumerate(wall_body):
      for j, value in enumerate(line):
        if value == '#':
          self.body.append([j, i])
  

  def draw(self):
    for x, y in self.body:
      pygame.draw.rect(screen, RED, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
  
# FOOD
class Food:
  def __init__(self):
      self.generate_random_pos_0lvl()
  
  def my_round(self, value, base=BLOCK_SIZE):
    return base * round(value / base)

  # for 0 lvl it have to generate random numbers between 0, 480
  def generate_random_pos_0lvl(self):
    self.x = self.my_round(random.randint(0, WINDOW_WIDTH - BLOCK_SIZE))
    self.y = self.my_round(random.randint(0, WINDOW_HEIGHT - BLOCK_SIZE))

  # for 1 lvl it have to generate random numbers between 60, 440
  def generate_random_pos_1lvl(self):
    self.x = self.my_round(random.randint(60, WINDOW_WIDTH - 40 - BLOCK_SIZE))
    self.y = self.my_round(random.randint(60, WINDOW_HEIGHT - 40 - BLOCK_SIZE))

  # for 2 lvl it have to generate random numbers between 100, 380
  def generate_random_pos_2lvl(self):
    self.x = self.my_round(random.randint(100, WINDOW_WIDTH - 100- BLOCK_SIZE))
    self.y = self.my_round(random.randint(100, WINDOW_HEIGHT - 100 - BLOCK_SIZE))

  def draw(self):
    self.color = BLUE
    pygame.draw.rect(screen, self.color, (self.x, self.y, BLOCK_SIZE, BLOCK_SIZE))


# SuperFood is the same Food class, diff between them is COLOR = YELLOW
class SuperFood:
  def __init__(self):
      self.generate_random_pos_0lvl()
  
  def my_round(self, value, base=BLOCK_SIZE):
    return base * round(value / base)
  
  def generate_random_pos_0lvl(self):
    self.x = self.my_round(random.randint(0, WINDOW_WIDTH - BLOCK_SIZE))
    self.y = self.my_round(random.randint(0, WINDOW_HEIGHT - BLOCK_SIZE))

  def generate_random_pos_1lvl(self):
    self.x = self.my_round(random.randint(60, WINDOW_WIDTH - 40 - BLOCK_SIZE))
    self.y = self.my_round(random.randint(60, WINDOW_HEIGHT - 40 - BLOCK_SIZE))

  def generate_random_pos_2lvl(self):
    self.x = self.my_round(random.randint(100, WINDOW_WIDTH - 100- BLOCK_SIZE))
    self.y = self.my_round(random.randint(100, WINDOW_HEIGHT - 100 - BLOCK_SIZE))

  def draw(self):
    self.color = YELLOW
    pygame.draw.rect(screen, self.color, (self.x, self.y, BLOCK_SIZE, BLOCK_SIZE))


# SNAKE 
class Snake:
  def __init__(self):
      self.body = [[10, 10], [11, 10]]
      self.dx = 1
      self.dy = 0
      
  def draw(self):
    for i, (x, y) in enumerate(self.body):
      color = RED if i == 0 else GREEN
      pygame.draw.rect(screen, color, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
  
  def move(self):
    for i in range(len(self.body) - 1, 0, -1):
      self.body[i][0] = self.body[i - 1][0]
      self.body[i][1] = self.body[i - 1][1]

    self.body[0][0] += self.dx
    self.body[0][1] += self.dy

score = 0
level = 0

def sql_query():
  sql = ""
  if acc == "yes":
    sql = f"update snake_game set user_score = {score} where username = '{username_yes}'; update snake_game set user_level = '{lvl(level)}' where username = '{username_yes}';"
  if acc == "no":
    sql = f"update snake_game set user_score = {score} where username = '{username_no}'; update snake_game set user_level = '{lvl(level)}' where username = '{username_no}';"
  cursor.execute(sql)
  conn.commit()


def game_pause():
  sql_query()


def game_over():
  sql_query()

  time.sleep(0.5)
  screen.fill(RED)
  font = pygame.font.SysFont("comicsansms", 40)
  text = font.render('Game Over', True, GREEN)
  screen.blit(text, (WINDOW_WIDTH // 2 - 100, WINDOW_HEIGHT // 2 - 200))

  font2 = pygame.font.SysFont("comicsansms", 30)
  text2 = font2.render(f'Score: {score} || Level: {lvl(level)}', True, GREEN)
  screen.blit(text2, (WINDOW_WIDTH // 2 - 150, WINDOW_HEIGHT // 2 - 150))
  pygame.display.update()
  time.sleep(2)
  pygame.quit()




# variables 
snake = Snake()
food = Food()
wall = Wall()
superfood = SuperFood()

last_key = ""

timer_sf = 0
timer_f = 0

clock = pygame.time.Clock()
FPS = 5

stop_button = 0
speed = 0 
while flag:
    for event in pygame.event.get():
      if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
        flag = False

  # turns    
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT and last_key != "left":
          last_key = "right"
          snake.dx = 1
          snake.dy = 0
        if event.key == pygame.K_LEFT and last_key != "right":
          last_key = "left"
          snake.dx = -1
          snake.dy = 0
        if event.key == pygame.K_UP and last_key != "down":
          last_key = "up"
          snake.dx = 0
          snake.dy = -1
        if event.key == pygame.K_DOWN and last_key != "up":
          last_key = "down"
          snake.dx = 0
          snake.dy = 1
        if event.key == pygame.K_SPACE:
            stop_button += 1
            game_pause()

    if stop_button % 2 == 0:
        snake.move() 

  # Foods which are disappearing after some time(timer)
    timer_sf += 1
    if timer_sf == 45:
      if level == 0: superfood.generate_random_pos_0lvl()
      if level == 1: superfood.generate_random_pos_1lvl()
      if level == 2: superfood.generate_random_pos_2lvl()
      timer_sf = 0

    timer_f += 1
    if timer_f == 60:
      if level == 0: food.generate_random_pos_0lvl()
      if level == 1: food.generate_random_pos_1lvl()
      if level == 2: food.generate_random_pos_2lvl()
      timer_f = 0

    # these lines check boundaries
    if snake.body[0][0] * BLOCK_SIZE > 500:
        game_over()

    if snake.body[0][1] * BLOCK_SIZE > 500:
        game_over()
    
    if snake.body[0][0] < 0:
        game_over()
    
    if snake.body[0][1] < 0:
        game_over()
  

    # Game Over
    for i in range(1, len(snake.body)):
      if snake.body[i][0] == snake.body[0][0] and snake.body[i][1] == snake.body[0][1]:
        game_over()
        flag = False


    screen.fill(BLACK)
    # draw 
    draw_grid()
    snake.draw()
    food.draw()
    wall.draw()
    
    # if snake eates food --> 1 point
    if snake.body[0][0] * BLOCK_SIZE == food.x and snake.body[0][1] * BLOCK_SIZE == food.y:
      snake.body.append([0, 0])

      if level == 0: food.generate_random_pos_0lvl()
      if level == 1: food.generate_random_pos_1lvl()
      if level == 2: food.generate_random_pos_2lvl()

      score += 1


    # if snake eates superfood
    if snake.body[0][0] * BLOCK_SIZE == superfood.x and snake.body[0][1] * BLOCK_SIZE == superfood.y:
      snake.body.append([0, 0])

      if level == 0: superfood.generate_random_pos_0lvl()
      if level == 1: superfood.generate_random_pos_1lvl()
      if level == 2: superfood.generate_random_pos_2lvl()

      score += 3
    

    if score >= 10 and score < 20:
      FPS = 10
      level = 1
      wall.load_wall(level)


    if score >= 20 and score < 40:
      FPS = 15
      level = 2
      wall.load_wall(level)

    if score < 70 and score >= 40:
      FPS = 20
    
    if score % 3 == 0:
      superfood.draw()

    
    font = pygame.font.SysFont("comicsansms", 20)
    text = font.render(f'Score: {score} || Level: {lvl(level)} || FPS: {FPS}', True, YELLOW)
    screen.blit(text, (20, 20))

    pygame.display.update()
    clock.tick(FPS)