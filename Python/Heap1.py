import heapq

data = [10, 20, 43, 1, 2, 65, 17, 44, 2, 3, 1]
heapq.heapify(data)
#el arreglo data pasa a ser el siguiente árbol binario:
#           1
#      1         17
#   2    2    65    43
# 44 10 3 20

print(data)

print(heapq.heappop(data))

print(data)

heapq.heappush(data, 4)
heapq.heappush(data, 19)
heapq.heappush(data, 21)

print(data, "\n")

H1 = [10, 20, 30, 40, 50]
H2 = [15, 25, 35, 45, 55]
H3 = heapq.merge(H1, H2)
print (list(H3))
