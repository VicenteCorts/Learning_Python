# Clase 205 - Creando nuestra primera Web con Python
# Composición Básica de Flask para Website:
from flask import Flask, render_template

app=Flask(__name__)
### Creación de rutas *************************************
@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about/')
def about():
    return render_template("about.html")
### FIN Creación de rutas *********************************


### Explicación en CLase 205 sobre __main__ y scripts importados
if __name__ == "__main__":
    app.run(debug=True)

# FIN Composición Básica de Flask para Website:






















