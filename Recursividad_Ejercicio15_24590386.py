# Algoritmo para calcular la suma de los dígitos de un número usando recursividad

# 1. Definir la clase SumaDigitos
# 2. Crear el constructor __init__ que reciba el número n y lo guarde en self.n
# 3. Definir el método calcular(n):
#    3.1. Si n es 0, retornar 0 (caso base)
#    3.2. Si no, retornar n % 10 + calcular(n // 10) (llamada recursiva)
# 4. Definir el método imprimir():
#    4.1. Llamar al método calcular usando self.n
#    4.2. Imprimir el resultado
# 5. Crear un objeto de la clase SumaDigitos con el número deseado
# 6. Llamar al método imprimir() del objeto
# 7. Fin del algoritmo

"""
def suma_digitos(n):
    if n == 0:
        return 0
    else:
        return n % 10 + suma_digitos(n // 10)

print(suma_digitos(1234))  # 10
"""
class SumaDigitos:
    def __init__(self, n):
        self.n = n  

    def calcular(self, n):
        if n == 0:  
            return 0
        else:
            return n % 10 + self.calcular(n // 10)  

    def imprimir(self):
        print(self.calcular(self.n))  

objSumaDigitos = SumaDigitos(1234)
objSumaDigitos.imprimir()  