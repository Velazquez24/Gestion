print ('Gestor de productos'.center(60,'-'))
productos = []
precio = []
cantidad = []

def cargar_datos():
    try:
        with open('productos.txt', 'r') as file:
            for line in file:
                datos = line.strip().split(', ')
                productos.append(datos[0])
                cantidad.append(int(datos[1]))
                precio.append(float(datos[2]))
        print('Datos cargados correctamente')
    except FileNotFoundError:
        print('No se encontraron datos previos')

def guardar_datos():
       with open('productos.txt', 'w') as file:
              for i in range(len(productos)):
                    file.write(f"{productos[i]}, {cantidad[i]}, {precio[i]}\n")
print('Datos guardados correctamente')

cargar_datos()

while True:
    print("""
    (1) Añadir Producto
    (2) Ver Productos
    (3) Actualizar Producto
    (4) Eliminar Producto
    (5) Guardar datos
    (6) Ver Productos Guardados
    """)

    respuesta = int(input('Ingrese su opcion: '))
    if respuesta == 1:
            try:
                an = input('ingrese el nombre de su producto').strip().lower()
                ac = int(input('ingrese la cantidad de su producto'))
                ap = float(input('ingrese el precio de su producto'))

                cantidad.append(ac)
                productos.append(an)
                precio.append(ap)
            except ValueError:
                print('Ingrese un producto valido')
            
    elif respuesta == 2:
            buscador = input('ingrese el nombre del producto para buscar').strip().lower()
            try:
                posicion = productos.index(buscador)
                print('la cantidad del producto es: ', cantidad[posicion])
                print('el nombre del producto es: ', productos[posicion])
                print('el precio del producto es: ', precio[posicion])
            except ValueError:
                print('Producto no encontrado')
                
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
                print('Producto eliminado')
        except ValueError:
              print('Producto no encontrado')
    elif respuesta == 5:
        if not productos:
                print('No hay datos para guardar')
        else:
                guardar_datos()
                print('Datos guardados correctamente')

    elif respuesta == 6:
        if productos:
            print('Estos son los productos guardados')
            for i in range (len(productos)):
                print (f"{i+1}. Nombre: {productos[i]}, Cantidad: {cantidad[i]}, Precio: {precio[i]}")
        else:
            print ('No hay productos guardados')
            
    else:
        break
