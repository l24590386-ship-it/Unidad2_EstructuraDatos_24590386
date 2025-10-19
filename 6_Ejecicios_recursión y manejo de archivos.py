#INSTITUTO TECNOLOGICO DE SAN JUAN DEL RIO 
#ESTRUCTURA DE DATOS 
#UNIDAD 2
#NOMBRE : ROCIO MOLINA MONROY 
#-----------------------------------------------------------

#EJERCICIO 1 imprimir los numeros pares desde 2 hasta un entero positivo N.
"""
import time
import tracemalloc  

# MeMc: Medición de tiempo y memoria para imprimir pares hasta N
tracemalloc.start()  
start_time_ns = time.time_ns()  

def imprimirParesHastaN(n):
    if type(n) != int or n < 1: 
        raise Exception("n debe ser entero positivo.")
    n -= n % 2   
    imprimirParesHastaNAux(n)
    print()

def imprimirParesHastaNAux(n):
    if n == 0: 
        return
    else: 
        imprimirParesHastaNAux(n - 2)
        print(n, end=" ")

imprimirParesHastaN(8)

end_time_ns = time.time_ns() 
current, peak = tracemalloc.get_traced_memory()  
tracemalloc.stop()  
# Resultados
print(f"\nTiempo de ejecución: {end_time_ns - start_time_ns} nanosegundos")
print(f"Memoria actual usada: {current} bytes")
print(f"Pico máximo de memoria: {peak} bytes")
"""

#EJERCICIO 2 imprimir los numeros impares entre dos enteros M y N con M<N.
"""
import time
import tracemalloc

# MeMc: Medición de tiempo y memoria para imprimir impares entre m y n
tracemalloc.start()
start_time_ns = time.time_ns()

def imprimirImparesEntreMyN(m, n):
    if type(m) != int:
        raise Exception("m debe ser entero positivo.")
    if type(n) != int or n <= m:
        raise Exception("n debe ser entero positivo y mayor que m.")
    m = m + 1 if m % 2 == 0 else m
    n = n - 1 if n % 2 == 0 else n
    imprimirImparesEntreMyNAux(m, n)
    print()

def imprimirImparesEntreMyNAux(m, n):
    if m > n:
        return
    else:
        print(m, end=" ")
        imprimirImparesEntreMyNAux(m + 2, n)

imprimirImparesEntreMyN(2, 8)

end_time_ns = time.time_ns()
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

print(f"\nTiempo de ejecución: {end_time_ns - start_time_ns} nanosegundos")
print(f"Memoria actual usada: {current} bytes")
print(f"Pico máximo de memoria: {peak} bytes")
"""
#EJERCICIO 3 suamr todos los numeros pares de una lista de enteros. 
"""
import time
import tracemalloc

# MeMc: Medición de tiempo y memoria para sumar pares hasta N
tracemalloc.start()
start_time_ns = time.time_ns()

def sumarPares(n):
    if type(n) != int or n < 3:
        raise Exception("n debe ser entero positivo.")
    n -= n % 2
    return sumarParesAux(n)

def sumarParesAux(n):
    if n == 0:
        return 0
    else:
        return sumarParesAux(n - 2) + n

resultado = sumarPares(8)
print(f"Suma de pares hasta 8: {resultado}")

end_time_ns = time.time_ns()
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

print(f"Tiempo de ejecución: {end_time_ns - start_time_ns} nanosegundos")
print(f"Memoria actual usada: {current} bytes")
print(f"Pico máximo de memoria: {peak} bytes")
"""

#EJERCICIO 4 contar la cantidad de digitos de un numero entero.
"""
import time
import tracemalloc

# MeMc: Medición de tiempo y memoria para contar dígitos
tracemalloc.start()
start_time_ns = time.time_ns()

def contarDigitos(n):
    if type(n) != int or n < 0:
        raise Exception("n debe ser entero no negativo.")
    return contarDigitosAux(n)

def contarDigitosAux(n):
    if n < 10:
        return 1
    else:
        return contarDigitosAux(n // 10) + 1

resultado = contarDigitos(123456)
print(f"Número de dígitos: {resultado}")

end_time_ns = time.time_ns()
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

print(f"Tiempo de ejecución: {end_time_ns - start_time_ns} nanosegundos")
print(f"Memoria actual usada: {current} bytes")
print(f"Pico máximo de memoria: {peak} bytes")
"""
#EJERCICIO 5 sumar los digitos de un numero entero.
"""
import time
import tracemalloc

# MeMc: Medición de tiempo y memoria para sumar dígitos
tracemalloc.start()
start_time_ns = time.time_ns()

def sumarDigitos(n):
    if type(n) != int or n < 0:
        raise Exception("n debe ser entero no negativo.")
    return sumarDigitosAux(n)

def sumarDigitosAux(n):
    if n < 10:
        return n
    else:
        return sumarDigitosAux(n // 10) + n % 10

resultado = sumarDigitos(123456)
print(f"Suma de los dígitos: {resultado}")

end_time_ns = time.time_ns()
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

print(f"Tiempo de ejecución: {end_time_ns - start_time_ns} nanosegundos")
print(f"Memoria actual usada: {current} bytes")
print(f"Pico máximo de memoria: {peak} bytes")
"""
#EJERCICIO 6 invertir el orden de los digitos de un numero entero.
import time
import tracemalloc

# MeMc: Medición de tiempo y memoria para invertir un número entero
tracemalloc.start()
start_time_ns = time.time_ns()

def contarDigitos(n):
    if type(n) != int or n < 0:
        raise Exception("n debe ser entero no negativo.")
    return contarDigitosAux(n)

def contarDigitosAux(n):
    if n < 10:
        return 1
    else:
        return contarDigitosAux(n // 10) + 1

def invertirEntero(n):
    if type(n) != int or n < 1:
        raise Exception("n debe ser entero positivo.")
    return invertirEnteroAux(n)

def invertirEnteroAux(n):
    if n < 10:
        return n
    else:
        return (n % 10) * 10**contarDigitos(n // 10) + invertirEnteroAux(n // 10)

resultado = invertirEntero(123456789)
print(f"Número invertido: {resultado}")

end_time_ns = time.time_ns()
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

print(f"Tiempo de ejecución: {end_time_ns - start_time_ns} nanosegundos")
print(f"Memoria actual usada: {current} bytes")
print(f"Pico máximo de memoria: {peak} bytes")
