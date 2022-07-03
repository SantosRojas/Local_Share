def linea(caracter,cantidad):
    for i in range(cantidad):
        if i<cantidad-1:
            print(f'{caracter}',end='')
        else:
            print(f'{caracter}')
