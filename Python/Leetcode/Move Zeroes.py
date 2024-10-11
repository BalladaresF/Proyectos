#Se busca mover todos los ceros a la derecha del arreglo.

nums = [0,1,0,3,12]

def moveZeroes(nums):
    last_non_zero = 0  # Mantiene la posición del último número no cero encontrado

    # Iteramos sobre el array
    for i in range(len(nums)):
        if nums[i] != 0:  # Si el elemento actual no es cero
            # Intercambiar el elemento actual con el elemento en last_non_zero
            nums[last_non_zero], nums[i] = nums[i], nums[last_non_zero] #Se asigna el valor de la izquierda a la derecha y viceversa.
            last_non_zero += 1  # Mover el puntero de last_non_zero a la siguiente posición

print(nums)
moveZeroes(nums)
print(nums)