# Algoritmo para verificar si un número es primo usando recursividad

# 1. Definir la clase EsPrimo
# 2. Crear el constructor __init__ que reciba el número n y lo guarde en self.n
# 3. Definir el método calcular(n, divisor=2):
#    3.1. Si n <= 2, retornar True si n es 2, sino False (caso base)
#    3.2. Si n es divisible entre divisor, retornar False
#    3.3. Si divisor^2 > n, retornar True
#    3.4. Si no, llamar recursivamente a calcular(n, divisor+1)
# 4. Definir el método imprimir():
#    4.1. Llamar al método calcular usando self.n
#    4.2. Imprimir el resultado
# 5. Crear un objeto de la clase EsPrimo con el número deseado
# 6. Llamar al método imprimir() del objeto
# 7. Fin del algoritmo

"""
def es_primo(n, divisor=2):
    if n <= 2:
        return n == 2
    if n % divisor == 0:
        return False
    if divisor * divisor > n:
        return True
    return es_primo(n, divisor+1)

print(es_primo(13))  # True
"""
class EsPrimo:
    def __init__(self, n):
        self.n = n  

    def calcular(self, n, divisor=2):
        if n <= 2:  
            return n == 2
        if n % divisor == 0:  
            return False
        if divisor * divisor > n:  
            return True
        return self.calcular(n, divisor + 1)  

    def imprimir(self):
        print(self.calcular(self.n))  

objPrimo = EsPrimo(13)
objPrimo.imprimir()  