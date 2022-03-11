#Ordenación por inserción dicotómica
lista_numeros = []
def pedir_lista_numeros(lista_numeros):
  while True:
    entrada = input("Introduce un número que se introducirá en la lista y dale al enter, para cerrar la lista dale al enter sin introducir nada.")
    try: 
      entrada = int(entrada) 
      lista_numeros.append(entrada)
    except:
      print("La lista introducida es: ", lista_numeros)
      break
  return lista_numeros
def ordenar_lista_numeros(lista_numeros):
  lista_numeros.sort()
  print("La lista ordenada es: ", lista_numeros)  
  return lista_numeros


lista_palabras = []
def pedir_lista_palabras(lista_palabras):
  while True:
    entrada = input("Introduce una palabra que se introducirá en la lista y dale al enter.")
    try: 
      entrada != int(entrada) 
      lista_palabras.append(entrada)
    except:
      print("La lista introducida es: ", lista_palabras)
      break
  return lista_palabras

def ordenar_lista_palabras(lista_palabras):
  lista_palabras.sort()
  print("La lista ordenada es: ", lista_palabras)  
  return lista_palabras

def pedir_lista_bool():
  lista_bool = []
  while True:
    entrada =input("Introduce un boolean (True o False) que se introducirá en la lista y dale al enter.")
    if entrada == "True" or "False":  
      lista_bool.append(entrada)
    else:
      break
  
  print("La lista introducida es: ", lista_bool)
  return lista_bool
def ordenar_lista_bool(lista_bool):
  i = 0
  elementos = len(lista_bool)
  for i in range((elementos-1)):
    if lista_bool[i] == "True" and lista_bool[i] != lista_bool[i+1]:
      eliminar = lista_bool[i]
      lista_bool.pop(i)
      lista_bool.append(eliminar)
    else:
      i += 1
  print("La lista ordenada es: ", lista_bool)
  return lista_bool


tipo_lista = int(input("Introduce si la lista a ordenar es de números(1), palabras(2), booleans(3): "))
if tipo_lista == 1:
  lista_numeros = []
  pedir_lista_numeros(lista_numeros)
  ordenar_lista_numeros(lista_numeros)
elif tipo_lista == 2:
  lista_palabras = []
  pedir_lista_palabras()
  ordenar_lista_palabras(lista_palabras)
elif tipo_lista == 3:
  lista_bool = []
  pedir_lista_bool()
  ordenar_lista_bool(lista_bool)

