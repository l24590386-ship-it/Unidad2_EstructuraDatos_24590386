# Algoritmo para verificar si una palabra es palíndromo usando recursividad

# 1. Definir la clase Palindromo
# 2. Crear el constructor __init__ que reciba la palabra y la guarde en self.palabra
# 3. Definir el método calcular(palabra):
#    3.1. Si la longitud de la palabra es menor o igual a 1, retornar True (caso base)
#    3.2. Si la primera letra es diferente de la última, retornar False
#    3.3. Si no, retornar calcular(resto de la palabra, sin primera y última letra)
# 4. Definir el método imprimir():
#    4.1. Llamar al método calcular usando self.palabra
#    4.2. Imprimir el resultado
# 5. Crear un objeto de la clase Palindromo con la palabra deseada
# 6. Llamar al método imprimir() del objeto
# 7. Fin del algoritmo

"""
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    elif palabra[0] != palabra[-1]:
        return False
    else:
        return es_palindromo(palabra[1:-1])

print(es_palindromo("anilina"))  # True
"""
class Palindromo:
    def __init__(self, palabra):
        self.palabra = palabra  

    def calcular(self, palabra):
        if len(palabra) <= 1: 
            return True
        elif palabra[0] != palabra[-1]:  
            return False
        else:
            return self.calcular(palabra[1:-1])  

    def imprimir(self):
        print(self.calcular(self.palabra)) 

objPal = Palindromo("anilina")
objPal.imprimir()  # Resultado: True