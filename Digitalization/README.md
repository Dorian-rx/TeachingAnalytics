# Hybridation au sein d’un ensemble

## Description courte du scénario d'analyse

L'apprentissage d'un cours inclut de nombreuses activités et  **requière une précise pédagogie** pour favoriser la compréhension de celui-ci. Ainsi, des activités telles que le visionnage d'une vidéo, la réalisation d'un quiz peuvent intégrer une séquence pédagogique, alors que d'autres activités comme la participation à un débat, une présentation ne peuvent être réalisés qu'en présentiel. Il est intéressant de comprendre les facteurs qui réduisent **l'hybridation totale** d'un module (ex: facteur technique, ou humain). L'object de ce package est de visualiser d'un point de vue universitaire, départementale et individuel, l'apport d'hybridation dans chaque cours.
Le public d'un MOOC étant plus large que son *public natif*, améliorer l'hybridation des cours peuvent améliorer leur popularité.

### Tag

Hybridation, Ciblage

## Cas d’utilisation

### Orientés concepteurs

#### Identification des ressources exploitables

Parmi les cours proposés par les enseignants, de nombreuses ressources ne sont pas exploités à travers des MOOCs. Un concepteur souhaite enrichir le contenu de son cours et améliorer l'hybridation de celui-ci. Il lui faut ainsi distinguer les ressources non exploitées et celles non exploitables.

#### Identification des niveaux d'hybridation

On cherche à identifier pour les durées de modules, la proportion d'hybridation de chacun. Des compréhensions possibles sont l'impossibilité de concevoir une grande hybridation pour le module ou un manque d'implémation du module.

### Orientés administrateurs

#### Distinction au sein d'un groupe

La compréhension des niveaux d'hybridation peut se faire depuis de nombreux échellon (au seins de l'université, d'un département) afin d'identifier les ressources qui peuvent être améliorer et possiblement implémenter dans un MOOCs.

### Orientés chercheurs

Création d'une base de référents agrégés (ex: PRAGE/PRCE) et de leur niveau d'utilisation de ressources en ligne (MOOCs). On peut orienter l'analyse sur la catégorisation de ces référents/enseignants ou encore département, on pourra ainsi s'intéresser à la distinction entre différents cas: celui où l'enseignant utilise très peu de ressources en ligne, celui qui fournit autant de ressources en ligne que de cours magistraux et celui qui utilise plus de ressource en ligne que de cours magistraux. On pourra identifier le niveau d'hybridation des trois patternes respectifs comme «Faible», «Moyen» et «Fort».
Il est possible de chercher les référents avec la possibilité d'ajouter un plus grand nombre de ressources en ligne.

## Inputs

### Logdata

Définition des identifiants des départements, des référents (enseignants, PRAG/PRCE) et des cours et la temporalité

Departement_ID | Referent_ID  | Cours_ID | Année |
---------------|--------------|----------|-------|
Identifiant unique du département | Identifiant unique du réferent (enseignant) | Identifiant unique du cours | Année du cours |
1 | 10002 | 2035| 2019
1 | 10002 | 2036| 2019
1 | 10003 | 2037| 2019
2 | 10015 | 2520| 2019
3 | 10050 | 2540| 2019

### Niveau d'hybridation

L'analyste a besoin pour réaliser ce travail de connaître de manière exacte la durée de chaque cours/module et leur proporton d'implémentation en ligne. Un travail de nettoyage de la base de données peut avoir été réalisé en amont par l'analyste pour filtrer des cours, des référents ou départements précis ou encore une année. Par exemple, on peut retirer l'année 2020 qui a connu une augmentation inhabituel  de l'utilisation de MOOCs afin de ne pas obtenir de résultats biaiser.

Base sur laquelle doit être réalisée l'analyse. Contient l'identifiant d'un cours, le temps d'un cours, la durée d'utilisation de MOOCs et la durée des cours magistraux.

Cours_ID | Temps_Cours  | Temps_MOOCs | Temps_Lecture |
---------|--------------|-------------|---------------|
Identifiant unique du cours | Durée totale du cours (cours magistraux et MOOCs inclut) | Durée totale des cours en ligne (MOOCs) | Durée totale des cours magistraux |
2030 | 35 | 5   | 30
2031 | 12 | 10  | 2
2032 | 50 | 40  | 10
2033 | 20 | 10  | 10
2034 | 90 | 60  | 30

## Outputs

### MOOC_Ratio

Ratio compris entre 0 et 1 qui représente la durée totale d'utilisation des ressources en ligne par rapport à la durée totale du cours.

Cours_ID | MOOC_Ratio  |
---------|-------------|
Identifiant unique du cours | Ratio durée d'utilisation de resosurces en ligne par rapport à la durée totale d'un cours |
2030 | 0.14
2031 | 0.83
2032 | 0.80
2033 | 0.50
2034 | 0.67

### Niveau_Hybridation

List de quatres valeurs représentant les quatres niveaux d'hybridation suivant: «Forte Hybridation», «Moyenne-Forte Hybridation», «Moyenne-Faible Hybridation» and «Faible Hybridation». Celle-ci dépends des MOOC_Ratio.

Cours_ID | MOOC_Ratio  | Niveau_Hybridation
---------|-------------|-------------------|
Identifiant unique du cours | Ratio durée d'utilisation de resosurces en ligne par rapport à la durée totale d'un cours | List affichant le niveau d'hybridation de chaque cours |
2030 | 0.14 | Faible Hybridation
2031 | 0.83 | Forte Hybridation
2032 | 0.80 | Moyenne-Forte Hybridation
2033 | 0.50 | Moyenne-Faible Hybridation
2034 | 0.67 | Moyene-Forte Hybridation

## Indicateur recommandés

Indicateur 1: Proportion des cours avec moins de 20% d'utilisation des ressources en ligne

Indicateur 2: Proportion des cours avec plus de 80% d'utilisation de ressources en ligne

## Exemples

### Cas d'étude Factice

L'étude factice est divisé en trois partie.

1. Le niveau d'hybridation de 21163 cours répartis entre 2011 et 2020. Cette partie montre l'hybridation de chaque cours à l'échelle universitaire.
2. Le niveau d'hybridation de 15 départements. Cette partie montre l'hybridation de chaque département.
3. Le niveau d'hybridation de 141 enseignants. Cette partie montre l'hybridation de chaque enseignant.

#### Échelle Universitaire

La réalisation de cette partie peut être retrouver ci-dessous: \
[GitHub Factice Data Link](https://github.com/Dorian-rx/TeachingAnalytics/blob/main/Hybridation/Example/Data/Hybridation_perYear.csv) \
[Algorithme Python permettant de réaliser l'Étude](https://github.com/Dorian-rx/TeachingAnalytics/blob/main/Hybridation/Example/Hybridation_perYear.py)

L'analyse de l'hybridation de chaque cours à l'échelle universitaire nous permet d'obtenir le nuage de point suivant avec un filtrage pour l'année 2019.

factice-data: Hybridation pour l'année 2019
![alt text](https://raw.githubusercontent.com/Dorian-rx/TeachingAnalytics/main/Hybridation/Example/Figures/Ndps%20sur%20le%20niveau%20d'hybridation%20pour%202019.png)

Le graphique ci-dessus nous montre le niveau d'hybridation de chaque cours et leur durée d'utilisation de ressources en ligne, leur durée de cours magistraux et leur durée totale. Cependant, cette analyse n'est pas assez ciblé et donc nous offre que très peu d'interprétation.

#### Échelle Départementale

Un ciblage plus important sur chaque département d'une université est possible. La réalisation de cette partie peut être retrouver ci-dessous: \
[GitHub Factice Data Link](https://github.com/Dorian-rx/TeachingAnalytics/blob/main/Hybridation/Example/Data/Hybridation_perDep_perTeacher.csv) \
[Algorithme Python permettant de réaliser l'Étude](https://github.com/Dorian-rx/TeachingAnalytics/blob/ef03f8671fc3599312f42c1fe4f3a3034a6d852e/Hybridation/Example/Hybridation_perDepartment.py)

L'analyse de l'hybridation de chaque département nous permet d'obtenir le barplot suivant qui affiche le nombre total d'heures de cours effectuées par chaque département et le temps d'utilisation de ressources en ligne et de cours magistraux.

factice-data: Hybridation par Département
![alt text](https://raw.githubusercontent.com/Dorian-rx/TeachingAnalytics/main/Hybridation/Example/Figures/Barplots%20sur%20le%20niveau%20d'hybridation%20par%20d%C3%A9partement.png)

Le graphique ci-dessus ne nous offre cependant pas une visibilité interresante car malgré une différence de temps de cours effectuées par chaque département due à la différence entre enseignant dans chaque département, nous avons un niveau hybridation par département moyennement-faible ou moyennement-forte.

#### Échelle Individuelle

Un ciblage encore plus important que départementale est un ciblage indivuduel concernant chaque enseignant. La réalisation de cette partie peut être retrouver ci-dessous: \
[GitHub Factice Data Link](https://github.com/Dorian-rx/TeachingAnalytics/blob/main/Hybridation/Example/Data/Hybridation_perDep_perTeacher.csv) \
[Algorithme Python permettant de réaliser l'Étude](https://github.com/Dorian-rx/TeachingAnalytics/blob/ef03f8671fc3599312f42c1fe4f3a3034a6d852e/Hybridation/Example/Hybridation_perTeacher.py)

L'analyse de l'hybridation de chaque enseignant nous permet d'obtenir les barplots suivant qui affiche le nombre d'heures de cours magistraux et le nombre d'heures d'utilisation de ressources en ligne effectuées.

factice-data: Hybridation par Enseignant
![alt text](https://raw.githubusercontent.com/Dorian-rx/TeachingAnalytics/main/Hybridation/Example/Figures/Barplots%20sur%20le%20niveau%20d'hybridation%20par%20enseignant.png)

Le graphique ci-dessus nous offre une visibilité à l'échelle individuelle et nous permet d'interprêter chaque comportement d'enseignant.

## Bibliographie

Romero, C. et al. (2008). Data mining in course management systems: Moodle case study and tutorial. Computers & Education, 51(1):368–384
