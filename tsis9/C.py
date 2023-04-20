import pygame

# Making canvas
screen = pygame.display.set_mode((900, 700))

# Setting Title
pygame.display.set_caption('GFG Paint')
screen.fill((255, 255, 255))
draw_on = False
last_pos = (0, 0)

eraser_width = 50

# Radius of the Brush
radius = 5

# My code: setting up colors and their boxes
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
ORANGE = (255, 128, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (128, 0, 128)
#icons of figures
circleImage = pygame.image.load("Circle.png").convert_alpha()
circleImage = pygame.transform.scale(circleImage, (50, 50))
screen.blit(circleImage, (840, 10))

rectImage = pygame.image.load("Rectangle.png").convert_alpha()
rectImage = pygame.transform.scale(rectImage, (50, 50))
screen.blit(rectImage, (780, 10))
    
squareImage = pygame.image.load("Square.png").convert_alpha()
squareImage = pygame.transform.scale(squareImage, (50, 50))
screen.blit(squareImage, (720, 10))

etrienImage = pygame.image.load("Triangle.png").convert_alpha()
etrienImage = pygame.transform.scale(etrienImage, (50, 50))
screen.blit(etrienImage, (660, 10))

trienImage = pygame.image.load("Right_Triangle.png").convert_alpha()
trienImage = pygame.transform.scale(trienImage, (50, 50))
screen.blit(trienImage, (600, 10))

rhombusImage = pygame.image.load("Rhombus.png").convert_alpha()
rhombusImage = pygame.transform.scale(rhombusImage, (50, 50))
screen.blit(rhombusImage, (540, 10))

COLOR_BUTTONS = [
    {"color": RED, "rect": pygame.Rect(10, 10, 50, 50)},
    {"color": WHITE, "rect": pygame.Rect(70, 10, 50, 50)},
    {"color": YELLOW, "rect": pygame.Rect(130, 10, 50, 50)},
    {"color": GREEN, "rect": pygame.Rect(190, 10, 50, 50)},
    {"color": BLUE, "rect": pygame.Rect(250, 10, 50, 50)},
    {"color": PURPLE, "rect": pygame.Rect(310, 10, 50, 50)}
]

# eraser and its box
eraser = pygame.image.load(r'C:\Users\User\Downloads\eraser1.png')
eraser_img_resize = pygame.transform.scale(eraser, (eraser_width, eraser_width))


eraser_rect = pygame.Rect(360, 10, 50, 50)


# ends here
def drawRectangle(screen, mouse_pos, w, h, color):
    x = mouse_pos[0]
    y = mouse_pos[1]
    rect = pygame.Rect(x, y, w, h)
    pygame.draw.rect(screen, color, rect, 3)

# function for circle


def drawCircle(screen, mouse_pos, color):
    x = mouse_pos[0]
    y = mouse_pos[1]
    pygame.draw.circle(screen, color, (x, y), 100, 3)

# function for square


def drawSquare(screen, mouse_pos, w, h, color):

    x = mouse_pos[0]
    y = mouse_pos[1]
    rect = pygame.Rect(x, y, w, h)
    pygame.draw.rect(screen, color, rect, 3)

# function for right triangle


def drawRightTriangle(screen, color, mouse_pos):

    # Define the points

    x = mouse_pos[0]
    y = mouse_pos[1]
    triangle_size = 50

    # Calculate the triangle's vertices

    triangle_points = [
        (x, y - triangle_size),
        (x - triangle_size, y + triangle_size),
        (x + triangle_size, y + triangle_size),
    ]

    # Draw the triangle

    pygame.draw.polygon(screen, color, triangle_points)

# function for equiteral triangle


def drawEquilateralTriangle(screen, color, mouse_pos):

    # Define the points

    x = mouse_pos[0]
    y = mouse_pos[1]
    triangle_size = 50

    # Calculate the triangle's vertices

    triangle_points = [
        (x, y - triangle_size - 100),
        (x - triangle_size, y + triangle_size),
        (x + triangle_size, y + triangle_size),
    ]

    # Draw the triangle

    pygame.draw.polygon(screen, color, triangle_points)


def drawRhombus(screen, color, mouse_pos):

    # Define the points

    x = mouse_pos[0]
    y = mouse_pos[1]
    rhombus_height = 50
    rhombus_width = 50

    # Calculate the rhombus's vertices
    rhombus_points = [
        (x, y - rhombus_height),
        (x + rhombus_width, y),
        (x, y + rhombus_height),
        (x - rhombus_width, y),
    ]

    # Drawing

    pygame.draw.polygon(screen, color, rhombus_points)

def roundline(canvas, color, start, end, radius=1):
    Xaxis = end[0] - start[0]
    Yaxis = end[1] - start[1]
    dist = max(abs(Xaxis), abs(Yaxis))
    for i in range(dist):
        x = int(start[0] + float(i) / dist * Xaxis)
        y = int(start[1] + float(i) / dist * Yaxis)
        pygame.draw.circle(canvas, color, (x, y), radius)

# My Code
color = WHITE
initial_pos = None
final_pos = None
figure = None

# ends here
try:
    while True:
        e = pygame.event.wait()

        if e.type == pygame.QUIT:
            raise StopIteration

        # My code
        if e.type == pygame.MOUSEBUTTONDOWN: # check if mouse button was clicked on the boxes' position and change the color the new one
            if eraser_rect.collidepoint(e.pos):
                color = BLACK
            for button in COLOR_BUTTONS:
                if button["rect"].collidepoint(e.pos):
                    color = button['color']
        if e.type == pygame.KEYDOWN:
            radius = 0 # check if keys were pressed and save the figure form
            if e.key == pygame.K_r:
                initial_pos = pygame.mouse.get_pos()
                figure = 'rect'
            elif e.key == pygame.K_1:
                initial_pos = pygame.mouse.get_pos()
                figure = 'circle'
            elif e.key == pygame.K_s:
                initial_pos = pygame.mouse.get_pos()
                figure = 'sqr'
            elif e.key == pygame.K_t:
                initial_pos = pygame.mouse.get_pos()
                figure = 'r_t'
            elif e.key == pygame.K_e:
                initial_pos = pygame.mouse.get_pos()
                figure = 'e_t'
            elif e.key == pygame.K_w:
                initial_pos = pygame.mouse.get_pos()
                figure = 'rhombus'
        if e.type == pygame.KEYUP:
            initial_pos = None
            final_pos = None
            radius = 5
        # get position of mouse cursor as mouse left button is up
        if e.type == pygame.MOUSEBUTTONUP:
            final_pos = pygame.mouse.get_pos()
        # drawing figures
        if (draw == "rect" and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mouseY > 30):
            drawRectangle(surface, pygame.mouse.get_pos(), 200, 100, mode)

        if (draw == "square" and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mouseY > 30):
            drawSquare(surface, pygame.mouse.get_pos(), 100, 100, mode)

        if (draw == "circle" and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mouseY > 30):
            drawCircle(surface, pygame.mouse.get_pos(), mode)

        if (draw == "etrien" and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mouseY > 30):
            drawRightTriangle(surface, mode, pygame.mouse.get_pos())
        
        if (draw == "trien" and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mouseY > 30):
            drawEquilateralTriangle(surface, mode, pygame.mouse.get_pos())

        if (draw == "rhombus" and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mouseY > 30):
            drawRhombus(surface, mode, pygame.mouse.get_pos())
        mouseX, mouseY = pygame.mouse.get_pos()


        if e.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.circle(screen, color, e.pos, radius)
            draw_on = True
        # When mouse button released it will stop drawing
        if e.type == pygame.MOUSEBUTTONUP:
            draw_on = False
        # It will draw a continuous circle with the help of roundline function.
        if e.type == pygame.MOUSEMOTION:
            if draw_on:
                pygame.draw.circle(screen, color, e.pos, radius)
                roundline(screen, color, e.pos, last_pos, radius)
            last_pos = e.pos

        # My code
        for button in COLOR_BUTTONS:
            pygame.draw.rect(screen, button["color"], button["rect"])

        screen.blit(eraser_img_resize, (370, 10))

        # ends here
        pygame.display.flip()


except StopIteration:
    pass

# Quit
pygame.quit()