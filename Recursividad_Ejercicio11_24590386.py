# Algoritmo para buscar un elemento en una lista usando recursividad

# 1. Definir la clase BuscarElemento
# 2. Crear el constructor __init__ que reciba la lista y el elemento a buscar, guardándolos en self.lista y self.elemento
# 3. Definir el método calcular(lista, elemento):
#    3.1. Si la lista está vacía, retornar False (caso base)
#    3.2. Si el primer elemento de la lista es igual al elemento buscado, retornar True
#    3.3. Si no, llamar recursivamente a calcular con el resto de la lista
# 4. Definir el método imprimir():
#    4.1. Llamar al método calcular usando self.lista y self.elemento
#    4.2. Imprimir el resultado
# 5. Crear un objeto de la clase BuscarElemento con la lista y el elemento deseado
# 6. Llamar al método imprimir() del objeto
# 7. Fin del algoritmo

"""
def buscar_elemento(lista, elemento):
    if not lista:
        return False
    elif lista[0] == elemento:
        return True
    else:
        return buscar_elemento(lista[1:], elemento)

print(buscar_elemento([1, 3, 5, 7], 5))  # True
"""
class BuscarElemento:
    def __init__(self, lista, elemento):
        self.lista = lista      
        self.elemento = elemento  
    def calcular(self, lista, elemento):
        if not lista:  
            return False
        elif lista[0] == elemento:  
            return True
        else:
            return self.calcular(lista[1:], elemento)  
    def imprimir(self):
        print(self.calcular(self.lista, self.elemento))  

objBuscar = BuscarElemento([1, 3, 5, 7], 5)
objBuscar.imprimir()  # Resultado: True