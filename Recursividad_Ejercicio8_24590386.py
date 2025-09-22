# Algoritmo para calcular el máximo común divisor (MCD) usando recursividad

# 1. Definir la clase MCD
# 2. Crear el constructor __init__ que reciba los números a y b y los guarde en self.a y self.b
# 3. Definir el método calcular(a, b):
#    3.1. Si b es 0, retornar a (caso base)
#    3.2. Si no, retornar calcular(b, a % b) (llamada recursiva)
# 4. Definir el método imprimir():
#    4.1. Llamar al método calcular usando self.a y self.b
#    4.2. Imprimir el resultado
# 5. Crear un objeto de la clase MCD con los números deseados
# 6. Llamar al método imprimir() del objeto
# 7. Fin del algoritmo

"""
def mcd(a, b):
    if b == 0:
        return a
    else:
        return mcd(b, a % b)

print(mcd(48, 18))  # 6
"""
class MCD:
    def __init__(self, a, b):
        self.a = a  
        self.b = b 

    def calcular(self, a, b):
        if b == 0:  
            return a
        else:
            return self.calcular(b, a % b) 
    def imprimir(self):
        print(self.calcular(self.a, self.b))  

objMCD = MCD(48, 18)
objMCD.imprimir() 