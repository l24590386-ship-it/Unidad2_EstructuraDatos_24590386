# Algoritmo para invertir una cadena usando recursividad

# 1. Definir la clase InvertirCadena
# 2. Crear el constructor __init__ que reciba la cadena y la guarde en self.cadena
# 3. Definir el método calcular(cadena):
#    3.1. Si la longitud de la cadena es 0, retornar la cadena (caso base)
#    3.2. Si no, retornar el último carácter + calcular(resto de la cadena sin el último carácter)
# 4. Definir el método imprimir():
#    4.1. Llamar al método calcular usando self.cadena
#    4.2. Imprimir el resultado
# 5. Crear un objeto de la clase InvertirCadena con la cadena deseada
# 6. Llamar al método imprimir() del objeto
# 7. Fin del algoritmo

"""
def invertir_cadena(cadena):
    if len(cadena) == 0:
        return cadena
    else:
        return cadena[-1] + invertir_cadena(cadena[:-1])

print(invertir_cadena("hola"))  # "aloh"
"""
class InvertirCadena:
    def __init__(self, cadena):
        self.cadena = cadena  

    def calcular(self, cadena):
        if len(cadena) == 0:  
            return cadena
        else:
            return cadena[-1] + self.calcular(cadena[:-1])  

    def imprimir(self):
        print(self.calcular(self.cadena))  

objInvertir = InvertirCadena("hola")
objInvertir.imprimir()  