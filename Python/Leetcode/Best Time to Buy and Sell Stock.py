# Maximizar ganancias encontrando el precio más bajo para comprar y el precio más alto para vender.
# Ejemplo: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6 - 1 = 5.

prices = [7,1,5,3,6,4]  #Este es el valor del producto en cada día. 

def maxProfit(prices):
    min_price = float('inf')  # Inicializar min_price a un valor muy alto
    max_profit = 0  # Se comienza con 0 ganancias

    for price in prices:
        # Actualizar min_price si encontramos un nuevo mínimo
        min_price = min(min_price, price)
        
        # Calcular la ganancia para el precio actual
        profit = price - min_price
        
        # Actualizar max_profit si el beneficio actual es mayor
        max_profit = max(max_profit, profit)

    return max_profit

print (maxProfit(prices))