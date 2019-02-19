import psutil
from Projeto import cpu
from variaveis import *

#Início
pygame.init()


######################## Defs ###########################
##### Memória #####
def uso_memoria(x, y, z):
    tela_memoria.fill(white)
    font = pygame.font.Font(None, 32)
    larg = largura_tela - 2* 20
    pygame.draw.rect(tela_memoria, blue, (0, 10, larg, 80))
    larg = larg* memoria.porcentagem() /100
    pygame.draw.rect(tela_memoria, red, (0, 10, larg, 80))
    info_memoria = str(memoria.porcentagem())
    texto_barra = "Uso da Memória (Total: " + str(memoria.total()) + "): " + info_memoria + "%"
    text = font.render(texto_barra, True, black)
    tela.blit(text, (10, z))
    tela.blit(tela_memoria, (x, y))

def mostra_info_memoria():
    memoria_total = font.render("Memória Total: " + str(memoria.total()), True, black)
    memoria_utilizada = font.render("Memória Utilizada: " + str(memoria.utilizado()), True, black)
    memoria_disponível = font.render("Memória Disponível: " + str(memoria.disponivel()), True, black)

    tela.blit(memoria_total, (10, 65))
    tela.blit(memoria_utilizada, (10, 95))
    tela.blit(memoria_disponível, (10, 125))



##### HD #####
def uso_hd(x, y, z):
    tela_hd.fill(white)
    font = pygame.font.Font(None, 32)
    larg = largura_tela - 2 * 20
    pygame.draw.rect(tela_hd, blue, (0, 10, larg, 80))
    larg = larg * hd.porcentagem() / 100
    pygame.draw.rect(tela_hd, red, (0, 10, larg, 80))
    info = str (hd.porcentagem())
    texto_barra = "Uso do Disco: (Total: " + str(hd.total()) + "): " + info + "%"
    text = font.render(texto_barra, True, black)
    tela.blit(text, (10, z))
    tela.blit(tela_hd, (x, y))

def mostra_info_hd():
    hd_total = font.render("Armazenamento Total: " + str(hd.total()), True, black)
    hd_utilizado = font.render("Armazenamento Utilizado: " + str(hd.utilizado()), True, black)
    hd_disponivel = font.render("Armazenamento Disponível: " + str(hd.disponivel()), True, black)

    tela.blit(hd_total, (10, 65))
    tela.blit(hd_utilizado, (10, 95))
    tela.blit(hd_disponivel, (10, 125))



##### CPU #####
def uso_cpu(x, y, z):
    tela_cpu2.fill(white)
    font = pygame.font.Font(None, 32)
    larg = largura_tela - 2 * 20
    pygame.draw.rect(tela_cpu2, blue, (0, 10, larg, 80))
    larg = larg * cpu.porcentagem() / 100
    pygame.draw.rect(tela_cpu2, red, (0, 10, larg, 80))
    texto_barra = "Uso da CPU: " + str(round((larg/10), 1)) + "%"
    text = font.render(texto_barra, True, black)
    tela.blit(text, (10, z))
    tela.blit(tela_cpu2, (x, y))

def usos_cpu_todos(l_cpu_percent):
    tela_cpu.fill(white)
    num_cpu = len(l_cpu_percent)
    x = y = 10
    desl = 10
    alt = tela_cpu.get_height() - 5*y
    larg = (tela_cpu.get_width()-45*y -(num_cpu+1) *desl ) /num_cpu
    d = x + desl
    for i in l_cpu_percent:
        pygame.draw.rect(tela_cpu, red, (d, y, larg, alt))
        pygame.draw.rect(tela_cpu, blue, (d, y, larg, (1-i/100)*alt))
        d = d + larg + desl
    tela.blit(tela_cpu, (largura_tela/6, altura_tela/1.4))

class Info:
   def __init__(self):
       self.__name = str(cpu.name())
       self.__arquitetura = str(cpu.arch())
       self.__palavra = str(cpu.bits())
       self.__max = str(cpu.freq_max())
       self.__cores = str(cpu.cores())

   def name(self):
       return self.__name

   def arquitetura(self):
       return self.__arquitetura

   def palavra(self):
       return self.__palavra

   def max(self):
       return self.__max

   def cores(self):
       return self.__cores

I = Info()

def mostra_info_cpu():
   nome_processador = font.render("Nome: " + I.name(), True, black)
   arquitetura_processador = font.render("Arquitetura: " + I.arquitetura(), True, black)
   palavra_processador = font.render("Palavra: " + I.palavra() + " bits", True, black)
   frequencia_processador = font.render("Frequência Atual: " + str(cpu.freq_atual()), True, black)
   max_frequencia_processador = font.render("Frequência Máxima: " + I.max(), True, black)
   nucleo_processador = font.render("Núcleos (lógicos): " + I.cores() + " (" + str(cpu.physical_processors()) + ")", True, black)
   tempo_processador = font.render("Tempo Ativo: " + str(cpu.tempo_ativo()), True, black)

   tela.blit(nome_processador, (10, 65))
   tela.blit(arquitetura_processador, (10, 95))
   tela.blit(palavra_processador, (10, 125))
   tela.blit(frequencia_processador, (10, 155))
   tela.blit(max_frequencia_processador, (10, 185))
   tela.blit(nucleo_processador, (10, 215))
   tela.blit(tempo_processador, (10, 245))




##### Ethernet #####
def mostra_info_ethernet():
    net_mac = font.render("Mac: " + str(ethernet.get_mac()), True, black)
    net_ip = font.render("IPv4: " + str(ethernet.get_ip()), True, black)
    net_mask = font.render("Máscara de Rede: " + str(ethernet.get_mask()), True, black)
    dados_enviados = font.render("Dados Enviados: " + str(ethernet.enviados()), True, black)
    dados_recebidos = font.render("Dados Recebidos: " + str(ethernet.recebidos()), True, black)
    pid_text = font.render("PID: ", True, black)

    tela.blit(net_mac, (10, 65))
    tela.blit(net_ip, (10, 95))
    tela.blit(net_mask, (10, 125))
    tela.blit(dados_enviados, (10, 155))
    tela.blit(dados_recebidos, (10, 185))
    tela.blit(pid_text, (10, 225))

def info_pid_ethernet(x):
    global info_pids
    info_pids = psutil.Process(x).connections()
    print(info_pids)





def info_pid_ethernet2():
    a = ""
    b = ''
    c = ''
    d = ''

    try:
        a = str(info_pids[0].laddr[0])
        b = str(info_pids[0].laddr[1])
        c = str(info_pids[0].raddr[0])
        d = str(info_pids[0].raddr[1])

        print("Endereço Local")
        print("IP:", info_pids[0].laddr[0])
        print("Porta:", info_pids[0].laddr[1])

        print()

        print("Endereço Remoto")
        print("IP:", info_pids[0].raddr[0])
        print("Porta:", info_pids[0].raddr[1])


        print(b)

    except:
        print("Error")

    end_local = font.render("Endereço Local", True, black)
    ip_local = font.render("IP: " + a, True, black)
    porta_local = font.render("Porta: " + b, True, black)
    end_remoto = font.render("Endereço Remoto", True, black)
    ip_remoto = font.render("IP: " + c, True, black)
    porta_remoto = font.render("PID: " + d, True, black)

    tela.blit(end_local, (10, 260))
    tela.blit(ip_local, (30, 290))
    tela.blit(porta_local, (30, 320))
    tela.blit(end_remoto, (10, 350))
    tela.blit(ip_remoto, (30, 380))
    tela.blit(porta_remoto, (30, 410))