root = [3, 9, 20, 5, 6, 15, 7]

# Primer paso: Definir nodos del árbol binario:
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(self, root: TreeNode) -> int:
    # Si no hay raíz, la profundidad es 0.
    if not root:
        return 0
        
    # Calcular recursivamente la profundidad del subárbol izquierdo y derecho.
    left_depth = self.maxDepth(root.left)
    right_depth = self.maxDepth(root.right)

    #La profundidad del nodo actual es 1 + la profundidad máxima de sus subárboles.
    return 1 + max(left_depth, right_depth)

