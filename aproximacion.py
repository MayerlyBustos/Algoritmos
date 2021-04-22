objetivo = int(input('Ingresa un numero: '))
epsilon = 0.01
paso = epsilon**2
respuesta = 0.0

while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
  print(abs(respuesta**2 - objetivo))
  respuesta += paso

if abs(respuesta**2 - objetivo) >= epsilon:  
  print(f'No se encontro raiz cuadrada {objetivo}')
else:
  print(f'La raiz cuadrada de {objetivo} es {respuesta}')