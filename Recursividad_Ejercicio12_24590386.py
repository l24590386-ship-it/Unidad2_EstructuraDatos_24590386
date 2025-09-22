# Algoritmo para multiplicar dos números usando recursividad (suma repetida)

# 1. Definir la clase Multiplicar
# 2. Crear el constructor __init__ que reciba los números a y b, y los guarde en self.a y self.b
# 3. Definir el método calcular(a, b):
#    3.1. Si b es 0, retornar 0 (caso base)
#    3.2. Si no, retornar a + calcular(a, b-1) (llamada recursiva)
# 4. Definir el método imprimir():
#    4.1. Llamar al método calcular usando self.a y self.b
#    4.2. Imprimir el resultado
# 5. Crear un objeto de la clase Multiplicar con los números deseados
# 6. Llamar al método imprimir() del objeto
# 7. Fin del algoritmo

"""
def multiplicar(a, b):
    if b == 0:
        return 0
    else:
        return a + multiplicar(a, b-1)

print(multiplicar(3, 4))  # 12
"""
class Multiplicar:
    def __init__(self, a, b):
        self.a = a  
        self.b = b  

    def calcular(self, a, b):
        if b == 0:  
            return 0
        else:
            return a + self.calcular(a, b - 1) 

    def imprimir(self):
        print(self.calcular(self.a, self.b))  

objMultiplicar = Multiplicar(3, 4)
objMultiplicar.imprimir()  # Resultado: 12