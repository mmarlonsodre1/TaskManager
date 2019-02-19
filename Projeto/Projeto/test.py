import psutil
print(psutil.pids())

a = psutil.pids()
lista = []
for x in a:
    lista.append(x)
    print(lista)