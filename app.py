# app.py
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
        cursor.execute('SELECT * FROM classe_devops LIMIT 1')

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
            'notes': result[3]
        }

        # Renvoyer les données au format JSON
        return jsonify(element), 200

    except Exception as e:
        return str(e), 500  # Renvoyer l'erreur 500 en cas d'erreur lors de l'accès à la base de données        

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

