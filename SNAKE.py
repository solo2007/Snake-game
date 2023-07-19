import pygame
import time
import random
import cv2

pygame.init()

screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Snake python")

background_img = pygame.image.load("start screen.png")

width = 200
height = 200

# Set up the camera capture using OpenCV
camera = cv2.VideoCapture(0)  # 0 represents the default camera
camera.set(3, width)
camera.set(4, height)


def game_starts():

    # Capture frame from the camera
    _, frame = camera.read()

    # Save the captured frame as an image file
    cv2.imwrite("camera_shot.jpg", frame)
    # main loop

    WIDTH, HEIGHT = 1150, 750
    FPS = pygame.time.Clock()
    speed = 9

    BACKGROUND = pygame.image.load("background.png")
    BACKGROUND = pygame.transform.scale(BACKGROUND,(WIDTH, HEIGHT))

    FRUIT_PHOTO = pygame.image.load("apple.png")
    FRUIT_PHOTO = pygame.transform.scale(FRUIT_PHOTO,(50,50))

    DISPLAY = pygame.display.set_mode((1150, 750))

    snake_head = pygame.image.load("camera_shot.jpg")
    snake_head = pygame.transform.scale(snake_head,(50,50))

    body_color = pygame.Color(0,10,155)

    # COLOURS

    BLACK = pygame.Color(0, 0, 0)
    WHITE = pygame.Color(255, 255, 255)
    RED = pygame.Color(255, 0, 0)
    GREEN = pygame.Color(0, 255, 0)
    BLUE = pygame.Color(0, 0, 255)

    snake_size = 48
    snake_body = [[240, 240], [220, 240], [200, 240], [180, 240]]
    snake_pos = [250, 250]

    fruit_pos = [random.randrange(1, (WIDTH // 50))*50, random.randrange(HEIGHT//50)*50]
    fruit_spawn = True

    direction = "RIGHT"
    change_to = direction
    score = 0

    def show_score(choice, color, font, size):
        score_font = pygame.font.SysFont(font, size)
        score_surface = score_font.render("Score : " + str(score),True, color)
        score_rect = score_surface.get_rect()
        DISPLAY.blit(score_surface, score_rect)

    def game_over():

        game_over_font = pygame.font.SysFont("MS Comic Sans", 50)
        game_over_surface = game_over_font.render("Your total score is : " + str(score), True, RED)
        game_over_rect = game_over_surface.get_rect()
        game_over_rect.midtop = WIDTH / 2, HEIGHT / 4

        DISPLAY.blit(game_over_surface, game_over_rect)
        pygame.display.flip()

        time.sleep(3)
        quit()

    while True:

        
        # movement
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    if direction == "DOWN":
                        direction = "DOWN"
                    else:
                        direction = "UP"
                
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    if direction == "UP":
                        direction = "UP"
                    else:
                        direction = "DOWN"
                
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    if direction == "LEFT":
                        direction = "LEFT"
                    else:
                        direction = "RIGHT"
                
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    if direction == "RIGHT":
                        direction = "RIGHT"
                    else:
                        direction = "LEFT"

                
                
                
                

        if direction == "UP":
            snake_pos[1] -= 50
        if direction == "DOWN":
            snake_pos[1] += 50
        if direction == "LEFT":
            snake_pos[0] -= 50
        if direction == "RIGHT":
            snake_pos[0] += 50

        for pos in snake_body[1::]:
            pygame.draw.rect(DISPLAY, body_color, pygame.Rect(pos[0], pos[1], snake_size, snake_size))
            DISPLAY.blit(snake_head,(snake_body[0][0], snake_body[0][1]))
                    
        if snake_pos[0] > WIDTH-50 or snake_pos[0] < 0:
            game_over()
        if snake_pos[1] > HEIGHT-50 or snake_pos[1] < 0:
            game_over()
        
        FPS.tick(speed)

        fruit_spawn = True

        snake_body.insert(0, list(snake_pos))
        if snake_pos[0] == fruit_pos[0] and snake_pos[1] == fruit_pos[1]:
            score += 10 
            fruit_spawn = False
        else:
            snake_body.pop()

        if fruit_spawn == False:
            fruit_pos = [random.randrange(1, (WIDTH // 50)) * 50, random.randrange(1, (HEIGHT // 50)) * 50]

        for block in snake_body[1:]:
            if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
                game_over()
        
        DISPLAY.blit(FRUIT_PHOTO, (fruit_pos[0], fruit_pos[1]))

        show_score(1, WHITE, "Arial", 20)
        
        pygame.display.update()
        DISPLAY.blit(BACKGROUND, (0,0))

        

#start button
start_btn_img = pygame.image.load("start button.png")
button_width = 100
button_height = 50
start_btn_img = pygame.transform.scale(start_btn_img, (button_width, button_height))
start_btn_rect = start_btn_img.get_rect()
start_btn_rect.center = (screen.get_width() // 2, screen.get_height() // 2)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if start_btn_rect.collidepoint(mouse_pos):
                game_starts()
    #screen image shown
    screen.blit(background_img, (0, 0))

    #start button shown
    screen.blit(start_btn_img, start_btn_rect)

    #ganaxleba ekranis
    pygame.display.flip()

pygame.quit()