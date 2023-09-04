import random

DIFICULTADES = ['F', 'M', 'D', 'MD', 'I']

RENDIRSE_OPCIONES_SI = ['S', 'SI']
RENDIRSE_OPCIONES_NO = ['N', 'NO']

FRASES = [
    'RINDETE, NO VAS A GANAR!',
    'ES INUTIL SEGUIR INTENTANDO!',
    'NUNCA GANARAS!',
    'NO VAS A ADIVINARLO!',
    'SOLO ESTAS PERDIENDO EL TIEMPO!',
    'ES MEJOR DARSE POR VENCIDO/A!',
    'ES IMPOSIBLE QUE LO ADIVINES!',
    'OLVIDALO, DE NADA SIRVE SEGUIR INTENTANDO!',
    'TU DESTINO ES PERDER!',
    'NO HAY POSIBILIDAD DE QUE GANES!',
    'LA SUERTE NO ESTA DE TU LADO!',
    'NO TIENES OPORTUNIDAD DE GANAR!',
    'NO ERES RIVAL PARA ESTE JUEGO!',
    'LA VICTORIA NO ES PARA TI!',
    'NO PODRAS ESCAPAR DE LA DERROTA!',
    'LA DERROTA TE PERSIGUE!',
    'CADA INTENTO ES UN FRACASO SEGURO!',
    'TUS POSIBILIDADES DE GANAR SON NULAS!',
    'ESTAS CONDENADO A PERDER!',
    'ES MEJOR QUE PIERDAS LA ESPERANZA!',
    'GANAR ES UNA ILUSION LEJANA PARA TI!',
    'ABANDONA TU ESPERANZA DE GANAR!',
    'TU PERSEVERANCIA ES ADMIRABLE, AUNQUE INUTIL!',
    'GANAR ESTA FUERA DE TU ALCANCE!',
    'CON CADA INTENTO SOLO CONSIGUES FRACASAR!',
    'TUS INTENTOS SON PATETICOS!',
    'DEBERIAS RENDIRTE!'
]


def presentacion_juego():
    print('-----------------------------------------------')
    print('-------------* ADIVINA EL NUMERO *-------------')
    print("-------------------  /\_/\  -------------------")
    print("------------------- ( o.o ) -------------------")
    print('-----------------------------------------------')

def dibujar_calavera():
    print("          ______")
    print("         /      \\")
    print("        |  X   X |")
    print("         \\   ^  /")
    print("          ||||||")


def dibujar_gato():
    print("      /\_/\ ")
    print("     ( o.o )")


def deseas_rendirte():
    while True:
        print(' ')
        print('Deseas rendirte?.')
        _rendirse = input('(s/n):')
        print(' ')

        _rendirse = _rendirse.strip().upper()

        if _rendirse in RENDIRSE_OPCIONES_SI:
            return True    
        elif _rendirse in RENDIRSE_OPCIONES_NO:
            return False
        else:
            print('Elige una opcion valida para rendirte o seguir jugando!.')

# ------------------------------------------------------------
# ------------------------- COMIENZO -------------------------
# ------------------------------------------------------------
print(' ')
presentacion_juego()
print(' ')
print('Ingresa la dificultad en la que quieres jugar:')
print('Muy facil   (       del 1 al 10        )   ---> MF')
print('Facil       (       del 1 al 100       )   ---> F')
print('Medio       (       del 1 al 1000      )   ---> M')
print('Dificil     ( del 1 al 50  - sin ayuda )   ---> D')
print('Muy dificil ( del 1 al 100 - sin ayuda )   ---> MD')
print('IMPOSIBLE   (     I M P O S I B L E    )   ---> I')
print(' ')

# Seleccion de dificultad
while True:
    dificultad = input('Tu eleccion: ')
    dificultad = dificultad.strip().upper()

    if dificultad == 'MF':
        print(' ')
        print('...')
        print(' ')
        print('En serio?... Muy facil? ._.')
        print('Eres la persona mas patetica que he conocido!')
        print('Elige una dificultad mas interesante')
        print(' ')

    if dificultad in DIFICULTADES:
        break
    else:
        print('Ingresa una dificultad (F, M, D, MD, I)')

if dificultad == 'F':
    numero_generado = random.randint(1, 100)
elif dificultad == 'M':
    numero_generado = random.randint(1, 1000)
elif dificultad == 'D':
    numero_generado = random.randint(1, 50)
elif dificultad == 'MD':
    numero_generado = random.randint(1, 100)
else:
    numero_generado = random.randint(1, 999999)
    print(' ')
    print(' -------------------------- ')
    print(' - NUNCA GANARAS EL JUEGO - ')
    print(' -------------------------- ')
    dibujar_calavera()

print(' ')

# Comienzo del juego

# Cada vez que contador llegue a 5 se ejecutara la funcion deseas_rendirte
contador = 0

while True:
    numero_ingresado = input('Ingresa un numero: ')

    try:
        numero_ingresado = int(numero_ingresado.strip())

        if numero_ingresado == numero_generado:
            if dificultad == 'I':
                print(' ')
                print('...')
                print(' ')
                print('Has hecho lo imposible...')
                print(' ')
                print('GANASTE EN LA MAXIMA DIFICULTAD.')
                print(f'{numero_generado} ES EL NUMERO QUE HE ELEGIDO Y LO HAS ADIVINADO!.')
                print(' ')
                print('Pero...')
                print(' ')
                print('---------------------------------------------------------------')
                print('- ES IMPOSIBLE QUE VUELVAS A GANARME EN ESTE MODO MUAJAJAJAJA -')
                print('---------------------------------------------------------------')
                print(' ')
                break

            print(f'Excelente! Lo has adivinado, {numero_generado} es el numero que he elegido.')
            break
        

        if contador == 5:
            se_rinde = deseas_rendirte()

            if se_rinde:
                if dificultad == 'I':
                    print(' ')
                    print('----------------------------------------')
                    print('- MUAJAJAJA TE DIJE QUE NUNCA GANARIAS -')
                    print('----------------------------------------')
                    dibujar_calavera()
                    print(' ')
                    break

                print('Es una lastima que te rindas :(')
                print('Vuelve a jugar cuando quieras!')
            else:
                contador = 0
        else:
            contador += 1

        
        if dificultad != 'I':
            print(f'{numero_ingresado} no es el numero que he elegido, vuelve a intentarlo.')

            if dificultad == 'F' or dificultad == 'M':
                if numero_ingresado < numero_generado:
                    print('Prueba con un numero mas grande.')
                else:
                    print('Prueba con un numero mas chico.')

        else:
            frase_seleccionada = random.choice(FRASES)
            print(frase_seleccionada)

        print(' ')

    except ValueError:
        print(f'{numero_ingresado} no es valido, debes ingresar un numero!.')

print(' ')
dibujar_gato()
print(' ')
print('Gracias por jugar!')
print(' ')

# PYTHON 3.11.5