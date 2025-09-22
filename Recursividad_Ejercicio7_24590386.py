# Algoritmo para calcular la suma de los elementos de una lista usando recursividad

# 1. Definir la clase SumaLista
# 2. Crear el constructor __init__ que reciba la lista y la guarde en self.lista
# 3. Definir el método calcular(lista):
#    3.1. Si la lista está vacía, retornar 0 (caso base)
#    3.2. Si no, retornar lista[0] + calcular(resto de la lista)
# 4. Definir el método imprimir():
#    4.1. Llamar al método calcular usando self.lista
#    4.2. Imprimir el resultado
# 5. Crear un objeto de la clase SumaLista con la lista deseada
# 6. Llamar al método imprimir() del objeto
# 7. Fin del algoritmo

"""
def suma_lista(lista):
    if not lista:
        return 0
    else:
        return lista[0] + suma_lista(lista[1:])

print(suma_lista([1, 2, 3, 4, 5]))  # 15
"""
class SumaLista:
    def __init__(self, lista):
        self.lista = lista  

    def calcular(self, lista):
        if not lista:  
            return 0
        else:
            return lista[0] + self.calcular(lista[1:])  
    def imprimir(self):
        print(self.calcular(self.lista))  

objSuma = SumaLista([1, 2, 3, 4, 5])
objSuma.imprimir()  