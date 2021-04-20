# Hybridation au sein d’un ensemble

## Description courte du scénario d'analyse

Chaque module **requière différente pédagogie** pour une meilleure compréhension. Ainsi, des activités (visionnage d'une vidéo, réalisation d'un quiz, ect) peuvent intégrer une séquence pédagogique, alors que d'autres activités (participation à un débat, présentation, ect) peuvent uniquement être réalisés  en présentiel. Il est intéressant de comprendre les facteurs qui réduisent **l'hybridation totale** d'un module (ex: facteur technique, ou humain). L'object de ce package est de visualiser d'un point de vue universitaire et départementale, la proportion d'hybridation de chaque module. \
Le public d'un MOOC étant plus large que son public natif*, améliorer l'hybridation des modules peuvent améliorer leur popularité.

### Tag
Hybridation

## Cas d’utilisation

### Orientés concepteurs

#### Identification des ressources exploitables

Parmi les modules proposés par les enseignants, de nombreuses ressources ne sont pas exploités à travers des MOOCs. Un concepteur souhaite enrichir le contenu de son cours et améliorer l'hybridation de celui-ci. Il lui faut ainsi distinguer les ressources non exploitées et celles non exploitables.

#### Identification des niveaux d'hybridation

On cherche à identifier pour les durées de modules, la proportion d'hybridation de chacun. Des compréhensions possibles: impossibilité de concevoir une grande hybridation pour le module, manque d'implémation du module.

### Orientés chercheurs

#### Typologie des comportements d’échantillonnage

Création d’une typologie des utilisateurs sur la base de leur comportement d’échantillonnage : nature et nombre de ressources sautées. On peut orienter l’analyse sur la catégorisation des utilisateurs, on pourra s’intéressera à la distinction entre différents cas : celui où l’utilisateur réalise la quasi-totalité des activités prescrites et n’ignore que quelques-unes d’entre elles ; celui où l’utilisateur ne réalise qu’une minorité des activités prescrites. On pourra identifier le premier pattern comme « skipping », et le second comme « cherry-picking ». On pourra définir les utilisateurs comme skippers ou cherry-pickers sur la base de ces patterns. On peut chercher à identifier selon une typologie d’utilisateurs identifiée (skipper, cherry-picker par exemple) les scores d’échantillonnage de telle ou telle ressource.

## Inputs

### Flat

### logdata

Données de logs, où l’on a défini la fenêtre temporelle d’intérêt

id | user_id | ressource_id| viewed_date | ...
---|-------- | -----------|-------- | ---
identifiant unique de la trace (int | identifiant unique d'un utilisateur |identifiant unique d'une ressource |  timestamp
1 | 123456 | vidéo S1.1|'2016-01-01'
2 | 123456 | vidéo S1.2|'2016-01-01'
3 | 123456 | vidéo S1.4|'2016-01-01'
3 | 489456 | vidéo S1.1|'2016-01-01'

### Séquence pédagogique

L’analyste a besoin pour réaliser ce travail de connaître de manière précise la séquence pédagogique prescrite. Un travail de nettoyage de la séquence peut avoir été réalisé en amont par l’analyste pour filtrer des éléments qui ne doivent pas être pris en compte dans la séquence prescrite. Par exemple, on peut retirer dans une séquence de vidéos une vidéo n’ayant pas une visée pédagogique (vidéo d’animation: présentation d’un module, etc) pour ne conserver que les vidéos pédagogiques à proprement parler car l’on sait que la plupart des utilisateurs sautent la vidéo d’animation, ce qui risque de biaiser la détection des “skippers” proprement dits.

prescribed_sequence_of_interest

Séquence pédagogique sur laquelle doit être réalisée l’analyse. Contient l’identifiant et l’ordre des ressources.

order | ressource_id|
---|-------- |
Ordre dans la séquence | identifiant unique d'une ressource
1 | vidéo S1.1 |
2 | vidéo S1.2 |

### xApi

* event name 1
* event name 2
* event name 3
* ...

## Outputs

### user_video_mat

Matrice binaire 1/0. Tableau avec en ligne les utilisateurs, en colonne les ressources de la sequence_of_interest, prenant la valeur 1 quand une activité a été évitée par un utilisateur

user_id | ressource 1| ressource 2 | ...
------- | -----------|-------- | ---
123456 | 0|0
123457 | 1|0

### resource_skipping_score

Identification des activités les plus fréquemment évitées par les utilisateurs, avec un rang et un score pour chaque ressource. Exemple : proportion des certifiés ayant évité la ressource.

ressource_id | score d'échantillonnage|
---|-------- |
vidéo S1.1 | 0.58
vidéo S1.2 |0.41

### user_skipping_score

Calculer un score pour chaque utilisateur en fonction de sa propension à sauter une ressource

user_id | score d'échantillonnage|
---|-------- |
123456 | 0.05
123457 |0.51

## Indicateurs recommandés

Indicateur 1 : Proportion des utilisateurs évitant plus de 10% des ressources prescrites

Indicateur 2 : Proportion des utilisateurs évitant plus de 80% des ressources prescrites

# Exemples

### Données factices

[Données factices] (Link)

### Cas d'étude Factice

L'étude factice est constitué de mille cours avec des niveaux d'hybridations et des durées différentes. L'étude est de montrer le niveau d'hybridation de chaque cours et comparer le nombre d'heure magistrale et le nombre d'heure sur MOOCs.

[Algorithme Python permettant de réaliser la base de données factice] (LINK)

resource_skipping_score
![Exemple de visualisation](https://cloud.githubusercontent.com/assets/4588154/15217738/2ed06e3a-185d-11e6-9548-2f1d8a6060d4.png)

## Bibliographie


## Légitimation de l'analyse
