from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
<<<<<<< HEAD
    return "Si lees esto estas en Prod. No deberias estar en Prod."
=======
    return "Servidor de develop. Aca van las nuevas features."
>>>>>>> develop

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
