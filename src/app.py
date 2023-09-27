from flask import Flask

# Crea una instancia de la aplicación Flask
app = Flask(__name__)

# Define una ruta y función de vista para la ruta raíz
@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    # Ejecuta la aplicación en el puerto 5000
    app.run(host='127.0.0.1', port=5000)
