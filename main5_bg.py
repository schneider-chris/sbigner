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

backgorund_file = "background.png" # Caminho para sua imagem de fundo
if os.path.exists(background_file):
    backgorund_orig = pygame.image.load(background_file).convert()
    background = pygame.transform.scale(background_orig, (WIDTH, HEIGHT))
else:
    backgorund_orig = None
    background = None
    print("Imagem de fundo não encontrada!")
