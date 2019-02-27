import socket

HOST = ''  # IP do servidor
PORTA = 9999  # Porta do servidor
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
origem = (HOST, PORTA)

udp.bind(origem)

while True:
    (msg, client) = udp.recvfrom(1024)

    if 'exit' == msg.decode('utf-8'):
        print("saindo")
        client.close()
        break

    else:
        msg = "ok..." + msg.decode('utf-8')

    udp.sendto(msg.encode('utf-8'), client)

input("clique para sair")
udp.close()

##################################################
# Memória
socket_cliente.send(porcentagem_memoria.encode('utf-8'))
socket_cliente.send(memoria_total.encode('utf-8'))
socket_cliente.send(memoria_utilizado.encode('utf-8'))
socket_cliente.send(memoria_disponivel.encode('utf-8'))

# CPU
socket_cliente.send(uso_cpu1.encode('utf-8'))
socket_cliente.send(cpu_nome.encode('utf-8'))
socket_cliente.send(cpu_arquitetura.encode('utf-8'))
socket_cliente.send(cpu_palavra.encode('utf-8'))
socket_cliente.send(cpu_max.encode('utf-8'))
socket_cliente.send(cpu_core.encode('utf-8'))
socket_cliente.send(cpu_frequencia_atual.encode('utf-8'))
socket_cliente.send(cpu_nucleos_processador.encode('utf-8'))
socket_cliente.send(cpu_tempo_ativo.encode('utf-8'))

# HD
socket_cliente.send(info_hd.encode('utf-8'))
socket_cliente.send(hd_total.encode('utf-8'))
socket_cliente.send(hd_utilizado.encode('utf-8'))
socket_cliente.send(hd_disponivel.encode('utf-8'))

# ETHERNET
socket_cliente.send(ethernet_mac.encode('utf-8'))
socket_cliente.send(ethernet_ip.encode('utf-8'))
socket_cliente.send(ethernet_mascara.encode('utf-8'))
socket_cliente.send(ethernet_enviados.encode('utf-8'))
socket_cliente.send(ethernet_recebidos.encode('utf-8'))





(larg_memoria) = a[0]
(larg_cpu) = a[5]
(larg_hd) = a[15]
(porcentagem_memoria) = a[1]
(memoria_total) = a[2]
(memoria_utilizado) = a[3]
(memoria_disponivel) = a[4]
# CPU bit/s
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
(info_hd) = a[16]
(hd_total) = a[17]
(hd_utilizado) = a[18]
(hd_disponivel) = a[19]

larg_memoria = (larg_memoria)
larg_cpu = (larg_cpu)
larg_hd = (larg_hd)

4


udp.sendto(larg_memoria, dest)
udp.sendto(larg_cpu, dest)
udp.sendto(larg_hd, dest)




print(servidor, larg_memoria.decode('utf-8'))

            msg = input()

            udp.sendto(larg_memoria.encode('utf-8'), dest)
            udp.sendto(porcentagem_memoria.encode('utf-8'), dest)
            udp.sendto(memoria_total.encode('utf-8'), dest)
            udp.sendto(memoria_utilizado.encode('utf-8'), dest)
            udp.sendto(memoria_disponivel.encode('utf-8'), dest)
            udp.sendto(larg_cpu.encode('utf-8'), dest)
            udp.sendto(uso_cpu1.encode('utf-8'), dest)
            udp.sendto(cpu_nome.encode('utf-8'), dest)
            udp.sendto(cpu_arquitetura.encode('utf-8'), dest)
            udp.sendto(cpu_palavra.encode('utf-8'), dest)
            udp.sendto(cpu_max.encode('utf-8'), dest)
            udp.sendto(cpu_core.encode('utf-8'), dest)
            udp.sendto(cpu_frequencia_atual.encode('utf-8'), dest)
            udp.sendto(cpu_nucleos_processador.encode('utf-8'), dest)
            udp.sendto(cpu_tempo_ativo.encode('utf-8'), dest)
            udp.sendto(larg_hd.encode('utf-8'), dest)
            udp.sendto(info_hd.encode('utf-8'), dest)
            udp.sendto(hd_total.encode('utf-8'), dest)
            udp.sendto(hd_utilizado.encode('utf-8'), dest)
            udp.sendto(hd_disponivel.encode('utf-8'), dest)
            udp.sendto(ethernet_mac.encode('utf-8'), dest)
            udp.sendto(ethernet_ip.encode('utf-8'), dest)
            udp.sendto(ethernet_mascara.encode('utf-8'), dest)
            udp.sendto(ethernet_enviados.encode('utf-8'), dest)
            udp.sendto(ethernet_recebidos.encode('utf-8'), dest)

##################################################
        #Memoria
        porcentagem_memoria = (porcentagem_memoria.decode('utf-8'))
        memoria_total = (memoria_total.decode('utf-8'))
        memoria_utilizado = (memoria_utilizado.decode('utf-8'))
        memoria_disponivel = (memoria_disponivel.decode('utf-8'))
        ##################################################

        ##################################################
        #CPU
        uso_cpu1 = (uso_cpu1.decode('utf-8'))
        cpu_nome = (cpu_nome.decode('utf-8'))
        cpu_arquitetura = (cpu_arquitetura.decode('utf-8'))
        cpu_palavra = (cpu_palavra.decode('utf-8'))
        cpu_max = (cpu_max.decode('utf-8'))
        cpu_core = (cpu_core.decode('utf-8'))
        cpu_frequencia_atual = (cpu_frequencia_atual.decode('utf-8'))
        cpu_nucleos_processador = (cpu_nucleos_processador.decode('utf-8'))
        cpu_tempo_ativo = (cpu_tempo_ativo.decode('utf-8'))

        ##################################################

        ##################################################
        #HD
        info_hd = (info_hd.decode('utf-8'))
        hd_total = (hd_total.decode('utf-8'))
        hd_utilizado = (hd_utilizado.decode('utf-8'))
        hd_disponivel = (hd_disponivel.decode('utf-8'))

        ##################################################

        ##################################################
        #Ethernet
        ethernet_mac = (ethernet_mac.decode('utf-8'))
        ethernet_ip = (ethernet_ip.decode('utf-8'))
        ethernet_mascara = (ethernet_mascara.decode('utf-8'))
        ethernet_enviados = (ethernet_enviados.decode('utf-8'))
        ethernet_recebidos = (ethernet_recebidos.decode('utf-8'))

        ##################################################