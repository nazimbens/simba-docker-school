# TP1 BASICS 

## Étape 1 : Premier Conteneur

#### 1.1. Vérifiez que Docker est installé en exécutant la commande suivante :

`docker --version`

#### 1.2. Créez et exécutez votre premier conteneur Docker en utilisant l'image `hello-world` :

`docker run hello-world`

#### 1.3. Observez la sortie pour comprendre les étapes de création et d'exécution d'un conteneur Docker.

## Étape 2 : Utilisation d'une Image Docker

#### 2.1. Recherchez l'image Docker officielle de Nginx sur Docker Hub :

`docker search nginx`

#### 2.2. Téléchargez l'image Nginx :

`docker pull nginx`

#### 2.3. Vérifiez que l'image a été téléchargée en exécutant la commande :

`docker images`

## Étape 3 : Exécution d'un Conteneur Nginx

#### 3.1. Exécutez un conteneur Nginx en utilisant l'image téléchargée :

`docker run -d -p 80:80 --name mon-nginx nginx`

#### 3.2. Vérifiez que le conteneur Nginx est en cours d'exécution :

`docker ps`

#### 3.3. Accédez au serveur Nginx depuis votre navigateur en visitant `http://localhost`. Vous devriez voir la page par défaut de Nginx.

## Étape 4 : Gestion des Conteneurs

#### 4.1. Arrêtez le conteneur Nginx :

`docker stop mon-nginx`

#### 4.2. Vérifiez que le conteneur est arrêté :

`docker ps -a`

#### 4.3. Redémarrez le conteneur Nginx :

`docker start mon-nginx`

#### 4.4. Supprimez le conteneur Nginx :

`docker rm mon-nginx`

#### 4.5. Vérifiez que le conteneur a été supprimé :

`docker ps -a`

## Étape 5 : Nettoyage

#### 5.1. Supprimez l'image Nginx (vous pouvez le faire si vous n'avez plus besoin de l'image) :

`docker rmi nginx`

#### 5.2. Vérifiez que l'image a été supprimée :

`docker images`

## Étape 6  : Entrer dans le bash de Ubuntu

#### 6.1. Lancez une image ubuntu en exécutant l'application Bash:

`docker run -it ubuntu bash`

#### 6.2. Vérifiez que l'image a été supprimée :

`docker images`
