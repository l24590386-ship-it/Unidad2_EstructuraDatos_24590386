# Algoritmo para imprimir una pirámide de asteriscos usando recursividad

# 1. Definir la clase Piramide
# 2. Crear el constructor __init__ que reciba la altura n y la guarde en self.n
# 3. Definir el método calcular(n):
#    3.1. Si n es 0, retornar (caso base)
#    3.2. Si no, llamar recursivamente a calcular(n - 1)
#    3.3. Imprimir '*' repetido n veces
# 4. Definir el método imprimir():
#    4.1. Llamar al método calcular usando self.n
# 5. Crear un objeto de la clase Piramide con la altura deseada
# 6. Llamar al método imprimir() del objeto
# 7. Fin del algoritmo
"""
def piramide(n):
    if n == 0:
        return
    piramide(n-1)
    print('*' * n)

piramide(5)
"""
class Piramide:
    def __init__(self, n):
        self.n = n  

    def calcular(self, n):
        if n == 0:  
            return
        self.calcular(n - 1)  
        print('*' * n)  
    def imprimir(self):
        self.calcular(self.n)  

objPiramide = Piramide(5)
objPiramide.imprimir()
