import psutil, socket, sys, pickle
from Projeto import cpu
from variaveis import *
import variaveis
#Início
pygame.init()

servidor = False
def funcionamento_servidor():
    if servidor == True:
        # Cria o socket
        socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Obtem o nome da máquina
        host = socket.gethostname()
        porta = 9999
        # Associa a porta
        socket_servidor.bind((host, porta))

        # Erro entre o Listen e o accept, só funciona quando abre o cliente antes
        # Escutando...
        socket_servidor.listen()

        (socket_cliente, addr) = socket_servidor.accept()

        lista = [larg_memoria, porcentagem_memoria, memoria_total, memoria_utilizado, memoria_disponivel,
                 larg_cpu, uso_cpu1, cpu_nome, cpu_arquitetura, cpu_palavra, cpu_max, cpu_core, cpu_frequencia_atual,
                 cpu_nucleos_processador, cpu_tempo_ativo,
                 larg_hd, info_hd, hd_total, hd_utilizado, hd_disponivel,
                 ethernet_mac, ethernet_ip, ethernet_mascara, ethernet_enviados, ethernet_recebidos]

        bytes = pickle.dumps(lista)
        socket_cliente.send(bytes)

        if variaveis.contador_alteracao_false == 50:
            socket_cliente.close()
            socket_servidor.close()
            variaveis.contador_alteracao_false = 0
        variaveis.contador_alteracao_false += 1
#############################################################
#Alteração Cliente-Servidor
alterar_modo = True
def alteracao():
    global Info
    global I
    global larg_memoria,porcentagem_memoria, memoria_total, memoria_utilizado, memoria_disponivel
    global larg_cpu, uso_cpu1, cpu_nome, cpu_arquitetura, cpu_palavra, cpu_max, cpu_core, cpu_frequencia_atual, cpu_nucleos_processador, cpu_tempo_ativo
    global larg_hd, info_hd, hd_total, hd_utilizado, hd_disponivel
    global ethernet_mac, ethernet_ip, ethernet_mascara, ethernet_enviados, ethernet_recebidos

    if alterar_modo == True:
        ##################################################
        #Memoria
        larg_memoria = larg * memoria.porcentagem() / 100
        porcentagem_memoria = str(memoria.porcentagem())
        memoria_total = str(memoria.total())
        memoria_utilizado = str(memoria.utilizado())
        memoria_disponivel = str(memoria.disponivel())
        ##################################################

        ##################################################
        #CPU
        larg_cpu = larg * cpu.porcentagem() / 100
        uso_cpu1 = str(round((larg_cpu /10), 1)) + "%"
        cpu_nome = str(cpu.name())
        cpu_arquitetura = str(cpu.arch())
        cpu_palavra = str(cpu.bits())
        cpu_max = str(cpu.freq_max())
        cpu_core = str(cpu.cores())
        cpu_frequencia_atual = str(cpu.freq_atual())
        cpu_nucleos_processador = str(cpu.physical_processors())
        cpu_tempo_ativo = str(cpu.tempo_ativo())

        ##################################################

        ##################################################
        #HD
        larg_hd = larg * hd.porcentagem() / 100
        info_hd = str(hd.porcentagem())
        hd_total = str(hd.total())
        hd_utilizado = str(hd.utilizado())
        hd_disponivel = str(hd.disponivel())

        ##################################################

        ##################################################
        #Ethernet
        ethernet_mac = str(ethernet.get_mac())
        ethernet_ip = str(ethernet.get_ip())
        ethernet_mascara = str(ethernet.get_mask())
        ethernet_enviados = str(ethernet.enviados())
        ethernet_recebidos = str(ethernet.recebidos())

        ##################################################

        ##################################################


    elif alterar_modo == False:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((socket.gethostname(), 9999))

            bytes = s.recv(1024)
            a = pickle.loads(bytes)
            if a:
                # Memória bits
                (larg_memoria) = a[0]
                (porcentagem_memoria) = a[1]
                (memoria_total) = a[2]
                (memoria_utilizado) = a[3]
                (memoria_disponivel) = a[4]

                # CPU bit/s
                (larg_cpu) = a[5]
                (uso_cpu1) = a[6]
                (cpu_nome) = a[7]
                (cpu_arquitetura) = a[8]
                (cpu_palavra) = a[9]
                (cpu_max) = a[10]
                (cpu_core) = a[11]
                (cpu_frequencia_atual) = a[12]
                (cpu_nucleos_processador) = a[13]
                (cpu_tempo_ativo) = a[14]

                # HD bits
                (larg_hd) = a[15]
                (info_hd) = a[16]
                (hd_total) = a[17]
                (hd_utilizado) = a[18]
                (hd_disponivel) = a[19]

                # Ethernet bits
                (ethernet_mac) = a[20]
                (ethernet_ip) = a[21]
                (ethernet_mascara) = a[22]
                (ethernet_enviados) = a[23]
                (ethernet_recebidos) = a[24]

        except Exception as erro:
            print(str(erro))
            # Memória bits
            (larg_memoria) = 0
            (porcentagem_memoria) = '0'
            (memoria_total) = '0'
            (memoria_utilizado) = '0'
            (memoria_disponivel) = '0'

            # CPU bit/s
            (larg_cpu) = 0
            (uso_cpu1) = '0'
            (cpu_nome) = '0'
            (cpu_arquitetura) = '0'
            (cpu_palavra) = '0'
            (cpu_max) = '0'
            (cpu_core) = '0'
            (cpu_frequencia_atual) = '0'
            (cpu_nucleos_processador) = '0'
            (cpu_tempo_ativo) = '0'

            # HD bits
            (larg_hd) = 0
            (info_hd) = '0'
            (hd_total) = '0'
            (hd_utilizado) = '0'
            (hd_disponivel) = '0'

            # Ethernet bits
            (ethernet_mac) = '0'
            (ethernet_ip) = '0'
            (ethernet_mascara) = '0'
            (ethernet_enviados) = '0'
            (ethernet_recebidos) = '0'

        if variaveis.contador_alteracao_false == 50:
            s.close()
            variaveis.contador_alteracao_false = 0
        variaveis.contador_alteracao_false +=1

    class Info:
        def __init__(self):
            self.__name = cpu_nome
            self.__arquitetura = cpu_arquitetura
            self.__palavra = cpu_palavra
            self.__max = cpu_max
            self.__cores = cpu_core

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
######################################################################################################

######################## Defs ###########################
##### Memória #####
def uso_memoria(x, y, z):
    tela_memoria.fill(white)
    font = pygame.font.Font(None, 32)
    larg = largura_tela - 2* 20
    pygame.draw.rect(tela_memoria, blue, (0, 10, larg, 80))
    larg = larg_memoria
    pygame.draw.rect(tela_memoria, red, (0, 10, larg, 80))
    info_memoria = porcentagem_memoria
    texto_barra = "Uso da Memória (Total: " + memoria_total + "): " + info_memoria + "%"
    text = font.render(texto_barra, True, black)
    tela.blit(text, (10, z))
    tela.blit(tela_memoria, (x, y))

def mostra_info_memoria():
    memoria_total1 = font.render("Memória Total: " + memoria_total, True, black)
    memoria_utilizada1 = font.render("Memória Utilizada: " + memoria_utilizado, True, black)
    memoria_disponivel1 = font.render("Memória Disponível: " + memoria_disponivel, True, black)

    tela.blit(memoria_total1, (10, 65))
    tela.blit(memoria_utilizada1, (10, 95))
    tela.blit(memoria_disponivel1, (10, 125))



##### HD #####
def uso_hd(x, y, z):
    tela_hd.fill(white)
    font = pygame.font.Font(None, 32)
    larg = largura_tela - 2 * 20
    pygame.draw.rect(tela_hd, blue, (0, 10, larg, 80))
    larg = larg_hd
    pygame.draw.rect(tela_hd, red, (0, 10, larg, 80))
    info = info_hd
    texto_barra = "Uso do Disco: (Total: " + hd_total + "): " + info + "%"
    text = font.render(texto_barra, True, black)
    tela.blit(text, (10, z))
    tela.blit(tela_hd, (x, y))

def mostra_info_hd():
    hd_total1 = font.render("Armazenamento Total: " + hd_total, True, black)
    hd_utilizado1 = font.render("Armazenamento Utilizado: " + hd_utilizado, True, black)
    hd_disponivel1 = font.render("Armazenamento Disponível: " + hd_disponivel, True, black)

    tela.blit(hd_total1, (10, 65))
    tela.blit(hd_utilizado1, (10, 95))
    tela.blit(hd_disponivel1, (10, 125))



##### CPU #####
def uso_cpu(x, y, z):
    tela_cpu2.fill(white)
    font = pygame.font.Font(None, 32)
    larg = largura_tela - 2 * 20
    pygame.draw.rect(tela_cpu2, blue, (0, 10, larg, 80))
    larg = larg_cpu
    pygame.draw.rect(tela_cpu2, red, (0, 10, larg, 80))
    texto_barra = "Uso da CPU: " + uso_cpu1
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



def mostra_info_cpu():
   nome_processador = font.render("Nome: " + I.name(), True, black)
   arquitetura_processador = font.render("Arquitetura: " + I.arquitetura(), True, black)
   palavra_processador = font.render("Palavra: " + I.palavra() + " bits", True, black)
   frequencia_processador = font.render("Frequência Atual: " + cpu_frequencia_atual, True, black)
   max_frequencia_processador = font.render("Frequência Máxima: " + I.max(), True, black)
   nucleo_processador = font.render("Núcleos (lógicos): " + I.cores() + " (" + cpu_nucleos_processador + ")", True, black)
   tempo_processador = font.render("Tempo Ativo: " + cpu_tempo_ativo, True, black)

   tela.blit(nome_processador, (10, 65))
   tela.blit(arquitetura_processador, (10, 95))
   tela.blit(palavra_processador, (10, 125))
   tela.blit(frequencia_processador, (10, 155))
   tela.blit(max_frequencia_processador, (10, 185))
   tela.blit(nucleo_processador, (10, 215))
   tela.blit(tempo_processador, (10, 245))




##### Ethernet #####
def mostra_info_ethernet():
    net_mac = font.render("Mac: " + ethernet_mac, True, black)
    net_ip = font.render("IPv4: " + ethernet_ip, True, black)
    net_mask = font.render("Máscara de Rede: " + ethernet_mascara, True, black)
    dados_enviados = font.render("Dados Enviados: " + ethernet_enviados, True, black)
    dados_recebidos = font.render("Dados Recebidos: " + ethernet_recebidos, True, black)
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
        z = None

    end_local = font.render("Endereço Local", True, black)
    ip_local = font.render("IP: " + a, True, black)
    porta_local = font.render("Porta: " + b, True, black)
    end_remoto = font.render("Endereço Remoto", True, black)
    ip_remoto = font.render("IP: " + c, True, black)
    porta_remoto = font.render("Porta: " + d, True, black)

    tela.blit(end_local, (10, 260))
    tela.blit(ip_local, (30, 290))
    tela.blit(porta_local, (30, 320))
    tela.blit(end_remoto, (10, 350))
    tela.blit(ip_remoto, (30, 380))
    tela.blit(porta_remoto, (30, 410))

    btn_cliente = font.render("CLIENTE", True, white)
    btn_original = font.render("ORIGINAL", True, white)
    btn_servidor = font.render("SERVIDOR", True, white)

    aviso_servidor = font.render("Após Clicar em 'Servidor', o programa irá travar até aparecer o cliente", True, black)

    tela.blit(btn_original, (71, 466))
    tela.blit(btn_cliente, (77, 506))
    tela.blit(btn_servidor, (68, 545))
    tela.blit(aviso_servidor, (200, 545))



