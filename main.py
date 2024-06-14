import pygame
import random

image_path = '/data/data/org.test.test_game/files/app/'

clock = pygame.time.Clock()
pygame.init()

screen = pygame.display.set_mode((1000, 563))  # flags=pygame.NOFRAME - убирает рамку
pygame.display.set_caption('test game')

icon = pygame.image.load(image_path + 'images/icon_elf.jpg')
pygame.display.set_icon(icon)

background = pygame.image.load(image_path + 'images/background/bg_1.png').convert_alpha()
background_mirror = pygame.image.load(image_path + 'images/background/bg_-1.png').convert_alpha()

# player = pygame.image.load('images/player_right/player_right_1.png')

walk_right = [
    pygame.image.load(image_path + 'images/player_right/player_right_1.png').convert_alpha(),
    pygame.image.load(image_path + 'images/player_right/player_right_2.png').convert_alpha(),
    pygame.image.load(image_path + 'images/player_right/player_right_3.png').convert_alpha(),
    pygame.image.load(image_path + 'images/player_right/player_right_4.png').convert_alpha(),]

walk_left = [
    pygame.image.load(image_path + 'images/player_left/player_left_1.png').convert_alpha(),
    pygame.image.load(image_path + 'images/player_left/player_left_2.png').convert_alpha(),
    pygame.image.load(image_path + 'images/player_left/player_left_3.png').convert_alpha(),
    pygame.image.load(image_path + 'images/player_left/player_left_4.png').convert_alpha(),]

ghost = pygame.image.load(image_path + 'images/ghost.png').convert_alpha()
ghost_list_in_game = []

player_anim_count = 0
background_anim_x = 0

player_speed = 7
player_x = 20
player_y = 480

is_jump = False
jump_count = 10

# background_sound = pygame.mixer.Sound(image_path + 'sounds/background_music.mp3')
# background_sound.play()

ghost_timer = pygame.USEREVENT + 1
pygame.time.set_timer(ghost_timer, random.randint(1500, 4000))

label_1 = pygame.font.Font(image_path + 'fonts/Jersey15-Regular.ttf', 100)
lose_label = label_1.render('Game Over', False, (193, 196, 199))

label_2 = pygame.font.Font('fonts/Jersey15-Regular.ttf', 65)
restart_label = label_2.render('Play again', False, (193, 196, 199))
restart_label_rect = restart_label.get_rect(topleft=(420, 300))

apples_max = 5
apple = pygame.image.load('images/apple.png').convert_alpha()
apples = []

gameplay = True

running = True
while running:
    keys = pygame.key.get_pressed()

    screen.blit(background, (background_anim_x, 0))
    screen.blit(background_mirror, (background_anim_x + 1000, 0))
    screen.blit(background, (background_anim_x + 2000, 0))

    if gameplay:
        player_rect = walk_right[0].get_rect(topleft=(player_x, player_y))

        if ghost_list_in_game:
            for (index, el) in enumerate(ghost_list_in_game):
                screen.blit(ghost, el)
                el.x -= 10

                if el.x < -10:
                    ghost_list_in_game.pop(index)

                if player_rect.colliderect(el):
                    gameplay = False

        if keys[pygame.K_a]:
            screen.blit(walk_left[player_anim_count], (player_x, player_y))
        else:
            screen.blit(walk_right[player_anim_count], (player_x, player_y))

        if keys[pygame.K_a] and player_x > 20:
            player_x -= player_speed
        elif keys[pygame.K_d] and player_x < 800:
            player_x += player_speed

        if not is_jump:
            if keys[pygame.K_w]:
                is_jump = True
        else:
            if jump_count >= -10:
                if jump_count > 0:
                    player_y -= (jump_count ** 2) / 2
                else:
                    player_y += (jump_count ** 2) / 2
                jump_count -= 2
            else:
                is_jump = False
                jump_count = 10

        if player_anim_count == 3:
            player_anim_count = 0
        else:
            player_anim_count += 1

        if background_anim_x == -2000:
            background_anim_x = 0
        else:
            background_anim_x -= 10

        if apples:
            for (index, el) in enumerate(apples):
                screen.blit(apple, (el.x, el.y))
                el.x += 15

                if el.x > 1020:
                    apples.pop(index)

                if ghost_list_in_game:
                    for (ind, ghost_el) in enumerate(ghost_list_in_game):
                        if el.colliderect(ghost_el):
                            ghost_list_in_game.pop(ind)
                            apples.pop(index)

    else:
        screen.fill((87, 88, 89))
        screen.blit(lose_label, (350, 150))
        screen.blit(restart_label, restart_label_rect)

        mouse = pygame.mouse.get_pos()
        if restart_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            gameplay = True
            player_x = 20
            ghost_list_in_game.clear()
            apples.clear()
            apples_max = 5

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == ghost_timer:
            ghost_list_in_game.append(ghost.get_rect(topleft=(1020, 480)))
        if gameplay and event.type == pygame.KEYUP and event.key == pygame.K_SPACE and apples_max > 0:
            apples.append(apple.get_rect(topleft=(player_x + 15, player_y + 5)))
            apples_max -= 1

    clock.tick(15)
