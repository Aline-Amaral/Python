from collections import deque

listaOriginal = ['A', '1', 'E', '5', 'T', '7', 'W', '8', 'G']
numeros = ["0","1","2","3","4","5","6","7","8","9"]
letras = []
digitos = []
result = []

for e in listaOriginal:
    if e in numeros:
        letras.append(e)
    else: 
        digitos.append(e)


result = letras.extend(digitos)

print(result)

fila = deque([5, 8])
fila.append(10) # [5, 8, 10]
fila.popleft()

fila.popright()

print(fila)
