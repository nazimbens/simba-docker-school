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
