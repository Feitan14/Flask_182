import sqlite3

# Función para crear la tabla de bebidas en la base de datos
def crear_tabla():
    conn = sqlite3.connect('almacen_bebidas.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS bebidas
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 nombre TEXT,
                 clasificacion TEXT,
                 marca TEXT,
                 precio REAL)''')
    conn.commit()
    conn.close()

# Función para agregar una nueva bebida
def agregar_bebida():
    nombre = input("Ingrese el nombre de la bebida: ")
    clasificacion = input("Ingrese la clasificación de la bebida: ")
    marca = input("Ingrese la marca de la bebida: ")
    precio = float(input("Ingrese el precio de la bebida: "))

    conn = sqlite3.connect('almacen_bebidas.db')
    c = conn.cursor()
    c.execute("INSERT INTO bebidas (nombre, clasificacion, marca, precio) VALUES (?, ?, ?, ?)",
              (nombre, clasificacion, marca, precio))
    conn.commit()
    conn.close()

# Función para eliminar una bebida
def eliminar_bebida():
    id_bebida = int(input("Ingrese el ID de la bebida que desea eliminar: "))

    conn = sqlite3.connect('almacen_bebidas.db')
    c = conn.cursor()
    c.execute("DELETE FROM bebidas WHERE id = ?", (id_bebida,))
    conn.commit()
    conn.close()

# Función para actualizar los datos de una bebida
def actualizar_bebida():
    id_bebida = int(input("Ingrese el ID de la bebida que desea actualizar: "))

    conn = sqlite3.connect('almacen_bebidas.db')
    c = conn.cursor()
    c.execute("SELECT * FROM bebidas WHERE id = ?", (id_bebida,))
    bebida = c.fetchone()

    if bebida:
        print("Datos actuales de la bebida:")
        print("Nombre:", bebida[1])
        print("Clasificación:", bebida[2])
        print("Marca:", bebida[3])
        print("Precio:", bebida[4])

        nombre = input("Ingrese el nuevo nombre de la bebida (deje en blanco para no modificar): ")
        clasificacion = input("Ingrese la nueva clasificación de la bebida (deje en blanco para no modificar): ")
        marca = input("Ingrese la nueva marca de la bebida (deje en blanco para no modificar): ")
        precio = input("Ingrese el nuevo precio de la bebida (deje en blanco para no modificar): ")

        if nombre == "":
            nombre = bebida[1]
        if clasificacion == "":
            clasificacion = bebida[2]
        if marca == "":
            marca = bebida[3]
        if precio == "":
            precio = bebida[4]
        else:
            precio = float(precio)

        c.execute("UPDATE bebidas SET nombre = ?, clasificacion = ?, marca = ?, precio = ? WHERE id = ?",
                  (nombre, clasificacion, marca, precio, id_bebida))
        conn.commit()
        print("Bebida actualizada correctamente.")
    else:
        print("No se encontró una bebida con el ID proporcionado.")

    conn.close()

# Función para mostrar todas las bebidas
def mostrar_bebidas():
    conn = sqlite3.connect('almacen_bebidas.db')
    c = conn.cursor()
    c.execute("SELECT * FROM bebidas")
    bebidas = c.fetchall()

    if bebidas:
        print("ID  |  Nombre        |  Clasificación  |  Marca      |  Precio")
        print("-------------------------------------------------------------")
        for bebida in bebidas:
            print("{:3d} | {:14s} | {:15s} | {:11s} | {:.2f}".format(bebida[0], bebida[1], bebida[2], bebida[3], bebida[4]))
    else:
        print("No hay bebidas en el almacén.")

    conn.close()

# Función para calcular el precio promedio de las bebidas
def calcular_precio_promedio():
    conn = sqlite3.connect('almacen_bebidas.db')
    c = conn.cursor()
    c.execute("SELECT AVG(precio) FROM bebidas")
    precio_promedio = c.fetchone()[0]
    conn.close()

    if precio_promedio:
        print("El precio promedio de las bebidas es: {:.2f}".format(precio_promedio))
    else:
        print("No hay bebidas en el almacén.")

# Función para calcular la cantidad de bebidas de una marca
def calcular_cantidad_por_marca():
    marca = input("Ingrese el nombre de la marca: ")

    conn = sqlite3.connect('almacen_bebidas.db')
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM bebidas WHERE marca = ?", (marca,))
    cantidad = c.fetchone()[0]
    conn.close()

    print("La cantidad de bebidas de la marca {} es: {}".format(marca, cantidad))

# Función para calcular la cantidad de bebidas por clasificación
def calcular_cantidad_por_clasificacion():
    clasificacion = input("Ingrese la clasificación: ")

    conn = sqlite3.connect('almacen_bebidas.db')
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM bebidas WHERE clasificacion = ?", (clasificacion,))
    cantidad = c.fetchone()[0]
    conn.close()

    print("La cantidad de bebidas de la clasificación {} es: {}".format(clasificacion, cantidad))

# Función principal del programa
def main():
    crear_tabla()

    while True:
        print("\n--- ALMACÉN DE BEBIDAS ---")
        print("1. Agregar bebida")
        print("2. Eliminar bebida")
        print("3. Actualizar bebida")
        print("4. Mostrar todas las bebidas")
        print("5. Calcular precio promedio de bebidas")
        print("6. Cantidad de bebidas de una marca")
        print("7. Cantidad de bebidas por clasificación")
        print("8. Salir")

        opcion = input("\nIngrese una opción: ")

        if opcion == "1":
            agregar_bebida()
        elif opcion == "2":
            eliminar_bebida()
        elif opcion == "3":
            actualizar_bebida()
        elif opcion == "4":
            mostrar_bebidas()
        elif opcion == "5":
            calcular_precio_promedio()
        elif opcion == "6":
            calcular_cantidad_por_marca()
        elif opcion == "7":
            calcular_cantidad_por_clasificacion()
        elif opcion == "8":
            break
        else:
            print("Opción inválida. Por favor, ingrese un número del 1 al 8.")

    print("¡Hasta luego!")

# Ejecutar el programa
if __name__ == "__main__":
    main()
