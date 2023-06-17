from flask import Flask, render_template, request

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
    return render_template('index.html')

@app.route('/guardar', methods=['POST'])
def guardar(): 
    if request.method == 'POST':
        titulo = request.form['txtTitulo']
        artista = request.form['txtArtista']
        anio = request.form['txtAnio']
        print(titulo, artista, anio)
    
    return "La info del album llego a su ruta friend;)"

@app.route('/eliminar')
def eliminar():
    return "se elimino el album en la BD"


#ejecutan el servidor
if __name__=='__main__':
    app.run(port= 5000, debug=True)