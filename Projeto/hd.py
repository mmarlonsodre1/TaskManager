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

def total():
    return conversor(psutil.disk_usage('/').total)

def utilizado():
    return conversor(psutil.disk_usage('/').used)

def disponivel():
    return conversor(psutil.disk_usage('/').free)

def porcentagem():
    return psutil.disk_usage('/').percent