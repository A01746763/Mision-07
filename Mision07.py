# Autor: Jonathan Sanabria Rocha
# Solucion de problemas con ciclos While

import sys

def probarDivisiones():
    dividendo = int(input("Dame el dividendo: "))
    divisor = int(input("Dame el divisor: "))

    cociente = 0
    dividendoInt=dividendo
    residuo = 0

    while dividendo >= divisor:
        dividendo = dividendo - divisor
        cociente = cociente + 1
        residuo = dividendo
    if dividendo < divisor:
        print("%d / %d = %d, sobra %d" % (dividendoInt, divisor, cociente, dividendo))
    else:
        print("%d / %d = %d, sobra %d" % (dividendoInt, divisor, cociente, residuo))


def encontrarMayor():
        numeroMayor = 0
        valor = int(input("Teclea un número [-1 para salir]: "))
        if valor == -1:
         print("No hay valor mayor")
        while valor != -1:
            if valor > numeroMayor:
                numeroMayor = valor
            valor = int(input("Teclea un número [-1 para salir]: "))
        print  ("El mayor es: ", numeroMayor)


def main():
    eleccion = -1
    while eleccion != 3:
        print("""Misión 07. Ciclos while
    Autor: Jonathan Sanabria Rocha
    Matrícula: A01746763
    1. Calcular divisiones
    2. Encontrar el mayor
    3. Salir""")
        eleccion = int(input("Teclea tu opción: "))
        if eleccion == 1:
            probarDivisiones()
        elif eleccion == 2:
            encontrarMayor()
        elif eleccion == 3:
          print("""
    Gracias por usar este programa, regresa pronto.""")

    sys.exit()

main()

main()


