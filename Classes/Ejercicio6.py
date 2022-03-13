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