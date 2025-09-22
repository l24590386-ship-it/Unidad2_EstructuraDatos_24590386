# Algoritmo para generar todas las permutaciones de una lista usando recursividad

# 1. Definir la clase Permutaciones
# 2. Crear el constructor __init__ que reciba la lista y la guarde en self.lista
# 3. Definir el método calcular(lista, inicio=0):
#    3.1. Si inicio == len(lista) - 1, imprimir la lista (caso base)
#    3.2. Si no, para cada índice i desde inicio hasta el final de la lista:
#         3.2.1. Intercambiar lista[inicio] con lista[i]
#         3.2.2. Llamar recursivamente a calcular(lista, inicio+1)
#         3.2.3. Deshacer el intercambio (backtracking)
# 4. Definir el método imprimir():
#    4.1. Llamar al método calcular usando self.lista
# 5. Crear un objeto de la clase Permutaciones con la lista deseada
# 6. Llamar al método imprimir() del objeto
# 7. Fin del algoritmo
"""
def permutaciones(lista, inicio=0):
    if inicio == len(lista) - 1:
        print(lista)
    else:
        for i in range(inicio, len(lista)):
            lista[inicio], lista[i] = lista[i], lista[inicio]
            permutaciones(lista, inicio + 1)
            lista[inicio], lista[i] = lista[i], lista[inicio]

permutaciones([1, 2, 3])
"""
class Permutaciones:
    def __init__(self, lista):
        self.lista = lista  

    def calcular(self, lista, inicio=0):
        if inicio == len(lista) - 1:  
            print(lista)  
        else:
            for i in range(inicio, len(lista)):
                lista[inicio], lista[i] = lista[i], lista[inicio]  
                self.calcular(lista, inicio + 1)  
                lista[inicio], lista[i] = lista[i], lista[inicio]  
    def imprimir(self):
        self.calcular(self.lista) 

objPermutaciones = Permutaciones([1, 2, 3])
objPermutaciones.imprimir()