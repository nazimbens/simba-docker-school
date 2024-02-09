# Utilisez une image de base Python
FROM python:3.8-slim

# Définissez le répertoire de travail dans le conteneur
WORKDIR /app

# Copiez le fichier requirements.txt (s'il existe) et installez les dépendances
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiez le code source dans le conteneur
COPY app.py .

# Exposez le port sur lequel le serveur Flask écoute (si nécessaire)
EXPOSE 8080

# Commande pour exécuter l'application Python
CMD ["python", "app.py"]

