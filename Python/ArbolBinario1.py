# Crear clase nodo:
class Node:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

# Función para insertar en el árbol binario:
    def insert(self, data):
        # Si el valor es menor al nodo padre:
        if data < self.data:
            if self.leftChild:
                # Si todavía se necesita mover al subárbol de la izquierda:
                self.leftChild.insert(data)
            else:
                self.leftChild = Node(data)
                return
        # Si el valor es mayor al nodo padre:    
        else:
            if self.rightChild:
                # Si todavía se necesita mover al subárbol de la derecha:
                self.rightChild.insert(data)
            else:
                self.rightChild = Node(data)
                return

# Función para buscar en el árbol binario:
    def search(self, val):
        # Si se encontró el valor:
        if val==self.data:
            return str(val)+" ha sido encontrado"
        # Si el valor es menor al nodo padre:
        elif val < self.data:
            # Si todavía se necesita mover al subárbol de la izquierda:
            if self.leftChild:
                return self.leftChild.search(val)
            else:
                return str(val)+" no ha sido encontrado"
        # Si el valor es mayor al nodo padre:    
        else:
            # Si todavía se necesita mover al subárbol de la derecha:
            if self.rightChild:
                return self.rightChild.search(val)
            else:
                return str(val)+" no ha sido encontrado" 

    # Función para imprimir árbol:
    def PrintTree(self):
        if self.leftChild:
            self.leftChild.PrintTree()
        print( self.data),
        if self.rightChild:
            self.rightChild.PrintTree()

# Crear nodo raíz:
root = Node(27)
# Insertar valores al árbol:
root.insert(14)
root.insert(35)
root.insert(31)
root.insert(10)
root.insert(19)
# Imprimir árbol binario:
root.PrintTree()
print("\n"+root.search(7))
print(root.search(14)+"\n")