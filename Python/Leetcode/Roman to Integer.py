# I = 1, V = 5, X = 10, L = 50
#C = 100, D = 500, M = 1000

A = "IV"        # 4
B = "MCMXCIV"   # 1994
C = "CCCXXXIII" # 333

def romanToInt(s: str) -> int:
    # Diccionario con los valores romanos:
    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }
    
    total = 0
    prev_value = 0
    
    # Iterar el número romano de izquierda a derecha:
    for char in s:
        curr_value = roman_values[char]
        
        # Si el valor actual es mayor que el anterior, restar dos veces el valor anterior
        # Como se ha realizado en la iteración anterior.
        if curr_value > prev_value:
            total += curr_value - 2 * prev_value
        else:
            total += curr_value
        
        # Actualizar el valor:
        prev_value = curr_value
    
    return total

print (romanToInt(A))
print (romanToInt(B))
print (romanToInt(C))

