import sqlite3

#creamos la base de datos y las tablas
def crear_tabla():
    conn = sqlite3.connect('almacen_b.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS bebidas id
              (id INTEGER PRIMARY KEY AUTOINCREMENT,nombre TEXT,
              clasificacion TEXT, 
              marca TEXT,
              precio REAL)''')
    conn.commit()
    conn.close()
    
#funcion para agregar bebidas
def agregar_bebida():
    nombre = input("ingrese el bombre de la bebida: ")
    cla = input("ingrese la clasificacion de la bebida: ")
    marca = input("ingrese la marca de la bebida: ")
    precio = float(input("ingrese el precio de la bebida: "))
    
    conn = sqlite3.connect('almacen_b.bd')
    c = conn.cursor()
    c.execute("INSERT INTO bebidas(nombre, clasificacion, marca, precio) VALUES(?, ?, ?, ?)",
              (nombre, cla, marca, precio))
    conn.commit()
    conn.close()
    
#funcion para eliminar una bebida
def eliminar_bebida():
    id_bebida = int(input("ingrese el id de la bebida que desea eliminar: "))
    
    conn = sqlite3.connect('almacen_b.db')
    c = conn.cursor()
    c.execute("SELECT * FROM bebidas WHERE id = ?", (id_bebida,))
    bebida = c.fetchone()
    
    if bebida:
        print("Datos actuales de la bebida: ")
        print("Nombre: ",bebida[1])
        print("Clasificacion: ",bebida[2])
        print("Marca: ",bebida[3])
        print("Precio: ",bebida[4])
        
        if nombre == "":
            nombre = bebida[1]
        if cla == "":
            cla = bebida[2]
        if marca == "":
            marca = bebida[3]
        if precio == "":
            precio = bebida[4]
        else:
            precio = float(precio)
        
        c.execute("UPDATE bebidas SET")