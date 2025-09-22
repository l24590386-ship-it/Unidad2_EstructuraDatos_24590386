# Algoritmo para calcular la potencia de un número usando recursividad

# 1. Definir la clase Potencial
# 2. Crear el constructor __init__ que reciba num1 (base) y num2 (exponente) y los guarde en self.num1 y self.num2
# 3. Definir el método calcularPote(num1, num2):
#    3.1. Si num2 es 0, retornar 1 (caso base: cualquier número elevado a 0 es 1)
#    3.2. Si no, retornar num1 * calcularPote(num1, num2 - 1) (llamada recursiva disminuyendo el exponente)
# 4. Definir el método imprimir():
#    4.1. Llamar a calcularPote usando self.num1 y self.num2
#    4.2. Imprimir el resultado
# 5. Crear un objeto de la clase Potencial con la base y exponente deseados (ej. 2 y 3)
# 6. Llamar al método imprimir() del objeto
# 7. Fin del algoritmo


"""
def potencia(a, b):
    if b == 0:
        return 1
    else:
        return a * potencia(a, b-1)

print(potencia(2, 3))  # 8
"""

class Potencial:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def calcularPote(self,num1,num2):
        if num2 == 0:
            return 1
        else:
            return num1 * self.calcularPote(num1, num2-1)
        
    def imprimir(self):
        print(self.calcularPote(self.num1, self.num2)) 

objPot = Potencial (2,3)
objPot.imprimir()