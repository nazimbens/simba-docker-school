# TP 3 - Docker compose - Connexion Services

## Objectif

Dans ce TP, vous allez apprendre à utiliser Docker Compose pour connecter deux services Docker : une application Python simple et une base de données MySQL.

## Prérequis

- Docker installé sur votre système : Installation de Docker
- Docker Compose installé sur votre système : Installation de Docker Compose
- Connaissance de base de Python

## Étape 1 : Création de l'Application Python

#### 1.1. Créez un dossier nommé `python-app` pour votre projet :

```
mkdir python-app
cd python-app
```

#### 1.2. Dans ce dossier, créez un fichier Python nommé app.py avec le contenu suivant :

```
import os
import pymysql
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    try:
        # Connexion à la base de données MySQL
        db_host = os.environ.get('MYSQL_HOST', 'localhost')
        db = pymysql.connect(host=db_host, user='root', password='mysecretrootpassword', database='mydatabase')

        # Exécution d'une requête SQL simple
        cursor = db.cursor()
        cursor.execute('SELECT * FROM classe_devops LIMIT 1')  # Sélectionnez le premier élément de la table classe_devops

        # Récupération des résultats
        result = cursor.fetchone()

        # Fermeture de la connexion à la base de données
        db.close()

        # Si aucun résultat n'est trouvé, renvoyer un message approprié
        if not result:
            return 'Aucun élément trouvé dans la base de données.', 404

        # Formatage des données récupérées
        element = {
            'id': result[0],
            'nom': result[1],
            'prenom': result[2],
            'notes': result[3],
            'autre_colonne': result[4]
        }

        # Renvoyer les données au format JSON
        return jsonify(element), 200

    except Exception as e:
        return str(e), 500  # Renvoyer l'erreur 500 en cas d'erreur lors de l'accès à la base de données

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)


```

## Étape 2 : Configuration de Docker Compose

#### 2.1. À la racine de votre projet, créez un fichier `docker-compose.yml` avec le contenu suivant :

```
version: '3.7'

services:
  python-app:
    build: .
    ports:
      - "8080:8080"
    environment:
      MYSQL_HOST: db

  db:
    image: mysql:5.7
    environment:
      MYSQL_ROOT_PASSWORD: mysecretrootpassword
      MYSQL_DATABASE: mydatabase

```

## Étape 3 : Exécution de Docker Compose

#### 3.1. Dans le même répertoire que votre fichier `docker-compose.yml`, exécutez la commande suivante pour démarrer les services avec Docker Compose :

`docker-compose up`

Ajoutez ensuite la table suivante dans la base de données :

```
CREATE TABLE classe_devops (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(255) NOT NULL,
    prenom VARCHAR(255) NOT NULL,
    notes FLOAT,
    autre_colonne VARCHAR(255)
);

INSERT INTO classe_devops (nom, prenom, notes) VALUES ('Nom1', 'Prénom1', 15.5);
INSERT INTO classe_devops (nom, prenom, notes) VALUES ('Nom2', 'Prénom2', 14.0);
INSERT INTO classe_devops (nom, prenom, notes) VALUES ('Nom3', 'Prénom3', 12.5);
-- Ajoutez autant d'insertions que nécessaire pour remplir votre table
```


#### 3.2. Test : exécution
Vous devriez voir les conteneurs démarrés.

## Étape 4 : Vérification de la Connexion

#### 4.1. Test : local host 
Ouvrez un navigateur web et accédez à `http://localhost:8080`. Vous devriez voir le message "Hello, Docker Compose!" affiché par votre application Python.

#### 4.2. Test : DB
L'application Python se connecte au service de base de données MySQL en utilisant le nom du service `db` comme hôte (`MYSQL_HOST: db`) en fonction de la configuration de `docker-compose.yml`.

## Étape 5 : Nettoyage

5.1. Pour arrêter et supprimer les conteneurs, exécutez la commande suivante dans le même répertoire que votre fichier `docker-compose.yml` :

`docker-compose down
