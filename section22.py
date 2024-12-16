# Clase 205 - Creando nuestra primera Web con Python
## Composición Básica de Flask para Website:
from flask import Flask

app=Flask(__name__)
### Creación de página individual
@app.route('/')
def home():
    return "Página principal - Homepage"

@app.route('/about/')
def about():
    return "Página about"
### FIN Creación de página individual
## FIN Composición Básica de Flask para Website:

## Explicación en CLase 205 sobre __main__ y scripts importados
if __name__ == "__main__":
    app.run(debug=True)
























