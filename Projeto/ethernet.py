import psutil

def conversor(n):
    simbolos = (' KB', ' MB', ' GB', ' TB', ' PB', ' EB', ' ZB', ' YB')
    prefixo = {}
    for i, s in enumerate(simbolos):
        prefixo[s] = 1 << (i + 1) * 10

    for s in reversed(simbolos):
        if n >= prefixo[s]:
            valor = float(n) / prefixo[s]
            return '%.1f%s' % (valor, s)
    return "%sB" % n


def enviados():
    return conversor(psutil.net_io_counters().bytes_sent)

def recebidos():
    return conversor(psutil.net_io_counters().bytes_recv)

def get_ip():
    ifaces = psutil.net_if_addrs()
    networks = list()
    for k, v in ifaces.items():
        ip = v[1].address
        ifnet= ip

        networks.append(ifnet)
    return networks[1]

def get_mac():
    ifaces = psutil.net_if_addrs()
    networks = list()
    for k, v in ifaces.items():
        ip = v[0].address
        ifnet= ip

        networks.append(ifnet)
    return (networks[0])

def get_mask():
    ifaces = psutil.net_if_addrs()
    networks = list()
    for k, v in ifaces.items():
        ip = v[1].netmask
        ifnet= ip

        networks.append(ifnet)
    return networks[0]