# Projet d'Architechture distribuée

# Introduction du Projet

Ce github contient notre projet d'Architecture distribué encadré par M. LIMA. Nous avons décidé de travailler sur une corrélation entre la météo en Europe et Les vols d'avions chaque jours en Europe également. Pour la météo, nous avons récupérer les données en fichiers csv sur une api donnant la météo en europe en streaming, ansi que les données archivées des jours précédents. Pour les vols d'avions, on a également récupéré un fichier csv sur un site web appelé opensky qui permet de récupérer les données des avions ayant décollé ou atteri dans les différents pays d'Europe. Notre objectif serai de voir si la météo en europe influe sur le nombre de départ et d'arrivé de vol d'avion dans les différent pays européens.

Voici le lien de notre Trello pour la gestion de notre projet : [**Trello**](https://trello.com/b/QQXGw0yf/archtecture-distribu%C3%A9e)

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
6. Veuillez a prèsent Retourner sur la VM du spark-master, à l'endroit où le fichier 'consumer.py' se situe, et faites ensuite un spark-submit : ./spark-submit --master spark://spark-master:7077 --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.3.2 /usr/bin/spark-3.0.0-bin-hadoop3.2/bin/consumer.py

Hélas nous sommes restés bloqués à un probleme de checkpoint entre un producer externe et le consumer, au moment de faire l'exécution du spark-submit du fichier consumer.py sur la vm spark-master, nous avons eu énormement de problèmes. Le dernier étant un problème de checkpoint. Par conséquent, nous avons perdus trop de temps à essayer de résoudres les différentes erreurs, nous n'avons pas pu terminer le projet entièrement et à temps.

 
Nous avons tout de même réussi à faire communiquer le producer et le consumer en écrivant des données brutes dans le producer. (Voir image ci-dessous).

![image](https://user-images.githubusercontent.com/129997458/230249883-d7af706d-e0cd-4a24-8e7f-da2220d80e9f.png)


Pour avoir ce résultat, il faut dans un premier temps, se connecter à la vm kafka (docker exec -it kafka bash) puis exécuter cette commande : kafka-topics.sh --create --bootstrap-server localhost:9092 --topic mytopic2. Ensuite exécuter cette commande : kafka-console-producer.sh --bootstrap-server localhost:9092 --topic mytopic2 --property "parse.key=true" --property "key.separator=:".

Ouvrir le fichier python 'read_test_pyspark.py' et le copier depuis un cmd local où est répértorié le fichier en question dans la vm de spark-master (docker cp read_test_pyspark.Py spark-master:/opt/workspace/spark/bin/).

Puis se connecter sur la vm de spark-master(docker exec -it spark-master bash) et lancer : spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.3.0 /opt/workspace/spark/bin/read_test_pyspark.py


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

2. Pour visualiser les diagrammes d'analyses de données, nous utiliserons l'outil PowerBI. Nous prendrons 2 fichiers csv, et nous les feront correler en cochant les champs qui nous interesse dans chacunes des analyses que nous montrerons lors de l'oral


## 5) Utiliser Mongo :
Vous pouvez utiliser une invite de commandes MongoDB pour modifier les données de votre base NoSQL. Ci-dessous, voici quelques commandes de base si vous voulez vous essayer à Mongo Shell.

Nous n'avons malheureusement pas pu allez jusqu'à cet étape, mais voici ci-desous comment il faut procéder :


Dans le cas où nous souhaiterions stocké nos csv dans mongo, nous pouvons simplement lancé ce script python qui va nous permettre de créer une base, et d'insérer les données que nous souhaitons : 'prog_insert_csv_in_mongo.py'.
Attention dans les fichier lié à mongo, au niveau de 'GET_DATABASE' changer le lien et mettre celui de VOTRE base mongo.

Pour lancer Mongo Shell, veuilez aller sur le dossier de votre MongoDB Shell > bin > mongo.exe.

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
