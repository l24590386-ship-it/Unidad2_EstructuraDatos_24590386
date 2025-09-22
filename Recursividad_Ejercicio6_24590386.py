# Algoritmo para contar las vocales de una cadena usando recursividad

# 1. Definir la clase ContarVocales
# 2. Crear el constructor __init__ que reciba la cadena y la guarde en self.cadena
# 3. Definir el método calcular(cadena):
#    3.1. Si la cadena está vacía, retornar 0 (caso base)
#    3.2. Si no, verificar si el primer carácter es vocal
#         3.2.1. Si es vocal, retornar 1 + calcular(resto de la cadena)
#         3.2.2. Si no es vocal, retornar calcular(resto de la cadena)
# 4. Definir el método imprimir():
#    4.1. Llamar al método calcular usando self.cadena
#    4.2. Imprimir el resultado
# 5. Crear un objeto de la clase ContarVocales con la cadena deseada
# 6. Llamar al método imprimir() del objeto
# 7. Fin del algoritmo

"""
def contar_vocales(cadena):
    if cadena == "":
        return 0
    else:
        if cadena[0].lower() in 'aeiou':
            return 1 + contar_vocales(cadena[1:])
        else:
            return contar_vocales(cadena[1:])

print(contar_vocales("Recursividad"))  # 5
"""
class ContarVocales:
    def __init__(self, cadena):
        self.cadena = cadena  

    def calcular(self, cadena):
        if cadena == "":  
            return 0
        else:
            if cadena[0].lower() in 'aeiou':  
                return 1 + self.calcular(cadena[1:])  
            else:
                return self.calcular(cadena[1:])  

    def imprimir(self):
        print(self.calcular(self.cadena))  

objVocales = ContarVocales("Recursividad")
objVocales.imprimir()  
