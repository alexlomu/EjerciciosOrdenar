#Ordenación por inserción dicotómica
def pedir_lista_numeros():
  lista_numeros = []
  while True:
    entrada =input("Introduce un número que se introducirá en la lista y dale al enter.")
    if entrada is int:
      entrada = int(entrada)
      lista_numeros.append(entrada)
    elif entrada is not int:
      print("Introduce un número por favor.")
    elif entrada == "":
      break
  print("La lista introducida es: ", lista_bool)
  return lista_numeros
def  ordenar_lista_numeros(lista_numeros):
  lista_numeros.sort()
  print("La lista ordenada es: ", lista_numeros)  
  return lista_numeros
    

def pedir_lista_palabras(lista_palabras):
  lista_palabras = []
  while True:
    entrada = input("Introduce una palabra que se introducirá en la lista y dale al enter.")
    if entrada is int or bool:
      print("Introduce una palabra por favor.")
    elif entrada is not int or bool:
      lista_palabras.append(entrada)
    elif entrada == "":
      break
  print("La lista introducida es: ", lista_palabras)
  return lista_palabras
def ordenar_lista_palabras(lista_palabras):
  lista_palabras.sort
  print("La lista ordenada es: ", lista_palabras)  
  return lista_palabras



def pedir_lista_bool():
  lista_bool = []
  while True:
    entrada =input"Introduce un boolean (True o False) que se introducirá en la lista y dale al enter."
    if entrada is not bool:
      print("Introduce un boolean por favor.")
    elif entrada is bool:    
      lista_bool.append(entrada)
    elif entrada == "":
      break
  print("La lista introducida es: ", lista_bool)
  return lista_bool
def ordenar_lista_bool(lista_bool):
  i = 0
  elementos = len(lista_bool)
  for i in range((elementos-1)):
    if lista_bool[i] == "True" and lista_bool[i] != lista_bool[i+1:
    ]
      eliminar = lista_bool[i]
      lista_bool.pop(i)
      lista_bool.append(eliminar)
    else:
      i += 1
  print("La lista ordenada es: ", lista_bool)
  return lista_bool