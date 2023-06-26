import math
import string
import random


#Funcion para hacer el tablero.
def tablero(tamanio):
    letras = list(" " + string.ascii_uppercase[: tamanio])     #Se utiliza string.ascii_uppercase[: tamanio] para crear una lista de letras mayúsculas del tamaño del tablero.
    tablero = [[' ' for _ in range((tamanio + 1))] for _ in range((tamanio + 1))]
    tablero[0] = letras

    for i in range(1, (tamanio + 1)):
        tablero[i][0] = str(i)
    
    return tablero
    
#Funcion para imprimir el tablero.
def imprimir_tablero(tablero):        
    
    for fila in tablero:
        print('-'.join(fila))

# Función para colocar los barcos de forma aleatoria
def colocar_barcos(tablero,barcos):
    tamanio = len(tablero) - 1 
    posicion_barcos = []
    
    for _ in range(barcos):
        fila = random.choice(string.ascii_uppercase[0:tamanio])
        columna = random.randint(1, tamanio)
        filas_columnas = (fila,columna)
        if filas_columnas not in posicion_barcos:
            posicion_barcos.append(filas_columnas)
        
    return posicion_barcos
        
# Función para disparar y comprobar si se acerto o no, y en ese caso poner X, O, o devuelve false si se ingresa una coordenada incorrecta.
def disparo(tablero, columna, fila, posicion_barcos):
    tamanio = len(tablero) - 1
    
    if fila not in range(1, tamanio + 1) or columna not in string.ascii_uppercase[:tamanio]:
        print("Coordenada inválida.")
        return False
    
    letra_fila = string.ascii_uppercase.index(columna) + 1
    coord = (columna,fila)
    
    if coord in posicion_barcos:
        print("¡Impacto! El disparo ha acertado en un barco.")
        tablero[fila][letra_fila] = "X"
        return True
    else:
        print("Agua. El disparo no ha acertado en ningún barco.")
        tablero[fila][letra_fila] = "O"
        
        
#Función para calcular el número de turnos
def turnos(nivel,tamanio):    
    if nivel == 1:
        #Se usa la función math.ceil, para redondear el número hacia arriba.
        turno = math.ceil((tamanio**2) * 0.70)  
        return turno
    elif nivel == 2:
        turno = math.ceil((tamanio**2) * 0.50)
        return turno
    elif nivel == 3:
        turno = math.ceil((tamanio**2) * 0.30)
        return turno  

###########################################################################################################################################################################


def jugar ():
    print ("\n")
    nivel = int(input("Ingresa la dificultad: 1- Fácil 2- Intermedio 3- Díficil: "))
    while nivel < 1 or nivel > 3:
        print("Entrada invalida. Ingrese un número del 1 al 3 para seleccionar la dificultad.")
        nivel = int(input("Ingresa la dificultad: 1- Fácil 2- Intermedio 3- Díficil: "))
      
    tamanio = int (input("Ingresa el tamaño del tablero. El tamaño mínimo es 3x3, y el máximo es 10x10. Ingresa un número del 3 al 10: "))
    while tamanio < 3 or tamanio > 10:
        print("Entrada invalida. ")
        tamanio = int(input("Ingresa el tamaño del tablero. El tamanio minimo es 3x3, y el maximo es 10x10. Ingresa un numero del 3 al 10: "))

    barcos = int(input(f"Ingresa la cantidad de barcos. La cantidad de barcos debe ser menor o igual a {tamanio}: "))
    while barcos <= 0 or barcos > tamanio:
        print ("Entrada invalida")
        barcos = int(input(f"Ingresa la cantidad de barcos a derribar. La cantidad de barcos debe ser menor o igual a {tamanio}: "))
 
    board = tablero(tamanio)
    posicion_barcos = colocar_barcos(board,barcos)
    turnos1 = turnos(nivel,tamanio)
    impactos = 0
    lista_tiros = []
    disparos_realizados = 0 
    
    while turnos1 > 0 and impactos < barcos:
        print("Tablero:")
        imprimir_tablero(board)
        coordenada = input("Ingrese las coordenadas del disparo. Por ejemplo: A5: ").upper()
        columna = coordenada[0].upper()
        fila = int(coordenada[1:])
        disparo(board, columna, fila, posicion_barcos)
        gol = disparo(board, columna, fila, posicion_barcos)
        while gol == True:
            impactos += 1
            break
            
        while gol == False:
            coordenada = input("Ingrese las coordenadas del disparo. Por ejemplo: A5: ").upper()
            columna = coordenada[0].upper()
            fila = int(coordenada[1:])
            disparo(board, columna, fila, posicion_barcos)
            gol = disparo(board, columna, fila, posicion_barcos)
        
        disparos_realizados = disparos_realizados + 1
        if impactos == barcos: 
            print("Ganaste maquina!!! Sos el campeón de Not Batalla Naval")
            break   #Finaliza el juego ya que derribaste todos los barcos. 
    
        turnos1 = turnos1 - 1 
    
   
        print(f"Te quedan {turnos1} tiros")
        print(f"Embocaste {impactos} barcos")
        lista_tiros.append(coordenada)
    
    
    print("Estos fuernos tus disparos:")
    print(lista_tiros)
    print(f"Disparaste {disparos_realizados}")
    print(f"Derribaste {impactos}")

jugar()

    
    
    
    
   
        