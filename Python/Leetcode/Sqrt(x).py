#Conseguir la raíz cuadrada del input sin utilizar librerías o métodos predeterminados. 

Input1 = 8
#Output = 2 (Respuesta exacta: 2.82842)

Input2 = 9
#Output = 3

#Método 1: Búsqueda binaria
def Sqrt(x: int) -> int:
    if x == 0:
        return 0
    
    left, right = 1, x
    
    while left <= right:
        mid = (left + right) // 2
        if mid * mid == x:
            return mid
        elif mid * mid < x:
            left = mid + 1
        else:
            right = mid - 1
    
    return right  # No se retornan decimales, solo el número entero.


#Método 2: Método de Newton (iterativo)
def OtherSqrt(x: int) -> int:
    if x == 0:
        return 0
    
    guess = x
    while guess * guess > x:
        guess = (guess + x // guess) // 2
    
    return guess

print (Sqrt(Input1))
print (OtherSqrt(Input2))
