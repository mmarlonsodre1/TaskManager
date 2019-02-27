import pygame
import psutil
import variaveis
from variaveis import *
from Projeto import cpu
from Projeto import memoria
from Projeto import hd
from Projeto import ethernet
from Projeto import usos

def botoes(x, y, w, z):
    global font

    quadrado = pygame.draw.rect(tela, cinza_claro, (x, y, w, z))

    btn_resumo_text = "Resumo"
    btn_etheret_text = "Ethernet"
    btn_memoria_text = "Memória"
    btn_cpu_text = "CPU"
    btn_hd_text = "HD"

    render_resumo = font.render(btn_resumo_text, True, black)
    render_ethernet = font.render(btn_etheret_text, True, black)
    render_memoria = font.render(btn_memoria_text, True, black)
    render_cpu = font.render(btn_cpu_text, True, black)
    render_hd = font.render(btn_hd_text, True, black)

    tela.blit(render_resumo, (12, 10))
    tela.blit(render_ethernet, (120, 10))
    tela.blit(render_memoria, (230, 10))
    tela.blit(render_cpu, (340, 10))
    tela.blit(render_hd, (407, 10))

def btn_resumo():
    net_mac = font.render("Mac: " + usos.ethernet_mac, True, black)
    net_ip = font.render("IPv4: " + usos.ethernet_ip, True, black)

    tela.blit(net_mac, (10, 65))
    tela.blit(net_ip, (10, 95))

    usos.uso_memoria(20, 180, 150)
    usos.uso_hd(20, 330, 300)
    usos.usos_cpu_todos(cpu.porcentagem_todos())
    usos.uso_cpu(20, 480, 450)

def btn_cpu():
    usos.mostra_info_cpu()
    usos.uso_cpu(20, 320, 290)
    usos.usos_cpu_todos(cpu.porcentagem_todos())

def btn_memoria():
    usos.mostra_info_memoria()
    usos.uso_memoria(20, 230, 200)

def btn_hd():
    usos.mostra_info_hd()
    usos.uso_hd(20, 230, 200)

def btn_ethernet():
    usos.mostra_info_ethernet()
    usos.info_pid_ethernet2()
    pygame.draw.rect(tela, cinza_claro, (0, 210, 1360, 5))

def menu_animation(x):
    if x == 0:
        botoes(5, 5, 100, 36)
        btn_resumo()

    elif x == 1:
        botoes(115, 5, 104, 36)
        btn_ethernet()

    elif x == 2:
        botoes(225, 5, 104, 36)
        btn_memoria()

    elif x == 3:
        botoes(335, 5, 60, 36)
        btn_cpu()

    elif x == 4:
        botoes(400, 5, 45, 36)
        btn_hd()

def main():
    global tela
    global fechou
    menu_list = 0
    tela.fill((255, 255, 255))
    pygame.init()

    usos.alterar_modo = False
    usos.alteracao()

    ####################################################
    # Botões do Menu
    btn_resumo = pygame.Rect(5, 5, 100, 36)
    btn_ethernet = pygame.Rect(115, 5, 104, 36)
    btn_memoria = pygame.Rect(225, 5, 104, 36)
    btn_cpu = pygame.Rect(335, 5, 60, 36)
    btn_hd = pygame.Rect(400, 5, 45, 36)
    #####################################################

    #####################################################
    #variaveis e atributos para o text box para ethernet
    input_box_pid = pygame.Rect(55, 220, 140, 32)
    button_original = pygame.Rect(55, 460, 140, 32)
    button_cliente = pygame.Rect(55, 500, 140, 32)
    button_servidor = pygame.Rect(55, 540, 140, 32)
    color_active = pygame.Color('dodgerblue2')
    color = black
    active = False

    text = ''
    ######################################################

    while not fechou:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Botoões do Menu
                if btn_resumo.collidepoint(event.pos):
                    menu_list = 0
                if btn_ethernet.collidepoint(event.pos):
                    menu_list = 1
                if btn_memoria.collidepoint(event.pos):
                    menu_list = 2
                if btn_cpu.collidepoint(event.pos):
                    menu_list = 3
                if btn_hd.collidepoint(event.pos):
                    menu_list = 4
                ###############################################

                ###############################################
                # Utilizar o teclado ao clicar no text box
                if input_box_pid.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = not active
                else:
                    active = False
                # Mudar a cor do text box
                color = color_active if active else black
                ############################################

                ############################################
                # Botão do cliente
                if button_cliente.collidepoint(event.pos):
                    if usos.alterar_modo == False:
                        usos.alterar_modo = True
                    else:
                        usos.alterar_modo = False
                    print(usos.alterar_modo)
                #############################################

                ##############################################
                # botão do original
                if button_original.collidepoint(event.pos):
                    if usos.alterar_modo == False:
                        usos.alterar_modo = True
                    else:
                        usos.alterar_modo = False
                    print(usos.alterar_modo)
                ###############################################

                ###############################################
                #Botão para conexão do servidor
                if button_servidor.collidepoint(event.pos):
                    if usos.servidor == False:
                        usos.servidor = True
                        print(usos.servidor)
                    else:
                        print(usos.servidor)
                        usos.servidor = False

            if event.type == pygame.KEYDOWN:
                #######################################
                #Passar as telas
                if event.key == pygame.K_RIGHT:
                    menu_list +=1
                    tela.fill(white)
                    if menu_list >= 5:
                        menu_list = 4
                        tela.fill(white)

                elif event.key == pygame.K_LEFT:
                    menu_list -= 1
                    tela.fill(white)
                    if menu_list <= 0:
                        menu_list = 0
                        tela.fill(white)

                elif event.key == pygame.K_SPACE:
                    menu_list = 0
                #############################################
                #############################################
                #Text box ethernet
                if menu_list == 1:
                    if active:
                        if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                        #Clique do enter
                            #trasnformar texto em numero já com regex
                            pid = text
                            if pid.isdigit():
                                pid = int(text)
                            else:
                                print("Digite Números")

                            #Resetar texto
                            text = ''

                            #Verificar se o pid é válido
                            if pid in variaveis.pid_list:
                                usos.info_pid_ethernet(pid)
                            else:
                                print("PID INVÁLIDO")

                        elif event.key == pygame.K_BACKSPACE:
                            text = text[:-1]
                        else:
                            text += event.unicode
                ###############################################

            if event.type == pygame.QUIT:
                fechou = True

        tela.fill(white)

        ############################################################
        #Linhas do menu
        pygame.draw.rect(tela, cinza_claro, (0, 5, 1360, 2))
        pygame.draw.rect(tela, cinza_claro, (0, 40, 1360, 2))
        ############################################################

        ##############################################################
        #Cor do botoes ethernet
        if usos.alterar_modo == False:
            color2 = black
            color1 = color_active
        else:
            color2 = color_active
            color1 = black

        if usos.servidor == True:
            color3 = color_active
        else:
            color3 = black

        ##############################################################

        ##############################################################
        # Text Box Ethernet
        if menu_list == 1:
            txt_surface = font.render(text, True, color)
            # Resize the box if the text is too long.
            width = max(200, txt_surface.get_width() + 10)
            input_box_pid.w = width
            # Blit the text.
            tela.blit(txt_surface, (input_box_pid.x + 5, input_box_pid.y + 5))
            # Blit the input_box rect.
            pygame.draw.rect(tela, color, input_box_pid, 2)

            # Print botoes cliente_servidor
            pygame.draw.rect(tela, color1, button_cliente)
            pygame.draw.rect(tela, color2, button_original)
            pygame.draw.rect(tela, color3, button_servidor)
        ###############################################################

        ###############################################################
        #Montar lista com PIDs
        if variaveis.contador_pid == 60:
            variaveis.pid_list = psutil.pids()
            print(variaveis.pid_list)
            variaveis.contador_pid = 0
        ###############################################################

        usos.alteracao()
        usos.funcionamento_servidor()
        variaveis.contador_pid += 1
        menu_animation(menu_list)
        pygame.display.update()
        relogio.tick(80)

    pygame.display.quit()
    pygame.quit()

if __name__ == '__main__':
    main()
