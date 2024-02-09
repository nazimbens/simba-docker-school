# TP 2 - Création d'une image docker

## Objectif

Dans ce TP, vous allez apprendre à créer une image Docker personnalisée contenant une application Python simple, puis à exécuter un conteneur basé sur cette image.

## Étape 1 : Création d'une Application Python Simple

#### 1.1. Créez un dossier nommé `python-app` pour votre projet :

`mkdir python-app cd python-app`

#### 1.2. Dans ce dossier, créez un fichier Python nommé `app.py` avec le contenu suivant :

``` 
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

```

## Étape 2 : Création d'une Image Docker

#### 2.1. Créez un fichier Docker nommé `Dockerfile` (sans extension) dans le même dossier que votre application Python `python-app`.

#### 2.2. Éditez le fichier `Dockerfile` avec le contenu suivant pour créer une image Docker personnalisée :

```
# Utilisez une image de base Python
FROM python:3.8-slim

# Copiez votre code Python dans le conteneur
COPY app.py /app.py

# Installez les dépendances (dans ce cas, Flask)
RUN pip install flask

# Définissez une variable d'environnement
ENV MA_VARIABLE "Valeur de la variable d'environnement"

# Exposez le port sur lequel le serveur Flask écoute
EXPOSE 8080

# Exécutez votre application lorsque le conteneur démarre
CMD ["python", "/app.py"]
```

#### 2.3. Construisez l'image Docker en utilisant le `Dockerfile` :

`docker build -t python-app-image .`

## Étape 3 : Exécution d'un Conteneur Python

#### 3.1. Exécutez un conteneur basé sur l'image Docker que vous avez créée :

`docker run -p 8080:8080 python-app-image`

#### 3.2. Vous devriez voir la sortie de votre application Python, qui devrait afficher la valeur de votre variable d'environnemen

## Étape 4 : Nettoyage

#### 4.1. Arrêtez et supprimez le conteneur que vous avez exécuté :

```
docker stop $(docker ps -q --filter ancestor=python-app-image) 
docker rm $(docker ps -aq --filter ancestor=python-app-image)
```

#### 4.2. Supprimez l'image Docker que vous avez créée :

`docker rmi python-app-image`
