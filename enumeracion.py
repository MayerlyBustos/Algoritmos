objetivo = int(input('Ingresa un numero: '))
respuesta = 0

while respuesta**2 < objetivo:
  respuesta += 1

if respuesta**2 == objetivo:
  print(f'La raiz cuadrada de {objetivo} es {respuesta}')

else: 
  print(f'{objetivo} no tiene raiz cuadrada exacta')