import os
import sys
import imprimir
import socket
ip=socket.gethostbyname(socket.gethostname())
ruta=sys.argv[1]
os.system('cls')
n=len(f'Carpeta: {ruta}')
m=len(f'Compartiendo Localmente')
try:
    imprimir.linea('=',m)
    print(f'Compartiendo Localmente')
    imprimir.linea('=',m)
    print('\n')
    imprimir.linea('=',n)
    print(f'Carpeta: {ruta}')
    print(f'Ip: {ip}')
    print('Puerto: 8000')
    imprimir.linea('=',n)
    os.system(f'python -m http.server --directory {ruta}')
except Exception as e:
    print(e)

