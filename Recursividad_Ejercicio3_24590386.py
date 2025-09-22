# Algoritmo para contar la cantidad de dígitos de un número usando recursividad

# 1. Definir la clase Contar_digitos
# 2. Crear el constructor __init__ que reciba n y lo guarde en self.n
# 3. Definir el método calcular(num):
#    3.1. Si num < 10, retornar 1 (caso base: un solo dígito)
#    3.2. Si no, retornar 1 + calcular(num // 10) (llamada recursiva dividiendo entre 10)
# 4. Definir el método imprimir():
#    4.1. Llamar al método calcular usando self.n
#    4.2. Imprimir el resultado
# 5. Crear un objeto de la clase Contar_digitos con el número deseado (ej. 12345)
# 6. Llamar al método imprimir() del objeto
# 7. Fin del algoritmo

"""
def contar_digitos(n):
    if n < 10:
        return 1
    else:
        return 1 + contar_digitos(n // 10)

print(contar_digitos(12345))  # 5
"""

class Contar_digitos:
    def __init__(self,n):
        self.n = n
    
    def calcular(self,num):
        if num < 10:
            return 1
        else:
            return 1 + self.calcular(num // 10)
        
    def imprimir(self):
        print(self.calcular(self.n))

objcon = Contar_digitos (12345)
objcon.imprimir()
