# Algoritmo para generar todas las combinaciones de los caracteres de una cadena usando recursividad

# 1. Definir la clase Combinaciones
# 2. Crear el constructor __init__ que reciba la cadena y la guarde en self.cadena
# 3. Definir el método calcular(cadena, actual=""):
#    3.1. Si la cadena está vacía, imprimir la combinación actual (caso base)
#    3.2. Si no, llamar recursivamente a calcular:
#         3.2.1. Incluyendo el primer carácter de la cadena en 'actual'
#         3.2.2. Excluyendo el primer carácter de la cadena
# 4. Definir el método imprimir():
#    4.1. Llamar al método calcular usando self.cadena
# 5. Crear un objeto de la clase Combinaciones con la cadena deseada
# 6. Llamar al método imprimir() del objeto
# 7. Fin del algoritmo

"""
def combinaciones(cadena, actual=""):
    if cadena == "":
        print(actual)
    else:
        combinaciones(cadena[1:], actual + cadena[0])
        combinaciones(cadena[1:], actual)

combinaciones("ab")
"""
class Combinaciones:
    def __init__(self, cadena):
        self.cadena = cadena  

    def calcular(self, cadena, actual=""):
        if cadena == "":  
            print(actual)  
        else:
            self.calcular(cadena[1:], actual + cadena[0])
            self.calcular(cadena[1:], actual)

    def imprimir(self):
        self.calcular(self.cadena)  

objComb = Combinaciones("ab")
objComb.imprimir() 