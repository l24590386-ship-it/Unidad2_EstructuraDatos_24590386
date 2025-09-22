# Algoritmo para resolver las Torres de Hanoi usando recursividad

# 1. Definir la clase TorresHanoi
# 2. Crear el constructor __init__ que reciba:
#    - n: número de discos
#    - origen: torre de origen
#    - destino: torre de destino
#    - auxiliar: torre auxiliar
#    Guardar estos valores en self.n, self.origen, self.destino y self.auxiliar
# 3. Definir el método calcular(n, origen, destino, auxiliar):
#    3.1. Si n es 1, imprimir "Mover disco de origen a destino" (caso base)
#    3.2. Si no:
#         3.2.1. Llamar recursivamente a calcular(n-1, origen, auxiliar, destino)
#         3.2.2. Llamar recursivamente a calcular(1, origen, destino, auxiliar)
#         3.2.3. Llamar recursivamente a calcular(n-1, auxiliar, destino, origen)
# 4. Definir el método imprimir():
#    4.1. Llamar al método calcular usando self.n, self.origen, self.destino, self.auxiliar
# 5. Crear un objeto de la clase TorresHanoi con los discos y torres deseadas
# 6. Llamar al método imprimir() del objeto
# 7. Fin del algoritmo

"""
def hanoi(n, origen, destino, auxiliar):
    if n == 1:
        print(f"Mover disco de {origen} a {destino}")
    else:
        hanoi(n-1, origen, auxiliar, destino)
        hanoi(1, origen, destino, auxiliar)
        hanoi(n-1, auxiliar, destino, origen)

hanoi(3, "A", "C", "B")
"""
class TorresHanoi:
    def __init__(self, n, origen, destino, auxiliar):
        self.n = n            
        self.origen = origen  
        self.destino = destino  
        self.auxiliar = auxiliar  
    def calcular(self, n, origen, destino, auxiliar):
        if n == 1:  
            print(f"Mover disco de {origen} a {destino}")
        else:
            self.calcular(n-1, origen, auxiliar, destino)
            self.calcular(1, origen, destino, auxiliar)
            self.calcular(n-1, auxiliar, destino, origen)

    def imprimir(self):
        self.calcular(self.n, self.origen, self.destino, self.auxiliar)  

objHanoi = TorresHanoi(3, "A", "C", "B")
objHanoi.imprimir()