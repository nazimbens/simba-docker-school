# TP5 - Docker Compose - Networking

## Étape 1 : Création de l'Application Python

#### 1.1. Créez un dossier nommé `python-app` pour votre projet :

```
mkdir python-app
cd python-app
```

#### 1.2. Dans ce dossier, créez un fichier Python nommé app.py avec le contenu suivant :

```
from flask import Flask
from redis import Redis, RedisError
import os
import socket

# Connect to Redis
redis = Redis(host="redis", db=0, socket_connect_timeout=2, socket_timeout=2)

app = Flask(__name__)

@app.route("/")
def hello():
    try:
        visites = redis.incr("compteur")
    except RedisError:
        visites = "<i>Erreur de connection Redis, compteur desactive</i>"

    html = "<h3>Bonjour {nom}!</h3>" \
           "<b>Hostname:</b> {hostname}<br/>" \
           "<b>Visites:</b> {visites} <br/>" \
           "<p>Abonne toi!</p>"
    return html.format(nom=os.getenv("NOM", "youtube"), hostname=socket.gethostname(), visites=visites)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
```

#### 1.3.  Créez un fichier Python nommé requirements.txt avec le contenu suivant :

```
Flask
Redis
```

#### 1.3.  Créez un fichier Python nommé docker-compose.yml avec le contenu suivant :

```
version: "3"
services:
  monapp:
    build: .
    image: monimage
    depends_on:
      - redis
    ports:
      - "80:80"
    networks:
      - monreseau
    environment:
      - NOM=les amis
  redis:
    image: redis
    networks:
      - monreseau

networks:
  monreseau:
```

#### 1.4 Créer le Dockerfile de l'image python 

```
FROM python:2.7-slim
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 80
ENV NOM coca
CMD ["python", "app.py"]
```


## Étape 2 : Exécution de Docker Compose

#### 2.1. Dans le même répertoire que votre fichier `docker-compose.yml`, exécutez la commande suivante pour démarrer les services avec Docker Compose :

`docker-compose up -d

#### 2.2. Test : exécution
Vous devriez voir les conteneurs démarrés.
