#listas
valores=[1,2,3,4,5]

#tupla
valorestupla = (1,2,3,4,5)
print(valorestupla)

#for valor in valorestupla:
    #print(valor)
#print(valorestupla[0])    
#valorestupla.append(6)
#print(valorestupla)

#De tupla a lista
listaValores = list(valorestupla)
print(valorestupla)
listaValores.append(6)
print(listaValores)
valorestupla = tuple(listaValores)
print(valorestupla)