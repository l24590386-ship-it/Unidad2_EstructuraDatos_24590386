# Algoritmo para calcular el factorial de un número usando recursividad

# 1. Definir la clase Factorial
# 2. Crear el constructor __init__ que reciba n y lo guarde en self.n
# 3. Definir el método calcularFactorial(num):
#    3.1. Si num es 1, retornar 1
#    3.2. Si no, retornar num * calcularFactorial(num - 1) (llamada recursiva)
# 4. Definir el método imprimir():
#    4.1. Llamar a calcularFactorial usando self.n
#    4.2. Imprimir el resultado
# 5. Crear un objeto de la clase Factorial con el número deseado (ej. 5)
# 6. Llamar al método imprimir() del objeto
# 7. Fin del algoritmo

"""
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))  # 120
"""
class Factorial: 
    def __init__(self,n ):
        self.n=n 
    
    def calcularFactorial(self, num ):
        if num == 1:
            return 1
        else:
            return num * self.calcularFactorial(num-1)

    def imprimir(self):
        print(self.calcularFactorial(self.n))

objfac = Factorial (5)
objfac.imprimir()

        
        