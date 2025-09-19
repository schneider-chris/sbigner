import pygame 
import os

pygame.init() 

WIDTH, HEIGHT = 1020, 900
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE) # Janela redimensional
pygame.display.set_caption("Mover imagem com setas")

# Definindo a cor do fundo
BG_COLOR = (30, 30, 40) # cor do fundo (uma cor escura)

# Carregar a Imagem
image_file = "player.png" # Coloque o nome da sua imagem aqui
if os.path.exists(image_file):
    img = pygame.image.load(image_file).convert_alpha() # Carregar a imagem
    img_rect = img.get_rect(center=(WIDTH // 2, HEIGHT // 2)) # Centralizar a imagem
else:
    print("Imagem não encontrada!")

background_file = "background.png" # Caminho para sua imagem de fundo
if os.path.exists(background_file):
    backgorund_orig = pygame.image.load(background_file).convert()
    background = pygame.transform.scale(background_orig, (WIDTH, HEIGHT))
else:
    backgorund_orig = None
    background = None
    print("Imagem de fundo não encontrada!")

SPEED = 2 
JUMP_STRENGTH = 30
GRAVITY = 0.9 
JUMPING = False
VELOCITY_Y = 0

def centralize_image():
    global img_rect, WIDTH, HEIGHT
    img_rect.center = (WIDTH // 2, HEIGHT // 2)

last_width, last_height = WIDTH, HEIGHT

def limit_movement():
    global img_rect, WIDTH, HEIGHT
    if img_rect.left < 0:
        img_rect.left = 0
    if img_rect.right > WIDTH:
        img_rect.right = WIDTH
    if img_rect.top < 0:
        img_rect.top = 0
    if img_rect.bottom > HEIGHT:
        img_rect.bottom = HEIGHT

def jump():
    global JUMPING, VELOCITY_Y
    if not JUMPING:
        VELOCITY_Y = -JUMP_STRENGTH
        JUMPING = True

def update_jump():
    global JUMPING, VELOCITY_Y, img_rect
    if JUMPING:
        VELOCITY_Y += GRAVITY
        img_rect.y += VELOCITY_Y

        if img_rect.bottom >= HEIGHT: 
            img_rect.bottom = HEIGHT
            JUMPING = False
            VELOCITY_Y = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    current_width, current_height = screen.get_size()

    if current_width != last_width or current_height != last_height:
        WIDTH, HEIGHT = current_width, current_height
        centralize_image()
        if backgorund_orig:
            background = pygame.transform.scale(backgorund_orig, (WIDTH, HEIGHT)) 
        last_width, last_height = current_width, current_height

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        img_rect.x -= SPEED # Move para a esquerda
    if keys[pygame.K_RIGHT]:
        img_rect.x += SPEED # Move para a direita
    if keys[pygame.K_UP]:
        img_rect.y -= SPEED # Move para cima
    if keys[pygame.K_DOWN]:
        img_rect.y += SPEED # Move para baixo

        if keys[pygame.K_SPACE]:
            jump()

    limit_movement()

    update_jump()

    if background:
        screen.blit(background, (0, 0))
    else:
        screen.fill(BG_COLOR)

    if img:
        screen.blit(img, img_rect.topleft)

    pygame.display.flip()

pygame.quit()