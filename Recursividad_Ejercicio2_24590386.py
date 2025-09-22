# Algoritmo para calcular la suma de los primeros n números naturales usando recursividad

# 1. Definir la clase Suma_natural
# 2. Crear el constructor __init__ que reciba n y lo guarde en self.n
# 3. Definir el método calcularsum(num):
#    3.1. Si num es 1, retornar 1 (caso base)
#    3.2. Si no, retornar num + calcularsum(num - 1) (llamada recursiva)
# 4. Definir el método imprimir():
#    4.1. Llamar a calcularsum usando self.n
#    4.2. Imprimir el resultado
# 5. Crear un objeto de la clase Suma_natural con el número deseado (ej. 5)
# 6. Llamar al método imprimir() del objeto
# 7. Fin del algoritmo

"""
def suma_natural(n):
    if n == 1:
        return 1
    else:
        return n + suma_natural(n-1)

print(suma_natural(5))  # 15
"""
class Suma_natural:
    def __init__(self,n):
        self.n = n 
    
    def calcularsum (self, num):
        if num == 1:
            return 1
        else:
            return num + self.calcularsum(num-1)

    def imprimir (self):
        print(self.calcularsum(self.n))

objsuma = Suma_natural (5)
objsuma.imprimir()

