from utils.terminal import limpiar
import backend.producto as Producto
from tabulate import tabulate

headers = ["Id", "Nombre", "Precio", "Cantidad"]

def solicitarProducto():
    id = input("Ingrese un ID: ")
    nombre = input(f"Ingrese el nombre del producto: ")
    precio = input (f"Ingrese el precio de su producto: ")
    cantidad = input (f"Ingrese la cantidad en stock de su producto: ")

    return (id, nombre, precio, cantidad)

def listarProductos():
    productos =  Producto.listarProductos()

    print(tabulate(productos, headers=headers, tablefmt="rounded_grid"))

def consultarProducto():
    id = input("Ingrese el ID del producto: ")

    producto = Producto.consultarProducto(id)

    if producto == None:
        print(f"Producto con ID {id} no existe")
        return
    
    print(tabulate([producto[1:]], headers=headers, tablefmt="rounded_grid"))

def agregarProducto():
    nuevo_producto = solicitarProducto()
    producto_creado = Producto.crearProducto(*nuevo_producto)

    if producto_creado: 
        print("Producto agregado exitosamnete.")
    else:
        print("Error agregando el producto.")

def eliminarProducto():
    id = input("Ingrese el ID del producto: ")
    producto_eliminado = Producto.eliminarProducto(id)

    if producto_eliminado:
        print("Producto eliminado exitosamente.")
    else: 
        print("Error: verifique que el producto con ese ID si exista")

def actualizarProducto():
    nuevo_producto = solicitarProducto
    producto_actualizado = Producto.actualizarProducto(*nuevo_producto)

    if producto_actualizado:
        print("Producto actualizado exitosamente.")
    else:
        print("Error: verificar que el producto con ese ID si exista")

def mostrarMenuDeProductos():
    separador = "--------------------------------------"
    bienvenida = "Bienvenido a UProducts powered by SuperTeam"
    opciones = {"1": listarProductos, "2": consultarProducto, "3": agregarProducto, "4": eliminarProducto, "5": actualizarProducto}
    solicitud = "Ingrese una opción: "
    salida = False

    while True: 
        menu = f"{bienvenida if salida == False else separador}\n1. Listar Productos\n2. Buscar Producto\n3. Agregar Producto\n4. Eliminar Producto\n5. Actualizar Producto\n6. Salir"
        print(menu)
        opcion = input(solicitud)
        salida = False

        if opcion == "6":
            limpiar()
            break

        if opcion in opciones:
            salida = True 
            solicitud = "Ingrese una opción: "
            limpiar()
            opciones.get(opcion)()
        else: 
            solicitud = "Solicitud invalida, ingrese una nueva opción: "
            limpiar()