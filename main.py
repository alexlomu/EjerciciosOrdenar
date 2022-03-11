import sys
import __init__


if __name__ == "__main__":
  while True:
    ejercicio = int(input("Introduce el número del ejercicio al que quieres acceder al código (4, 5 o 6)"))
    if ejercicio == 4:
      tipo_lista = int(input("Introduce si la lista a ordenar es de números(1), palabras(2), booleans(3)"))
      if tipo_lista == 1:
        pedir_lista_numeros()
        ordenar_lista_numeros(lista_numeros)
        break
      elif tipo_lista == 2:
        pedir_lista_palabras()
        ordenar_lista_palabras(lista_palabras)
        break
      elif tipo_lista == 3:
        pedir_lista_bool()
        ordenar_lista_bool(lista_bool)
        break
      else:
        print("Introduce 1, 2 o 3.")
    
    