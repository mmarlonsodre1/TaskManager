import psutil
import datetime
import cpuinfo

def name():
    return cpuinfo.get_cpu_info()['brand']

def arch():
    return cpuinfo.get_cpu_info()['arch']

def bits():
    return cpuinfo.get_cpu_info()['bits']


def conversor(n):
    simbolos = (' GHz', ' THz', ' PHz', ' EHz', ' ZHz', ' YHz')
    prefixo = {}
    for i, s in enumerate(simbolos):
        prefixo[s] = 1 << (i + 1) * 10

    for s in reversed(simbolos):
        if n >= prefixo[s]:
            valor = float(n) / prefixo[s]
            return '%.1f%s' % (valor, s)
    return "%sB" % n


def freq_atual():
    return conversor(psutil.cpu_freq().current)

def freq_min():
    return psutil.cpu_freq().min

def freq_max():
    return conversor(psutil.cpu_freq().max)

def cores():
    return psutil.cpu_count()

def physical_processors():
    return psutil.cpu_count(logical=False)

def porcentagem_todos():
    return psutil.cpu_percent(percpu=True)

def porcentagem():
    return psutil.cpu_times_percent().user

def tempo_ativo():
    return datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%H:%M:%S")

