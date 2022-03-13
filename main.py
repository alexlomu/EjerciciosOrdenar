import sys



if __name__ == "__main__":
  while True:
    ejercicio = int(input("Introduce el número del ejercicio al que quieres acceder al código (4, 5 o 6): "))
    if ejercicio == 4:
      from Classes import Ejercicio4      
    elif ejercicio == 5:
      from Classes import Ejercicio5
    elif ejercicio == 6:
      from Classes import Ejercicio6
    else:
      break
      
    
    