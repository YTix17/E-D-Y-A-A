"""Desarrolle un algoritmo que entregue la secuencia de Collatz de un número entero calculado a partir del promedio de N números ingresados por teclado.
(N corresponde a [último dígito de su código + 3] )."""
#Mi código es 2221881, o sea, 1 + 3 = 4 dígitos pediré
n = 4
lista = []
for i in range (n):
    valor = int(input("Ingrese un valor entero: "))
    lista.append(valor)
suma = sum(lista)
promedio = suma/n
#Después de recibir el promedio de los valores, pasamos a recrear la serie de Collatz
if promedio > 0:
    while promedio != 1:
        if promedio % 2 == 1:  
            promedio = promedio * 3 + 1
        else:
            promedio //= 2
        print(promedio)
else:
    print("El número que tecleo no es válido")
