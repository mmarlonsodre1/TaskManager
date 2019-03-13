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
    btn_processos_text = "Processos"
    btn_arquivos_text = "Arquivos"

    render_resumo = font.render(btn_resumo_text, True, black)
    render_ethernet = font.render(btn_etheret_text, True, black)
    render_memoria = font.render(btn_memoria_text, True, black)
    render_cpu = font.render(btn_cpu_text, True, black)
    render_hd = font.render(btn_hd_text, True, black)
    render_processos = font.render(btn_processos_text, True, black)
    render_arquivos = font.render(btn_arquivos_text, True, black)

    tela.blit(render_resumo, (12, 10))
    tela.blit(render_ethernet, (120, 10))
    tela.blit(render_memoria, (230, 10))
    tela.blit(render_cpu, (340, 10))
    tela.blit(render_hd, (407, 10))
    tela.blit(render_processos, (455, 10))
    tela.blit(render_arquivos, (580, 10))

def btn_resumo():
    net_mac = font.render("Mac: " + usos.ethernet_mac, True, black)
    net_ip = font.render("IPv4: " + usos.ethernet_ip, True, black)

    tela.blit(net_mac, (10, 65))
    tela.blit(net_ip, (10, 95))

    usos.uso_memoria(20, 180, 150)
    usos.uso_hd(20, 330, 300)
    usos.usos_cpu_todos()
    usos.uso_cpu(20, 480, 450)

def btn_cpu():
    usos.mostra_info_cpu()
    usos.uso_cpu(20, 320, 290)
    usos.usos_cpu_todos()

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

def btn_processos():
    usos.mostra_pid()

def btn_arquivos():
    usos.mostra_arquivos()

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

    elif x == 5:
        tela_processos2.fill(white)
        tela_processos.fill(white)
        botoes(447, 5, 125, 36)
        btn_processos()

    elif x == 6:
        tela_processos2.fill(white)
        tela_processos.fill(white)
        botoes(572, 5, 115, 36)
        btn_arquivos()

def main():
    global tela
    global fechou
    menu_list = 0
    tela.fill((255, 255, 255))
    pygame.init()

    usos.alteracao()

    ####################################################
    # Botões do Menu
    btn_resumo = pygame.Rect(5, 5, 100, 36)
    btn_ethernet = pygame.Rect(115, 5, 104, 36)
    btn_memoria = pygame.Rect(225, 5, 104, 36)
    btn_cpu = pygame.Rect(335, 5, 60, 36)
    btn_hd = pygame.Rect(400, 5, 45, 36)
    btn_processos = pygame.Rect(447, 5, 125, 36)
    btn_arquivos = pygame.Rect(572, 5, 115, 36)
    #####################################################

    #####################################################
    #variaveis e atributos para o text box para ethernet
    input_box_pid = pygame.Rect(55, 220, 140, 32)
    input_box_arquivos = pygame.Rect(10, 55, (largura_tela - 2*10), 32)
    button_original = pygame.Rect(55, 460, 140, 32)
    button_cliente = pygame.Rect(55, 500, 140, 32)
    button_servidor = pygame.Rect(55, 540, 140, 32)
    color_active = pygame.Color('dodgerblue2')
    color = black
    color4 = black
    active = False
    active1 = False

    text = ''
    text1 = ''

    ######################################################

    ######################################################

    while not fechou:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 5:
                    variaveis.scroll_y = variaveis.scroll_y - 15
                if event.button == 4:
                    if variaveis.scroll_y > 0:
                        variaveis.scroll_y = 0
                    else:
                        variaveis.scroll_y = variaveis.scroll_y + 15

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
                if btn_processos.collidepoint(event.pos):
                    menu_list = 5
                if btn_arquivos.collidepoint(event.pos):
                    menu_list = 6
                ###############################################

                ###############################################
                    # Clique TextBox PID
                if input_box_pid.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = not active
                else:
                    active = False
                # Mudar a cor do text box
                color = color_active if active else black
                ############################################

                ###############################################
                # Clique TextBox arquivos
                if input_box_arquivos.collidepoint(event.pos):
                    # Toggle the active variable.
                    active1 = not active1
                else:
                    active1 = False
                # Mudar a cor do text box
                color4 = color_active if active1 else black
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
                    if menu_list >= 7:
                        menu_list = 6
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
                            variaveis.pid = text
                            if variaveis.pid.isdigit():
                                variaveis.pid = int(text)
                                variaveis.lista_enviar = [variaveis.pid, variaveis.diretorio]
                            else:
                                print("Digite Números")

                            #Resetar texto
                            text = ''

                            #Verificar se o pid é válido
                            try:
                                usos.info_pid_ethernet(variaveis.pid)
                            except:
                                pass

                        elif event.key == pygame.K_BACKSPACE:
                            text = text[:-1]
                        else:
                            text += event.unicode
                ###############################################

                ###############################################
                #TextBox Arquivos
                if menu_list == 6:
                    if active1:
                        if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                        #Clique do enter
                            #trasnformar texto em numero já com regex
                            variaveis.diretorio = text1
                            variaveis.lista_enviar = [variaveis.pid, variaveis.diretorio]
                            #Resetar texto
                            text1 = ''

                            try:
                                usos.mostra_arquivos()
                            except Exception as error:
                                print(str(error))

                        elif event.key == pygame.K_BACKSPACE:
                            text1 = text1[:-1]
                        else:
                            text1 += event.unicode
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
            variaveis.pid_list = 0
        else:
            color2 = color_active
            color1 = black
            ###############################################################
            # Montar lista com PIDs
            variaveis.contador_pid = 60
            if variaveis.contador_pid == 60:
                variaveis.pid_list = psutil.pids()
                variaveis.contador_pid = 0
            ###############################################################

        if usos.servidor == True:
            color3 = color_active
            # Verificar se o pid é válido
            try:
                usos.info_pid_ethernet(variaveis.pid)
            except Exception as erro:
                print(str(erro))
                pass
        else:
            color3 = black

        ##############################################################

        ##############################################################
        # Text Box Ethernet
        if menu_list == 1:
            txt_surface = font.render(text, True, color)
            width = max(200, txt_surface.get_width() + 10)
            input_box_pid.w = width
            tela.blit(txt_surface, (input_box_pid.x + 5, input_box_pid.y + 5))
            pygame.draw.rect(tela, color, input_box_pid, 2)

            # Print botoes cliente_servidor
            pygame.draw.rect(tela, color1, button_cliente)
            pygame.draw.rect(tela, color2, button_original)
            pygame.draw.rect(tela, color3, button_servidor)
        ###############################################################

        ###############################################################
        #TextBox Arquivos
        if menu_list == 6:
            txt_surface = font.render(text1, True, color4)
            width = max(largura_tela - 2*10, txt_surface.get_width() + 10)
            input_box_arquivos.w = width
            tela.blit(txt_surface, (input_box_arquivos.x + 5, input_box_arquivos.y + 5))
            pygame.draw.rect(tela, color4, input_box_arquivos, 2)

        usos.alteracao()
        usos.funcionamento_servidor()
        variaveis.contador_pid += 1
        menu_animation(menu_list)
        relogio.tick(60)
        pygame.display.flip()
        pygame.display.update()
    pygame.display.quit()
    pygame.quit()

if __name__ == '__main__':
    main()
