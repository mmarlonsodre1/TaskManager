import pygame, os
from Projeto import memoria
from Projeto import hd
from Projeto import cpu
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
legenda = pygame.display.set_caption("PROJETO TASK MANAGER")

#scroll mouse
scroll_y = 0
scroll = 0

tela_memoria = pygame.Surface((largura_tela, 100))
tela_cpu = pygame.Surface((largura_tela, altura_tela/3))
tela_cpu2 = pygame.Surface((largura_tela, 100))
tela_hd = pygame.Surface((largura_tela, 100))
tela_processos = pygame.Surface((largura_tela, 5000))
tela_processos2 = pygame.Surface((largura_tela, 1300))


fechou = False
relogio = pygame.time.Clock()
contador = 60
pid = None
pid_list = []
contador_pid = 60
contador_alteracao_false = 10
altura_pid = 10

tempo_thread = 20

lista_enviar = []

#Arquivos
diretorio = ''

font = pygame.font.Font(None, 32)
larg = largura_tela - 2 * 20

contata = 50