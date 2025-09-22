# Algoritmo para convertir un número decimal a binario usando recursividad

# 1. Definir la clase DecimalABinario
# 2. Crear el constructor __init__ que reciba el número decimal n y lo guarde en self.n
# 3. Definir el método calcular(n):
#    3.1. Si n es 0, retornar cadena vacía '' (caso base)
#    3.2. Si no, retornar calcular(n // 2) + str(n % 2) (llamada recursiva y concatenación del residuo)
# 4. Definir el método imprimir():
#    4.1. Llamar al método calcular usando self.n
#    4.2. Imprimir el resultado
# 5. Crear un objeto de la clase DecimalABinario con el número deseado
# 6. Llamar al método imprimir() del objeto
# 7. Fin del algoritmo
"""
def decimal_a_binario(n):
    if n == 0:
        return ''
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

print(decimal_a_binario(10))  # "1010"
"""
class DecimalABinario:
    def __init__(self, n):
        self.n = n 

    def calcular(self, n):
        if n == 0:  
            return ''
        else:
            return self.calcular(n // 2) + str(n % 2)  
    def imprimir(self):
        print(self.calcular(self.n))

objBinario = DecimalABinario(10)
objBinario.imprimir()  