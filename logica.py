import os

entrada = str(input()) # Entrada de texto de la nota

def guardar(titulo, contenido, ruta):
    archivo = open(f'{ruta}\{titulo}.txt', 'w')
    archivo.write(contenido)
    archivo.close()

def localizacion(ruta):
    if ruta == 'y':
        ruta = input('Ingresa una ruta: ')
        guardar(nombre, entrada, ruta)
    else:
        guardar(nombre, entrada, ruta='C:\\Users\\Nejosudo\\Desktop\\2024')

r = input('¿Guardar? y/n')

if r == 'y':
    nombre= input('Ingresa titulo de tu nota')
    ruta = input('Guardar en otra ruta? y/n predeterminado: C:\\Users\\Nejosudo\\Desktop')
    localizacion(ruta)
else:
    print('saliendo.')
    exit()

