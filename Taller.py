def operaciones():
  print(f'Hallar raiz cuadrada de un numero ingresado por el usuario \n Elija una opcion: \n 1. Enumeracion Exhaustiva. \n 2. Aproximacion de soluciones. \n 3. Busqueda binaria.')
  opcion = int(input('Elija una opcion valida: '))
  numero = int(input('Ingrese un numero: ')) 

#=====Opcion====================================
  if(opcion == 1):
    Enumeracion(numero)
  elif(opcion == 2):
    Aproximacion(numero)
  elif(opcion == 3):
    BusquedaBinaria(numero)
  else:
    print(f'Opcion invalida, ingrese una opcion valida. !')

#==============Enumeracion=======================
def Enumeracion(objetivo):
  respuesta = 0

  while respuesta**2 < objetivo:
    respuesta += 1

  if respuesta**2 == objetivo:
    print(f'La raiz cuadrada de {objetivo} es {respuesta}')

  else: 
    print(f'{objetivo} no tiene raiz cuadrada exacta')

#===============Aproximacion======================
def Aproximacion(objetivo):
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

#=========Busqueda Binaria========================

def BusquedaBinaria(objetivo):
  epsilon = 0.001
  bajo = 0.0
  alto = max(1.0, objetivo)
  respuesta = (alto + bajo) / 2

  while abs(respuesta**2 - objetivo) >= epsilon:
      print(f'bajo={bajo}, alto={alto}, respuesta={respuesta}')
      if respuesta**2 < objetivo:
          bajo = respuesta
      else:
          alto = respuesta
      respuesta = (alto + bajo) / 2
  print(f'La raiz cuadrada de {objetivo} es {respuesta}')

operaciones()
