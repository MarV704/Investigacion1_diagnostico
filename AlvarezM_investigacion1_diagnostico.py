#### Codigo 8
 mayor de tres numeros
 Pide tres numeros al usuario e imprime el mayor de ellos.

numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))
numero3 = int(input("Ingresa el tercer número: "))

el_mayor = max(numero1, numero2, numero3)

print(f"El número mayor es: {el_mayor}")

#### Codigo 9
 Suma de digitos
 Pide un numero entero al usuario y calcula la suma de sus digitos.

numero_str = input("Ingresa un número entero: ")

suma_digitos = 0

for digito_char in numero_str:
    suma_digitos += int(digito_char)

print(f"La suma de los dígitos es: {suma_digitos}")

#### Codigo 10
 contador de palabras
 Pide una frase al usuario e imprime cuantas palabras contiene.

frase = input("Ingresa una frase: ")

palabras = frase.split()

numero_de_palabras = len(palabras)

print(f"La frase contiene {numero_de_palabras} palabras.")

#### Codigo 11
 lista inversa
 Crea una lista con los numeros del 10 al 1(en orden inverso) y muestrala.

numeros_descendente = list(range(10, 0, -1))

print(numeros_descendente)

#### Codigo 12
 numeros aleatorios
 genera una lista de 5 numeros aleatorios entre 1 y 20.(usa import random).

import random

numeros_aleatorios = []

for _ in range(5):
    numero = random.randint(1, 20)
    numeros_aleatorios.append(numero)

print(f"Tu lista de 5 números aleatorios es: {numeros_aleatorios}")

#### Codigo 13
 adivinar un numero
 Genera un numero aleatorio del 1 al 10. El usuario debe adivinarlo con pistas de "mayor" o "menor".

import random

numero_secreto = random.randint(1, 10)
intentos = 0
adivinado = False

print("Adivina el numero entre el 1 al 10.")

while not adivinado:
    try:
        intento_usuario = int(input("Ingresa tu numero: "))
        intentos += 1

        if intento_usuario < numero_secreto:
            print("Mas alto, intenta de nuevo.")
        elif intento_usuario > numero_secreto:
            print("Mas bajo, intenta de nuevo.")
        else:
            print(f"Adivinaste el número es {numero_secreto} en {intentos} intentos.")
            adivinado = True
    except ValueError:
        print("Entrada no válida. Por favor, ingresa un número entero.")

#### Codigo 14
 Secuencia personalizada
 Crea una lista con todos los multiplos de 3 entre 1 y 30.

multiplos_de_3 = []

for numero in range(1, 31):
    if numero % 3 == 0:
        multiplos_de_3.append(numero)

print(multiplos_de_3)
