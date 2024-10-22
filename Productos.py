print ('Gestor de productos'.center(60,'-'))
productos = []
precio = []
cantidad = []

def guardar_datos():
       with open('productos.txt', 'w') as file:
              for i in range(len(productos)):
                    file.write(f"{productos[i]}, {cantidad[i]}, {precio[i]}\n")
print('Datos guardados correctamente')

while True:
    print("""
    (1) Añadir Producto
    (2) Ver Productos
    (3) Actualizar Producto
    (4) Eliminar Producto
    (5) Guardar datos
    """)

    respuesta = int(input('Ingrese su opcion: '))
    if respuesta == 1:
            an = input('ingrese el nombre de su producto').strip().lower()
            ac = int(input('ingrese la cantidad de su producto'))
            ap = float(input('ingrese el precio de su producto'))

            cantidad.append(ac)
            productos.append(an)
            precio.append(ap)
            
    elif respuesta == 2:
            buscador = input('ingrese el nombre del producto para buscar').strip().lower()
            posicion = productos.index(buscador)
            print('la cantidad del producto es: ', cantidad[posicion])
            print('el nombre del producto es: ', productos[posicion])
            print('el precio del producto es: ', precio[posicion])

    elif respuesta == 3:
        buscador = input('Ingrese el producto que desea modificar: ').strip().lower()
        try:
            posicion = productos.index(buscador)
            an = input('Ingrese el nuevo nombre de su producto: ').strip().lower()
            ac = int(input('Ingrese la nueva cantidad de su producto: '))
            ap = float(input('Ingrese el nuevo precio de su producto: '))
            cantidad[posicion] = ac
            productos[posicion] = an
            precio[posicion] = ap
        except ValueError:
            print('producto no encontrado')    
                
    elif respuesta == 4:
        buscador = input('Ingrese el nombre del producto que quiera eliminar: ').strip().lower()
        try:
                posicion = productos.index(buscador)
                del productos[posicion]
                del cantidad[posicion]
                del precio[posicion]
        except ValueError:
              print('producto no encontrado')
    elif respuesta == 5:
           guardar_datos()
           print ('Datos Guardados correctamente')
    else:
        break
    
