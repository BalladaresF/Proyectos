# Dado un array de números enteros nums, encuentre todas las combinaciones de tres números cuya suma sea igual a cero.

nums = [-1, 0, 1, 2, -1, -4]
# Output: [[-1, -1, 2], [-1, 0, 1]]

def threeSum(nums):
    # Ordenar el array
    nums.sort()
    res = []
    
    # Iterar sobre cada número en el array
    for i in range(len(nums) - 2):
        # Saltar los números duplicados para el primer elemento
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        # Usar dos punteros: uno en el siguiente número y otro en el final
        left, right = i + 1, len(nums) - 1
        
        # Mientras los punteros no se crucen
        while left < right:
            total_sum = nums[i] + nums[left] + nums[right]
            
            # Si la suma es cero, agregamos la combinación a la lista de resultados
            if total_sum == 0:
                res.append([nums[i], nums[left], nums[right]])
                
                # Mover los punteros y evitar duplicados
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                
                # Mover ambos punteros después de encontrar una combinación válida
                left += 1
                right -= 1
            
            # Si la suma es menor que cero, incrementamos el puntero izquierdo
            elif total_sum < 0:
                left += 1
            
            # Si la suma es mayor que cero, decrementamos el puntero derecho
            else:
                right -= 1
    
    # Retornar la lista con todas las combinaciones válidas
    return res

print(nums)
print(threeSum(nums))