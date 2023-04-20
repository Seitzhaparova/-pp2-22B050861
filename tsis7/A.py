import pygame
import datetime
pygame.init()

size = screen_width, screen_height = 500, 500
screen = pygame.display.set_mode((size))
screen_center = screen_width/2, screen_height/2

image = pygame.image.load(r"C:\Users\User\Desktop\main-clock.png")
image = pygame.transform.scale(image, (500,500))
img_rect = image.get_rect(center=screen_center)

right_hand = pygame.image.load(r"C:\Users\User\Desktop\righthand.png")
right_hand = pygame.transform.scale(right_hand, (300, 100))
right_hand_rect = right_hand.get_rect(center=screen_center)

left_hand = pygame.image.load(r"C:\Users\User\Desktop\lefthand.png")
left_hand = pygame.transform.scale(left_hand, (400, 100))
left_hand_rect = left_hand.get_rect(center=screen_center)

l_angle = 6
r_angle = 6

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    screen.blit(image, img_rect)

    time = datetime.datetime.now()
    minutes, seconds = time.minute, time.second

    rot_l = pygame.transform.rotate(left_hand, (-6 * seconds) + 90)
    hand_l = rot_l.get_rect()
    hand_l.center = left_hand_rect.center

    rot_r = pygame.transform.rotate(right_hand, (-6 * minutes) + 90)
    hand_r = rot_r.get_rect()
    hand_r.center = right_hand_rect.center

    l_angle -= 0.66
    r_angle -= 0.0011

    screen.blit(rot_l, hand_l)
    screen.blit(rot_r, hand_r)
    pygame.display.flip()