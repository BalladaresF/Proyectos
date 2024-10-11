l1 = [1,2,4]
l2 = [1,3,4]

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_linked_list(arr):
    # Si la lista está vacía, devolvemos None
    if not arr:
        return None

    # Creamos el nodo inicial
    head = ListNode(arr[0])
    current = head

    # Recorremos los elementos restantes y los añadimos como nodos
    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next

    return head

def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    # Nodo sentinela (dummy) para simplificar el manejo del puntero
    dummy = ListNode()
    current = dummy

    # Mientras ambas listas no estén vacías
    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    # Si una de las listas todavía tiene nodos, los agregamos a la lista fusionada
    if l1:
        current.next = l1
    if l2:
        current.next = l2

    # Retornamos la lista fusionada a partir del siguiente nodo del dummy
    return dummy.next

def print_linked_list(head: ListNode):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

# Convertimos las listas de Python en listas enlazadas
l1 = create_linked_list([1, 2, 4])
l2 = create_linked_list([1, 3, 4])

# Llamamos a la función mergeTwoLists
merged_list = mergeTwoLists(l1, l2)

# Imprimimos el resultado
print_linked_list(merged_list)