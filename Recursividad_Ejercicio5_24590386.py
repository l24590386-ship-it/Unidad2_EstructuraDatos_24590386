# Algoritmo para calcular el n-ésimo número de Fibonacci usando recursividad

# 1. Definir la clase Fibonacci
# 2. Crear el constructor __init__ que reciba num1 (posición en la serie) y lo guarde en self.num1
# 3. Definir el método calcularFibo(num1):
#    3.1. Si num1 es 0 o 1, retornar num1 (casos base: los dos primeros números de Fibonacci)
#    3.2. Si no, retornar calcularFibo(num1 - 1) + calcularFibo(num1 - 2) (llamadas recursivas)
# 4. Definir el método imprimir():
#    4.1. Llamar a calcularFibo usando self.num1
#    4.2. Imprimir el resultado
# 5. Crear un objeto de la clase Fibonacci con la posición deseada (ej. 6)
# 6. Llamar al método imprimir() del objeto
# 7. Fin del algoritmo

"""
def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6))  # 8
"""
class Fibonacci:
    def __init__(self,num1):
        self.num1 = num1

    def calcularFibo(self,num1):
        if num1 == 0 or num1 == 1:
            return num1
        else:
            return self.calcularFibo(num1-1) + self.calcularFibo(num1-2)
        
    def imprimir(self):
        print(self.calcularFibo(self.num1)) 

objFibo =Fibonacci(6)
objFibo.imprimir()
