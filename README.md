# Projet d'Architechture distribué

# Introduction du Projet

Ce github contient notre projet d'Architecture distribué encadré par M. LIMA. Nous avons décidé de travailler sur une corrélation entre la météo en Europe et Les vols d'avions chaque jours en Europe également. Pour la météo, nous avons récupérer les données en fichiers csv sur une api donnant la météo en europe en streaming, ansi que les données archivées des jours précédents. Pour les vols d'avions, on a également récupéré un fichier csv sur un site web appelé opensky qui permet de récupérer les données des avions ayant décollé ou atteri dans les différents pays d'Europe. Notre objectif serai de voir si la météo en europe influe sur le nombre de départ et d'arrivé de vol d'avion dans les différent pays européens.

# Prérequis

Pour éxécuter ce projet, vous aurez besoin de plusieurs éléments :
- [**Python**](https://www.python.org/)
- [**Doker**](https://www.docker.com/products/docker-desktop/)
- [**Spark**](https://spark.apache.org/downloads.html)
- [**Kafka**](https://kafka.apache.org/downloads)
- [**MongoDB Shell**](https://www.mongodb.com/try/download/shell)
- [**MongoDB Compass**](https://www.mongodb.com/products/compass)

Dépendance à Installer:
- [**Pandas**](https://pandas.pydata.org/)
- [**Pyspark**](https://pypi.org/project/pyspark/)
- [**Pymongo**](https://www.mongodb.com/docs/drivers/pymongo/)
- [**Kafka-python**](https://pypi.org/project/kafka-python/)


# Mise en place du projet

## 1) Datasets

1. Commencez par récupérer un csv récent des 2 Datasets. Les données sont mise à jours sur les api tous les jours.
2. Traitement des datasets : Ne garder que les colonnes utiles pour le projet. La clé commune est le jour de l'année.Garder le Dataset des vol d'avion complet, et ne garder que les colonnes de la météo intéressantes tel que la vitesse du vent, où la température.

  - Pour que tout fonctionne, assurez-vous d'avoir placé votre projet dans le dossier Projet_Archi_Distrib . 

  -  
## 2) Démarrage

1. Créez l'image de docker compose en mettant kafka, zookeper,  spark-master et spark-worker dans la même image :docker-compose.yml
2. Stockez le 'docker-compose.yml' dans le même dossier que les datasets qui sera en finalité votre dossier de projet
3. Lancez ensuite le cluster docker
4. Ouvrir une invite de commande puis dirigez vous dans le dossier du projet en faisant 'cd .....' puis 'docker-compose up
5. Retounez dans docker desktop pour voir si les containers tournent bien correctement, ou bien faites un 'docker ps' pour voir les vm qui tournent

## 3) Communication

1. Connectez vous aux VM de spark-master et de kafka. Pour ce faire veuillez utiliser la commande : docker exec -it kafka bash' et 'docker exec -it spark-master bash
2. Puis allez sur la VM de kafka, puis créer un topic en faisant cette fois-ci la commande : kafka-topics.sh --create --topic mytopic --bootstrap-server localhost:9092
3. Pour vérifier votre topic, vous pouvez voir la description des topics sur la vm en réalisant la commande suivante : kafka-topics.sh --describe --topic mytopic --bootstrap-server localhost:9092
4. Ouvrir maintenant le fichier python 'consumer.py' qui se situe dans le dossier du projet sur la machine locale, puis copier ce fichier dans la VM de spark-master en faisant la commande : 'docker cp consumer.py spark-master:/usr/bin/spark-3.0.0-bin-hadoop3.2/bin', en ouvrant une invite de commande avec le path du dossier du projet
5. Ouvrir ensuite le fichier python 'producer.py' et le lancer n'importe où sur la machine locale (par exemple vscode, jupyterlab ...)
6. Veuillez aprèse Retourner sur la VM du spark-master, à l'endroit où le fichier 'consumer.py' se situe, et faites ensuite un spark-submit : ./spark-submit --master spark://spark-master:7077 --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.3.2 /usr/bin/spark-3.0.0-bin-hadoop3.2/bin/consumer.py


## 4) Analyse

1. Une fois tout cela réalisé, nous avons envoyé nos fichier csv dans une base MongoDB
Ouvrir Visual Studio Code et ouvrir le dossier du site.
Ouvrir le dossier de la base de données sur l'éditeur.
Ouvrir MongoDB Compass à côté pour visualiser les collections qui se sont insérées.
Lancer les scripts python (dans VSCode) dans l'ordre suivant:
Les 3 programmes insert :
Dossier1
Dossier2
L'agregate :
DossierAggregate
Lors de l'ouverture de MongoDB Compass, une fois s'être connecté, après l'insertion des programmes python précédents, nous obtenons donc 3 collections distinctes dans une base de données qui s'appelle Projet.

2. Pour visualiser les diagrammes d'analyses de données, lancez les fichiers suivants que vous trouverez dans Dossier_analyse.
  - **Analyse1;py** :
  - **Analyse2.py** :
  - **Analyse3.py** :
  - **Analyse4.py** : 
  - **Analyse5.py** : 


## 5) Utiliser Mongo :
Vous pouvez utiliser une invite de commandes MongoDB pour modifier les données de votre base NoSQL. Ci-dessous, voici quelques commandes de base si vous voulez vous essayer à Mongo Shell.

Pour lancer Mongo Shell, veuilez aller sur le dossier de votre MongoDB Shell > bin > mongo.exe

Si vous voulez afficher les collections de la base :
```python
show collections
```

Si vous voulez visualiser tout le contenu de la collection :
```python
db.collection.find()
```

Si vous voulez rechercher une valeur en particulier :
```python
db.collection.find({ nom_de_la_colonne: 'valeur' })
```

Si vous voulez ajouter un élément à votre base :
```python
db.collection.insertOne({ nom_de_la_colonne : 'valeur', nom_de_la_colonne_2 : 'valeur'})
```

Si vous voulez supprimer un élément à votre base :
```python
db.collection.deleteOne({ "_id": x })
```

Si vous voulez modifier un élément à votre base :
```python
db.collection.updateOne({ _id: x }, { $set: { "nom_de_la_colonne": "valeur" } })
```
