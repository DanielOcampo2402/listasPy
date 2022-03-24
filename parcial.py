productos = []
band = True

opcion = 1

print("Digite 1 para recibir (codigo, nombre, precio) de un producto : ")
print("2.Mostrar")
print("3.Editar")


while(opcion != 0):
    opcion = int(input("Digite la opcion que desea elegir :"))
    if(opcion == 1):
        producto={}
        producto['codigo'] = input("Digite el codigo del producto :")
        producto['nombre'] = input("Digite el nombre del producto :")
        producto['precio'] = int(input("Digite el precio del producto :"))
        productos.append(producto)
    elif(opcion == 2):
        print("")  
        print(productos)
    elif(opcion == 3):
        cod = input("Digite el codigo del producto :")
        for producto in productos:
            if(producto['codigo'] == cod ):
                nuevoPrecio = input("Digite el nuevo precio del producto :")
                producto['precio'] == nuevoPrecio
                band = True
                break
            else:
                band = False
        if(band == False):
            print("Producto no encontrado")           
    elif(opcion == 4):
            cod = input("Digite el codigo del producto :")
            for producto in productos:
                if(producto['codigo'] == cod ):
                    productos.remove(producto)
                    print("Se elimino el producto")
                    band = True
                    break
                else:
                    band = False
            if(band == False):
                print("No se elimino el producto")           



    else:
        print("")
          
