import pygame
import os

# Inicializando o Pygame
pygame. init()

# Definindo o tamanho da janela padrão
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode ((WIDTH, HEIGHT), pygame.RESIZABLE) # Janela redimensionável
pygame.display.set_caption("Mover Imagem com Setas")

# Definindo a cor de fundo
BG_COLOR = (193, 0, 40) # cor de fundo (um tom escuro)


# Carregar a imagem
image_file = "GAME\\player.png" # Coloque o nome correto da sua imagem aqui
if os.path.exists (image_file):
    img = pygame.image.load (image_file).convert_alpha() # Carregar a imagem
    img_rect = img.get_rect(center=(WIDTH // 2, HEIGHT // 2)) # Centraliza a imagem
else:
    print ("Imagem não encontrada!")


# Velocidade de movimento
SPEED = 2 # pixels por movimento
JUMP_STRENGTH = 20 # Força do pulo (quanto maior, mais alto o pulo)
GRAVITY = 0.3 # Gravidade, fazendo o personagem cair
JUMPING = False # Indica se o personagem está no ar
VELOCITY_Y = 0 # Velocidade no eixo Y (inicialmente sem velocidade de pulo)

# Função para centralizar a imagem conforme o tamanho da tela 
def centralize_image():
    global img_rect, WIDTH, HEIGHT
    img_rect.center = (WIDTH // 2, HEIGHT // 2) # Centraliza a imagem no centro da tela

# Variáveis para controle de redimensionamento
last_width, last_height = WIDTH, HEIGHT

# Limite de movimento para que o personagem não saia da tela
def limit_movement():
    global img_rect, WIDTH, HEIGHT
    # Limita a posição da imagem para não sair da tela if img rect.left ‹ 0:
    img_rect.left < 0:
    img_rect.left < 0:
if img_ rect.right › WIDTH:
img rect.right = WIDTH