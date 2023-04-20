import pygame,random,sys
from pygame.locals import *
pygame.init()
RED=(255, 0, 0)
BLACK=(0, 0, 0)
#sys.setrecursionlimit(10000)
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)
FPS = 40
SPEED=5
SCORE=0
music = [pygame.mixer.Sound(r"C:\Users\User\Downloads\crash.wav"),
         pygame.mixer.Sound(r"C:\Users\User\Downloads\collect_coin.mp3")]
FramePerSec = pygame.time.Clock()
size= widht, height = 600, 500
screen_center= widht/2, height/2
screen= pygame.display.set_mode((size))
pygame.display.set_caption("Game")
running=True
background=pygame.image.load(r"C:\Users\User\Downloads\Street.png")
background=pygame.transform.scale(background, size)
img_rect = background.get_rect(center=screen_center)
class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(r"C:\Users\User\Downloads\Yellow lamba.png")
        self.image= pygame.transform.scale(self.image,(100,200))
        self.rect = self.image.get_rect()
        self.rect.center=(random.randint(40,widht-40),0) 
 
      def move(self):
        self.rect.move_ip(0,10)
        if (self.rect.bottom > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)
  
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(r"C:\Users\User\Downloads\White lamba.png")
        self.image= pygame.transform.scale(self.image,(100,200))
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
 
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0,5)
         
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < widht:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)


p1=Player()
e1=Enemy()
enemies = pygame.sprite.Group()
enemies.add(e1)
all_sprites = pygame.sprite.Group()
all_sprites.add(p1)
all_sprites.add(e1)

 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

while running:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
              SPEED += 2 
              SCORE+=1   
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    screen.blit(background, img_rect)
    scores = font_small.render(str(SCORE), True, BLACK)
    screen.blit(scores, (10,10))
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        entity.move()
    

    if pygame.sprite.spritecollideany(p1, enemies):
        music[0].play()      
        screen.fill(RED)
        screen.blit(game_over, (100, 200))
        pygame.display.update()
        for entity in all_sprites:
            entity.kill() 
        time.sleep(3)
        pygame.quit()
        sys.exit()        
          
    pygame.display.update()
    FramePerSec.tick(FPS)