import pygame
pygame.init()

size = width, height = 600, 500
screen_center= width/2, height/2

screen = pygame.display.set_mode(size)
image = pygame.image.load(r"C:\Users\User\Downloads\spongebob_img.jpg")
image = pygame.transform.scale(image, (600,500))
img_rect = image.get_rect(center=screen_center)

music = [pygame.mixer.Sound(r"C:\Users\User\Downloads\sponge_music.mp3"),
         pygame.mixer.Sound(r"C:\Users\User\Downloads\sponge_music2.mp3")]

i = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        screen.blit(image, img_rect)
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            music[i].play()
        if key[pygame.K_UP]:
            music[i].stop()
        if key[pygame.K_RIGHT]:
            if i!=1:
                music[0].stop()
                music[1].play()
            else:  
                music[1].stop()
                music[0].play()
        if key[pygame.K_LEFT]:
            if i == 0:
                music[0].stop()
                music[1].play()
            else:
                music[1].stop()
                music[0].play()
               

    pygame.display.update() 