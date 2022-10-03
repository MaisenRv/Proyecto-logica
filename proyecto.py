
tamano = int(input("Elige el tamaño del canino\n 1 para pequeño\n 2 para mediano\n 3 para grande\n"))

peso_alimento = 10
peso_agua = 10
porcion = None
porcion_bebida = None
tiempo = 1

ALIMENTO_MAX = 10
BEBIDA_MAX = 10

if (tamano == 1):
    porcion = 0.250
    porcion_bebida = 0.15

elif (tamano == 2):
    porcion = 0.5
    porcion_bebida = 0.35

elif (tamano == 3):
    porcion = 0.75
    porcion_bebida = 0.5
else:
    print("valor no valido")


def alarma():
    print("Debe abastecer el alimento o el liquido del dispositivo")


def alimentar():
    global peso_alimento
    global peso_agua

    if (peso_alimento < 0.5 or peso_agua < 0.5):
        alarma()
        tipo = int(input("Que desea abastecer\n 1 para alimento \n 2 para agua\n"))
        cantidad = float(input("Cuanto desea abastecer"))

        abastecer(tipo, cantidad)
    else:
        peso_alimento = peso_alimento - porcion
        peso_agua = peso_agua - porcion_bebida


def abastecer(tipo, cantidad):
    global peso_alimento
    global peso_agua

    if (tipo == 1 and peso_alimento+cantidad <= ALIMENTO_MAX):
        peso_alimento += cantidad
        print("Abastecido con exito")
        
    elif (tipo == 2 and peso_agua + cantidad <= BEBIDA_MAX):
        peso_agua += cantidad
        print("Abastecido con exito")
    
    elif (peso_alimento+cantidad > ALIMENTO_MAX or peso_agua + cantidad > BEBIDA_MAX):
        print("La cantidad excede la capacidad maxima")
        print("Cantidad de alimento en este momento: ", peso_alimento)
        print("Cantidad de agua en este momento: ", peso_agua)
      
    else:
        print("valor no valido")

if(tiempo == 13):
    alimentar()