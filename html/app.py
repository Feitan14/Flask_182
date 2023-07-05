from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuración de la base de datos SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'  # Nombre de la base de datos
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Definición del modelo de datos
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rfc = db.Column(db.String(15), nullable=False)
    nombre = db.Column(db.String(100), nullable=False)
    apellido_paterno = db.Column(db.String(100), nullable=False)
    apellido_materno = db.Column(db.String(100), nullable=False)
    matricula = db.Column(db.String(20), nullable=False)
    correo = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    rol = db.Column(db.String(20), nullable=False)

# Ruta para el formulario
@app.route('/')
def index():
    return render_template('formulario.html')

# Ruta para procesar los datos del formulario
@app.route('/registro', methods=['POST'])
def registro():
    rfc = request.form['rfc']
    nombre = request.form['nombre']
    apellido_paterno = request.form['apellido_paterno']
    apellido_materno = request.form['apellido_materno']
    matricula = request.form['matricula']
    correo = request.form['correo']
    password = request.form['password']
    rol = request.form['rol']

    nuevo_usuario = Usuario(rfc=rfc, nombre=nombre, apellido_paterno=apellido_paterno,
                            apellido_materno=apellido_materno, matricula=matricula,
                            correo=correo, password=password, rol=rol)

    db.session.add(nuevo_usuario)
    db.session.commit()

    return 'Usuario registrado correctamente'

if __name__ == '__main__':
    app.run()
