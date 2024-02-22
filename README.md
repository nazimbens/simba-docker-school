# TP4 - Docker Network

# Travaux Pratiques Docker Network

## Objectif

L'objectif de ce TP est de vous familiariser avec Docker Network et d'apprendre à créer, gérer et utiliser des réseaux Docker pour connecter des conteneurs entre eux.

## Étape 1 : Création d'un Réseau Docker

#### 1. Créer le réseau Docker
`docker network create mon-reseau`

#### 2. Vérifier la création du réseau 
`docker network ls`

## Étape 2 : Création de Conteneurs et Connexion au Réseau

Créez deux conteneurs Docker qui sont connectés au réseau que vous avez créé dans l'étape précédente. Utilisez l'image officielle NGINX pour l'un des conteneurs et l'image officielle MySQL pour l'autre :

```
docker run -d --name mon-nginx --network mon-reseau nginx
docker run -d --name mon-mysql --network mon-reseau -e MYSQL_ROOT_PASSWORD=mysecret mysql:5.7
```

Vérifiez que les deux conteneurs sont en cours d'exécution et connectés au réseau `mon-reseau` :
`docker ps`

Vérifiez les détails du réseau `mon-reseau` en utilisant la commande :
`docker network inspect mon-reseau`

## Étape 3 : Test de la Connectivité
Accédez au conteneur NGINX depuis un navigateur web en utilisant l'adresse IP du conteneur. Vous pouvez obtenir l'adresse IP du conteneur NGINX en utilisant la commande suivante :

`docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' mon-nginx`

Connectez-vous au conteneur MySQL en utilisant la commande `docker exec`. Par exemple, pour accéder au shell MySQL :

`docker exec -it mon-mysql mysql -u root -p`

## Étape 4 : Suppression des Conteneurs et du Réseau
Arrêtez et supprimez les conteneurs NGINX et MySQL :

```
docker stop mon-nginx mon-mysql 
docker rm mon-nginx mon-mysql
```

Supprimez le réseau Docker que vous avez créé :

`docker network rm mon-reseau`

