nombres = ["alejandro", "estiben", "david"]
numeros =[3,4,5,6,7,8]

print(nombres[1])
print(nombres[-1])
print(nombres[1:])

#funciones

#extend esto lo que hace es agregar elementos a una lista de
nombres.extend(numeros)
print(nombres)

#append funciona para poser agregar un elemnto a la lista 

nombres.append("juan")
print(nombres)

#clear funciona parap poder limpiar toda la lista 
#pop funciona para sacar un elemeto de la lista

nombres2 = nombres

print(nombres2)