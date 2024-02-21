# TP6 - Docker Volumes

# Lister les volumes 

`docker volume ls`

# Créer un volume

`docker volume create <name-volume>

Dans notre cas on va créer le volume suivant :

`docker volume create mynginx`

Appelez le en fonction de vos besoins et ayant un lien avec le container que l'on va créer

# Vérifier que son volume a bien été créer 

`docker volume ls`

# Associer son volume au container 

Pour utiliser ce volume, on va utiliser la ligne de commande docker pour exécuter/lancer un container : 

`docker run -d --name <name-container> -v <name-volume>:/var/data/ <name-image>:latest`

Pour notre exemple on va utiliser `mynginx`

`docker run -d --name c1 -v mynginx:/user/share/nginx/html/ nginx:latest`

# Vérifier que le container existe 

`docker exec -ti c1 bash`

-ti permet de rentrer directement à l'intérieur du container

On se retrouve maintenant à l'intérieur d'un bash comme si on était à l'intérieur du container.

`ls` permet d'afficher les dossiers et fichiers présents.

`ls /usr/share/nginx/html/` on retrouve à l'intérieur notre fichier `index.html`

`cat /usr/share/nginx/html/index.html` on peut avoir apparaître le code de la page d'accueil du serveur nginx. 

# Retrouver le fichier à l'extérieur : dans le host

`docker volume inspect mynginx`

On va donc voir apparaître notre point de montage sur le Host (en local). Vérifions donc que ce point de montage est bien raccordé et possède les mêmes fichiers que notre container. 

`sudo ls <chemin>`

Afficher le contenu du fichier 

`sudo cat <chemin>`

# Modification du fichier 

Dans le terminal de votre serveur Nginx, modifiez le fichier index.html 

`echo toto > /usr/share/nginx/html/index.html`

Vérifiez ensuite que la modification a été faite en local.

`sudo cat <chemin>`

On verra que la modification a bien été prise en compte ! 

# Attribuer ce volume à un nouveau container

`docker run -ti --name c2 --rm -v mynginx:/data/ debian:latest bash`

Vérifier que le fichier index.html se trouve bien ici. 

`ls /data/`

Afficher le contenu du fichier index.html

`cat /data/index.html`

On retrouve bien toto ! Et si on le modifiait 🙃

`echo titi > /data/index.html`

Si on souhaite supprimer il faut stopper et supprimer le container en utilisation 

`docker volume rm mynginx`

Même si je supprime tous les container au niveau du HOST, le volume est persistant et il reste intacte en local. 


