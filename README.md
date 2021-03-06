## EjerciciosOrdenar
Mi dirección de GitHub para este repositorio es la siguiente: [GitHub](https://github.com/alexlomu/EjerciciosOrdenar)
https://github.com/alexlomu/EjerciciosOrdenar

Para esta entrega hemos tenido que realizar 3 ejercicios:
# Ejercicio 4. Ordenación por inserción dicotómica
En este ejercicio nos piden que dada una lista con elementos comparables, ordenemos los mismos. He creado diferentes funciones dependiendo del tipo de elementos que queramos introducir en la lista. El diagrama de flujo propuesto es el siguiente:
![figma1](https://user-images.githubusercontent.com/91721507/158076314-9ebb113d-ccdd-4bb9-9c0f-db28abe83354.PNG)



El código propuesto es el siguiente:
```
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
  print("La lista introducida es: ", lista_numeros)
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
  lista_palabras.sort()
  print("La lista ordenada es: ", lista_palabras)  
  return lista_palabras



def pedir_lista_bool():
  lista_bool = []
  while True:
    entrada =input("Introduce un boolean (True o False) que se introducirá en la lista y dale al enter.")
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
    if lista_bool[i] == "True" and lista_bool[i] != lista_bool[i+1]:
      eliminar = lista_bool[i]
      lista_bool.pop(i)
      lista_bool.append(eliminar)
    else:
      i += 1
  print("La lista ordenada es: ", lista_bool)
  return lista_bool
  ```
# Ejercicio 5. Una ordenación topológica
En este ejercicio nos piden realizar un algoitmo que ordene unas tareas y sea capaz de determinar cuando dos de estas se pueden realizar a la vez o no.
El diagrama de flujo propuesto es el siguiente:




![figma2](https://user-images.githubusercontent.com/91721507/158076354-6c1b6661-bd63-48fd-8fb3-cbb3538fb50e.PNG)

El código propuesto es el siguiente:
```
#Una ordenación topológica
list = []
def llenar_lista(list):
    total = int(input("Escribe cuantas variables introducirás en la lista." ))
    i= 0
    for i in range(total-1):
        entrada =input("Introduce una palabra que se introducirá en la lista y dale al enter.")
        if entrada != "":
            list.append(entrada)
            i += 1
        else:
            print("Has introducido algo erroneo, por favor vuelve a introducir las variables desde el principio")
            llenar_lista(list)
    print("La lista introducida es {}".format(list))
    return list



def ordenar_lista(list):
    for i in range(len(list)-1):
        for j in range(len(list)-1):
            if list[j] > list[j+1]:
                print ("Intercambiando {} con {}...".format(list[j], list[j+1]))
                list[j], list[j+1] = list[j+1], list[j]
    print("La lista ordenada es {}".format(list))
    return list

llenar_lista(list)
ordenar_lista(list)
```
# Ejercicio 6. Completar las especificaciones
Para este ejercicio nos piden que dado un rango definido con un máximo y un mínimo se compruebe y ordene dentro de ese rango, los elementos de una lista. Además debemos hacer una copia de seguridad del máximo del segmento, desplazar los elementos una celda a la izquierda y colocar el elemento más grande del segmento en lo "alto". El diagrama del flujo propuesto es el siguiente:

![figma3](https://user-images.githubusercontent.com/91721507/158080123-2767c50f-6d7c-49aa-b9ac-6d72e1a374e1.PNG)


El código propuesto es el siguiente:
```
#Completar las especificaciones
maximo = int(input("Introduce el valor máximo."))
minimo = int(input("Introduce el valor mínimo."))
def rango():
    try:
        maximo > minimo
        return maximo, minimo
    except:
        print("El máximo debe ser superior al mínimo")
        maximo = int(input("Introduce el valor máximo."))
        minimo = int(input("Introduce el valor mínimo."))
        rango()
rango()

lista = []
def crear_lista():
    tamaño = int(input("Introduce el tamaño que tendrá la lista"))
    for i in range(tamaño-1):
        entrada = input("Introduce lo que quieras añadir a la lista y dale al enter.")
        lista.append(entrada)
    return lista
crear_lista()

def sacarmaximo(minimo, maximo):
    for i in range(minimo, maximo):
        max = lista[i] 
        if lista[i] > max:
            max = lista[i]
    return max
sacarmaximo(minimo, maximo)

def remplazar(minimo, maximo):
    for i in range(minimo, (maximo-1)):
        lista[i] = lista[i+1]
    return lista
remplazar(minimo, maximo)

def explorar(lista):
    m = lista[0]
    lista = lista[1:] + lista[:1]
    return lista
explorar(lista)
```
