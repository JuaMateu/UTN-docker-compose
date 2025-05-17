from flask import Flask, request
from flask_cors import CORS
import datetime
import os

app = Flask(__name__)
CORS(app)

LOG_FILE = "/logs/multiplicaciones.log"

@app.route("/multiplicar")
def multiplicar():

    # valida los parámetros
    try:
        x = float(request.args.get("x"))
        y = float(request.args.get("y"))
    except (TypeError, ValueError):
        return "Parámetros inválidos. Probá /multiplicar?x=2&y=3", 400

    # calcula la multiplicación y genera el mensaje
    resultado = x * y
    mensaje = f"Se multiplicó {x} por {y}, el resultado fue {resultado}"

    # Asegura que el directorio exista
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

    # Escribe el mensaje en el archivo de log
    with open(LOG_FILE, "a") as log:
        log.write(f"[{datetime.datetime.now()}] {mensaje}\n")

    # Devuelve el mensaje al usuario
    return mensaje

#ruta para ver los logs
@app.route("/logs")
def ver_logs():
    # Verifica si el archivo de log existe
    if not os.path.exists(LOG_FILE):
        return "No hay logs aún."
    # Lee el contenido del archivo de log
    with open(LOG_FILE, "r") as log:
        contenido = log.read()
    # Devuelve el contenido del archivo de log
    return f"<pre>{contenido}</pre>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)