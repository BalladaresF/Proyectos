# Dado un array ordenado de enteros en orden ascendente y un número target, escribe una función para encontrar 
# el índice del target en el array. Si el target no se encuentra, devuelve -1.

nums1 = [-2, 0, 3, 5, 9, 12]
target1 = 9 #La solución debería ser 4, ya que nums[4] = 9.

nums2 = [-2, 0, 3, 5, 9, 12]
target2 = 2 #La solución debería ser -1, ya que 2 no está en el arreglo.

#Se realiza una búsqueda binaria porque el arreglo está ordenado.

def Buscar(nums, target):
    left, right = 0, len(nums) - 1  # Inicializar los punteros, uno al inicio y otro al final.
    
    while left <= right:            
        mid = left + (right - left) // 2  # Calcular el punto medio
        
        if nums[mid] == target:  # El valor medio es el objetivo. Si el valor existe, eventualmente será el punto medio.
            return mid
        
        elif nums[mid] < target:  # El objetivo está en la mitad derecha
            left = mid + 1
        
        else:  # El objetivo está en la mitad izquierda
            right = mid - 1
    
    return -1  # El objetivo no está en el array

print (Buscar(nums1, target1))
print (Buscar(nums2, target2))





