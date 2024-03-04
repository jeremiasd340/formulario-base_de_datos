from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# Configuración de la conexión a la base de datos
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="jered340",
    database="formulario"
)

# Manejo de errores al conectar a la base de datos
if db.is_connected():
    print("Conexión exitosa a la base de datos")
else:
    print("Error al conectar a la base de datos")

# Ruta para mostrar el formulario
@app.route('/', methods=['GET'])
def formulario():
    return render_template('formulario.html')

# Ruta para procesar los datos enviados desde el formulario
@app.route('/registro', methods=['POST'])
def guardar():
    try:
        # Obtener los datos del formulario
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        correo = request.form['gmail']
        contrasena = request.form['contraseña']

        # Crear un cursor para ejecutar consultas SQL
        cursor = db.cursor()

        # Consulta SQL para insertar los datos en la base de datos
        sql = "INSERT INTO usuarios (nombre, apellido, correo, contrasena) VALUES (%s, %s, %s, %s)"
        val = (nombre, apellido, correo, contrasena)

        # Ejecutar la consulta SQL
        cursor.execute(sql, val)

        # Confirmar los cambios en la base de datos
        db.commit()

        # Devolver un mensaje indicando que los datos se han guardado correctamente
        return '¡Datos guardados correctamente!'
    except Exception as e:
        # Si ocurre algún error, imprimirlo y devolver un mensaje de error al cliente
        print("Error al guardar datos:", e)
        return 'Error al procesar los datos, por favor inténtalo de nuevo.'

if __name__ == '__main__':
    # Iniciar la aplicación Flask en modo debug
    app.run(debug=True)

# Cerrar la conexión a la base de datos al finalizar la aplicación
# db.close()  # Comentado para evitar cerrar la conexión antes de tiempo
