# Algoritmo para contar cuántas veces aparece un carácter en una cadena usando recursividad

# 1. Definir la clase ContarCaracter
# 2. Crear el constructor __init__ que reciba la cadena y el carácter a buscar, guardándolos en self.cadena y self.caracter
# 3. Definir el método calcular(cadena, caracter):
#    3.1. Si la cadena está vacía, retornar 0 (caso base)
#    3.2. Si el primer carácter de la cadena es igual al carácter buscado, retornar 1 + calcular(resto de la cadena)
#    3.3. Si no, retornar calcular(resto de la cadena)
# 4. Definir el método imprimir():
#    4.1. Llamar al método calcular usando self.cadena y self.caracter
#    4.2. Imprimir el resultado
# 5. Crear un objeto de la clase ContarCaracter con la cadena y el carácter deseado
# 6. Llamar al método imprimir() del objeto
# 7. Fin del algoritmo

"""
def contar_caracter(cadena, caracter):
    if cadena == "":
        return 0
    else:
        if cadena[0] == caracter:
            return 1 + contar_caracter(cadena[1:], caracter)
        else:
            return contar_caracter(cadena[1:], caracter)

print(contar_caracter("banana", "a"))  # 3
"""
class ContarCaracter:
    def __init__(self, cadena, caracter):
        self.cadena = cadena      
        self.caracter = caracter  

    def calcular(self, cadena, caracter):
        if cadena == "":  
            return 0
        else:
            if cadena[0] == caracter:  
                return 1 + self.calcular(cadena[1:], caracter)  
            else:
                return self.calcular(cadena[1:], caracter)  

    def imprimir(self):
        print(self.calcular(self.cadena, self.caracter))  

objContar = ContarCaracter("banana", "a")
objContar.imprimir()  # Resultado: 3