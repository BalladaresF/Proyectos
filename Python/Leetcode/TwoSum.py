# Objetivo: encontrar dos números enteros en el array nums tales que sumen el valor del target, que en este caso es 9.
nums = [2, 7, 11, 15]
target = 9

# método utilizado: Hash Map, o diccionario. 
def TwoSum(nums, target):
    num_map = {}                                #almacena los números que ya se han visto y sus índices.
    for i, num in enumerate(nums):              
        complement = target - num               #se resta el valor num al target.
        if complement in num_map:               
            return [num_map[complement], i]     #si el valor resultante existe en nums, es la respuesta correcta.
        num_map[num] = i

# TwoSum imprime la ubicación de los valores que suman a 9 en el arreglo, no los valores.
print (TwoSum(nums, target))