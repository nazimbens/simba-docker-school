#app.py 
import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    # Récupérer la valeur de la variable d'environnement 'MA_VARIABLE' (changez le nom au besoin)
    ma_variable = os.environ.get('MA_VARIABLE', 'Valeur par défaut si la variable n\'est pas définie')
    return f'Contenu de la variable d\'environnement MA_VARIABLE : {ma_variable}'

if __name__ == '__main__':
    # Spécifier le port 8080 pour le serveur
    port = int(os.environ.get('PORT', 8080))
    
    # Démarrer le serveur Flask
    app.run(host='0.0.0.0', port=port)

