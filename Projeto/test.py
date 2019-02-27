import socket

HOST = socket.gethostname()  # IP do servidor
PORTA = 9999  # Porta do servidor
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (HOST, PORTA)

msg = input("Mensagem: ")
udp.sendto(msg.encode('utf-8'), dest)

while msg != 'exit':
    (msg, servidor) = udp.recvfrom(1024)
    print(servidor, msg.decode('utf-8'))
    msg = input()
    udp.sendto(msg.encode('utf-8'), dest)
udp.close()