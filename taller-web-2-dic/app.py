from flask import Flask, render_template
import requests 

# Crear una aplicacion flask 
app = Flask(__name__) 

# Definimos una ruta 
@app.route("/")
def inicio (): 
    # Hacer un pediddo a la api de rick and morty 
    personajes = requests.get('https://rickandmortyapi.com/api/character').json()
    personajes = personajes['results']
    print(personajes)
    return render_template('inicio.html',personajes=personajes)


if __name__ == "__main__":
    app.run(debug=True) 