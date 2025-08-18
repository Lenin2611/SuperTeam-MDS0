from utils.terminal import limpiar
import backend.cliente as Cliente
from tabulate import tabulate

headers = ["Id", "Nombre", "Precio", "Cantidad"]

def solicitarProducto():
    id = input("Ingrese un ID: ")
    nombre = input(f"Ingrese el nombre del producto: ")
    precio = input (f"Ingrese el precio de su producto: ")
    cantidad = input (f"Ingrese la cantidad en stock de su producto: ")

    return (id, nombre, precio, cantidad)

def listarClientes():
    clientes =  Cliente.listarClientes()

    print(tabulate(clientes, headers=headers, tablefmt="rounded_grid"))

def consultarCliente():
    documento = input("Ingrese el ID del producto: ")

    cliente = Cliente.consultarCliente(documento)

    if cliente == None:
        print(f"Producto con ID {documento} no existe")
        return
    
    print(tabulate([cliente[1:]], headers=headers, tablefmt="rounded_grid"))

def agregarProducto():
    nuevo_producto = solicitarProducto()
    producto_creado = Cliente.crearProducto(*nuevo_producto)

    if producto_creado: 
        print("Producto agregado exitosamnete.")
    else:
        print("Error agregando el producto.")

def mostrarMenuDeClientes():
    separador = "--------------------------------------"
    bienvenida = "Bienvenido a UProducts powered by SuperTeam"
    opciones = {"1": listarClientes, "2": consultarCliente, "3": agregarProducto}
    solicitud = "Ingrese una opción: "
    salida = False

    while True: 
        menu = f"{bienvenida if salida == False else separador}\n1. Listar Productos\n2. Buscar Producto\n3. Agregar Producto\n4. Salir"
        print(menu)
        opcion = input(solicitud)
        salida = False

        if opcion == "4":
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