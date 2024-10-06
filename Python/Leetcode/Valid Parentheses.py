#Determinar si el string dado es válido, lo cual ocurre si:
#   1: Todos los paréntesis de apertura tienen paréntesis de cierre correspondiente.
#   2: Los paréntesis están correctamente anidados.

A = "()"
B = "()[]{}"
C = "(]"
D = "([)]"

def EsValido(Text: str) -> bool:
    stack = []
    # Mapea los paréntesis de cierre a su correspondiente apertura
    Pares = {')': '(', '}': '{', ']': '['}
    
    for char in Text:
        if char in Pares:
            # Tomamos el tope de la pila o un valor por defecto si la pila está vacía
            top_element = stack.pop() if stack else '#'
            
            # Si el paréntesis de cierre no corresponde, no es válido
            if Pares[char] != top_element:
                return False
        else:
            # Si es un paréntesis de apertura, lo añadimos a la pila
            stack.append(char)
    
    # Si la pila está vacía, significa que todos los paréntesis se emparejaron correctamente
    return not stack

print (EsValido(A))
print (EsValido(B))
print (EsValido(C))
print (EsValido(D))