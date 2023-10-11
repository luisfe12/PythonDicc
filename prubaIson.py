"""
Se usa el -1 como valor de ingreso cuando el usuario ingresa
alguna clave del diccionario que no existe
"""

# Esta funcion sirve tanto para agregar y actualizar valores


def newDiccionarioValues(Productos, Precios, Stock, clave):
    # Los condiconales son para controla en caso ingrese un valor nulo o vacio
    if (clave in Productos):
        print("entro en actualizar ", Productos[clave])
        producto = input(
            "Ingrese el nuevo nombre del producto: " or Productos[clave])
        precio = float(
            input("Ingrese el nuevo precio del producto: ") or Precios[clave])
        stock = int(input("Ingrese la nueva cantidad en stock: ")
                    or Stock[clave])

        if not producto:
            producto = Productos[clave]

    else:
        # print("no es actualizar",  Productos[clave])
        producto = input("Ingrese el nuevo nombre del producto: " or "vacio")
        precio = float(input("Ingrese el nuevo precio del producto: ") or 0.0)
        stock = int(input("Ingrese la nueva cantidad en stock: ") or 0.0)

        if not producto:
            producto = "vacio"

    Productos[clave] = producto
    Precios[clave] = precio
    Stock[clave] = stock


def deleteValues(Productos, Precios, Stock,):
    clave = int(
        input("Ingrese el número de producto que desea eliminar: ") or -1)
    if clave in Productos:
        del Productos[clave]
        del Precios[clave]
        del Stock[clave]
        print("El producto fue eliminado con éxito.")
    else:
        print("Ese producto no se encontro.")


def main():
    # Datos Iniciales que me dieron en el ejemplo
    Productos = {1: 'Pantalones', 2: 'Camisas', 3: 'Corbatas', 4: 'Casacas'}
    Precios = {1: 200.00, 2: 120.00, 3: 50.00, 4: 350.00}
    Stock = {1: 50, 2: 45, 3: 30, 4: 15}

    # Un while true para que siempre este en ejcucion
    while True:

        print("========================================")
        print("Lista de Productos:")
        print("========================================")
        # Se recorre los productos actuales que tenemos
        for clave, producto in Productos.items():
            print(str(clave).ljust(4), producto.ljust(20), str(
                Precios[clave]).ljust(10), str(Stock[clave]).ljust(5))

        print("========================================")
        print("[1] Agregar, [2] Eliminar, [3] Actualizar, [4] Salir")
        opcion = input("Elija opción: ")

        if opcion == "1":
            # Agregar valores
            clave = int(input("Ingrese el número de producto: ") or -1)
            if clave == -1:
                continue
            if (clave in Productos):
                print(
                    f"Esa clave existe y pertenece al producto: '{Productos[clave]}' \n \n")
                continue
            newDiccionarioValues(Productos=Productos,
                                 Precios=Precios, Stock=Stock, clave=clave)
            print(f"El nuevo produccto: '{producto}' fue agregado con éxito.")

        elif opcion == "2":
            # Eliminar un producto
            deleteValues(Productos=Productos,
                         Precios=Precios, Stock=Stock,)

        elif opcion == "3":
            # Actualizar un producto
            clave = int(
                input("Ingrese el número de producto que desea actualizar: ") or -1)
            if clave in Productos:
                newDiccionarioValues(Productos=Productos,
                                     Precios=Precios, Stock=Stock, clave=clave)

                print(f"Producto '{producto}' actualizado con éxito.")
            else:
                print("Producto no encontrado.")

        elif opcion == "4":
            # Salir del programa
            break

        else:
            print("Esa opción no válida, elija entre las opciones (1, 2, 3 o 4).")

    print("Saliendo del programa.")


if __name__ == "__main__":
    main()
