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


# Mise en place du projet

## 1) Datasets

1. Commencez par récupérer un csv récent des 2 Datasets. Les données sont mise à jours sur les api tous les jours.
2. Traitement des datasets : Ne garder que les colonnes utiles pour le projet. La clé commune est le jour de l'année.Garder le Dataset des vol d'avion complet, et ne garder que les colonnes de la météo intéressantes tel que la vitesse du vent, où la température.

  - Pour que tout fonctionne, assurez-vous d'avoir placé votre projet dans le dossier Projet_Archi_Distrib . 

  -  
## 2) Communication

L'Objectif est de faire communiquer le producer, présent dans un vscode local, avec le consumer qui se trouve dans le spark-master présent sur docker.
 On commence par télécharger l'image docker-compose.yml.
 Lancer les fichier pythons : producer.py et consumer.py
 
On créer le topic sur la console avec la commande : kafka-topics.sh --create --topic mytopic --bootstrap-server localhost:9092
Ensuite on envoie cette commande : kafka-topics.sh --describe --topic mytopic --bootstrap-server localhost:9092
Et enfin on envoi une 3ème commande qui vas permettre la communication entre le producer et le consumer : kafka-console-producer.sh --topic mytopic --bootstrap-server localhost:9092

Lancer ensuite la commande : spark-submit --master spark://f10e5025887c:7077 --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.3.2 /opt/workspace/consumer.py. Cela lancera le fonctionnement du spark submit.


## 3) Analyse

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


## 4) Utiliser Mongo :
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
