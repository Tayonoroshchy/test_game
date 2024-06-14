import pygame

pygame.init()

screen = pygame.display.set_mode((1000, 600))  # flags=pygame.NOFRAME - убирает рамку
pygame.display.set_caption('test game')

icon = pygame.image.load('images/icon_elf.jpg')
pygame.display.set_icon(icon)

square = pygame.Surface((50, 170))
square.fill((251, 160, 227))

my_font = pygame.font.SysFont('fonts/Jersey15-Regular.ttf', 50)
text_surface = my_font.render('Test Font', True, 'black')

player = pygame.image.load('images/icon_game.png')

running = True

while running:
    screen.fill((224, 176, 255))  # цвет фона rjb или названи цвета
    screen.blit(square, (0, 0))  # фигура и координаты

    screen.blit(text_surface, (300, 100))

    screen.blit(player, (300, 50))

    pygame.draw.circle(square, (193, 84, 193), (20, 40), 15)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        # elif event.type == pygame.KEYDOWN:  # смена цвета при нажатии на 'a'
        #     if event.key == pygame.K_a:
        #         screen.fill((251, 160, 227))
