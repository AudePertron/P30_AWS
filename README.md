# Une infra dans le Cloud
Projet de groupe réalisé par Aude et Ludivine

Créer une base PostGres hébergée sur RDS 
Créer une API sur EC2
Executer des requêtes

## 1. Créer l'instance EC2
Tout d'abord nous avons créé une instance sur EC2 (en choisissant les options gratuites, et l'image Ubuntu 20.04)
Nous avons géré les groupes de sécurité afin d'ouvrir les accès.
Nous avons ensuite tout réalisé depuis VS Code, en utilisant l'authentification SSH.

Nous avons décidé de tout créer via docker, avec le docker compose suivant:

```yml
version: '3.1'

services:

  db:
    image: postgres
    container_name: db_brief
    restart: always
    environment:
      POSTGRES_USER: USER #à remplacer
      POSTGRES_PASSWORD: PWD #à remplacer
    volumes:
      - ./clubdata.sql:/clubdata.sql
```
Puis nous avons utilisé le .sql de [cette page](https://pgexercises.com/gettingstarted.html) pour créer la base de données, via un bucket sur S3.

## 2. API
Nous avons choisi FastAPI, pour sa rapidité et sa flexibilité.
Nous avons également créé un docker compose puis avons hébergé l'API sur l'instance EC2.
Nous avons créé quelques requêtes:


## 3. Requêtes
- première requête: récupérer la liste des facilities:
[/api/info](http://35.181.9.190:8000/api/info)

![infos](/images/infos.png)

- deuxième requête: voir quelle facilities sont accessibles pour un prix donné:
[/api/cost/20](http://35.181.9.190:8000/api/cost/20)

![infos](/images/cost.png)

- troisième requête: trouver une facility par son nom:
[/api/facility/Tennis](http://35.181.9.190:8000/api/facility/Tennis)

![infos](/images/facility.png)
