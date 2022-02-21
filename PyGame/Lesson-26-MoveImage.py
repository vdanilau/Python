import  pygame

MAX_X = 1024 # разрешение экрана
MAX_Y = 800
IMG_SIZE_X = 100
IMG_SIZE_Y = 107

game_over = False
bg_color = (0, 0, 0)

pygame.init()

screen = pygame.display.set_mode((MAX_X, MAX_Y), pygame.FULLSCREEN)
pygame.display.set_caption("My First pygame Game") # Это ставит имя окошка

myimage = pygame.image.load("chastener.png").convert()
myimage = pygame.transform.scale(myimage, (IMG_SIZE_X, IMG_SIZE_Y)) # А это уменьшит саму картинку!

x = 500
y = 100

move_right = False
move_left = False
move_up = False
move_down = False

# -------- Main Game Loop ---------
while game_over == False:
    for event in pygame.event.get(): # считывает все ивенты, нажатие кнопок, движение мышки
        if event.type == pygame.KEYDOWN: # указываем именно нажатие кнопки как ивент
            if event.key == pygame.K_ESCAPE: # при нажатии кнопки ESC
                game_over = True
            if event.key == pygame.K_LEFT:
                move_left = True
            if event.key == pygame.K_RIGHT:
                move_right = True
            if event.key == pygame.K_UP:
                move_up = True
            if event.key == pygame.K_DOWN:
                move_down = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                move_left = False
            if event.key == pygame.K_RIGHT:
                move_right = False
            if event.key == pygame.K_UP:
                move_up = False
            if event.key == pygame.K_DOWN:
                move_down = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos  # Перехватывает и передает именно координаты курсора мыши

    if move_left == True:
        x -= 1
        if x < 0:
            x = 0 # т.е. не уйдет левее экрана в невидимую область
    if move_right:
        x += 1
        if x > MAX_X - IMG_SIZE_X:
            x = MAX_X - IMG_SIZE_X
    if move_up:
        y -= 1
        if y < 0:
            y = 0
    if move_down:
        y += 1
        if y > MAX_Y - IMG_SIZE_Y:
            y = MAX_Y - IMG_SIZE_Y



    screen.fill(bg_color) # Убираем с экрана предыдущие изображения (чтобы не было кучи рисунков при движении)
    screen.blit(myimage, (x, y)) # выкидывает картинку в координаты
    pygame.display.flip() # команда делает рендеринг и непосредственно выводит на экран