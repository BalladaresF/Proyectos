List = [1, 2, 2, 3, 4, 4, 5, 6, 6]

def removeDuplicates(nums):
    if len(nums) == 0:
        return 0
    
    # Puntero lento
    i = 0
    
    # Puntero rápido comienza desde el segundo elemento
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:  # Si encontramos un número nuevo
            i += 1              # Mueve el puntero lento
            nums[i] = nums[j]    # Actualiza el array con el nuevo número único
    
    return i + 1  # La longitud del array con elementos únicos

# Este código imprime la cantidad de valores distintos del arreglo.
print (removeDuplicates(List))