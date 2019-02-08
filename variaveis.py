import pygame
from Projeto import memoria
from Projeto import hd
from Projeto import ethernet
pygame.init()

#Cores
black = (0, 0, 0)
white = (255, 255, 255)
red =(255, 0, 0)
blue = (0, 0, 255)
cinza_claro = (200, 200, 200)

#Variaveis
largura_tela = 1360
altura_tela = 768
resolucao = (largura_tela, altura_tela)
tela = pygame.display.set_mode(resolucao)
legenda = pygame.display.set_caption("TP03 de Marlon Sodré")
tela_memoria = pygame.Surface((largura_tela, 100))
tela_cpu = pygame.Surface((largura_tela, altura_tela/3))
tela_cpu2 = pygame.Surface((largura_tela, 100))
tela_hd = pygame.Surface((largura_tela, 100))
fechou = False
relogio = pygame.time.Clock()
contador = 60



font = pygame.font.Font(None, 32)
larg = largura_tela - 2 * 20



