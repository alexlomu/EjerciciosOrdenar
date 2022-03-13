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
