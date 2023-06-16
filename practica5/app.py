from flask import Flask

#inicializacion del servidor Flask
app= Flask(__name__)
app.config['MySQL_HOST'] = "localhost"
app.config['MySQL_USER'] = "root"
app.config['MySQL_PASSWORD'] = ""
app.config['MySQL_BD'] = "bdflask"

#declaramos una ruta
#ruta se compone de nombre y funcion 
#ruta index o ruta principal: (http://localhost:5000)
@app.route('/')
def index():
    return "Hola mundo"

@app.route('/guardar')
def guardar():
    return "se guardo el album en la BD"

@app.route('/eliminar')
def eliminar():
    return "se elimino el album en la BD"


#ejecutan el servidor
if __name__=='__main__':
    app.run(port= 5000, debug=True)