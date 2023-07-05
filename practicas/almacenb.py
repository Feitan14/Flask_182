import sqlite3

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

def eliminar_bebida():
    id_bebida = int(input("Ingrese el ID de la bebida que desea eliminar: "))

    conn = sqlite3.connect('almacen_bebidas.db')
    c = conn.cursor()
    c.execute("DELETE FROM bebidas WHERE id = ?", (id_bebida,))
    conn.commit()
    conn.close()

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

def mostrar_bebidas():
    conn = sqlite3.connect('almacen_bebidas.db')
    c = conn.cursor()
    c.execute("SELECT * FROM bebidas")
    bebidas = c.fetchall()

    if bebidas:
        print("ID  |  Nombre         |  Clasificación   |  Marca       |  Precio")
        print("---------------------|-----------------|--------------|---------")
        for bebida in bebidas:
            print("{:3d} | {:15s} | {:16s} | {:12s} | {:.2f}".format(bebida[0], bebida[1], bebida[2], bebida[3], bebida[4]))
    else:
        print("No hay bebidas en el almacén.")

    conn.close()

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

def calcular_cantidad_por_marca():
    marca = input("Ingrese el nombre de la marca: ")

    conn = sqlite3.connect('almacen_bebidas.db')
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM bebidas WHERE marca = ?", (marca,))
    cantidad = c.fetchone()[0]
    conn.close()

    print("La cantidad de bebidas de la marca {} es: {}".format(marca, cantidad))

