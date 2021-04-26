# Hybridation au sein d’un ensemble

## Description courte du scénario d'analyse

L'apprentissage d'un cours inclut de nombreuses activitées et  **requière une certaine pédagogie** pour favoriser la compréhension de celui-ci. Ainsi, des activités telles que le visionnage d'une vidéo, la réalisation d'un quiz peuvent intégrer une séquence pédagogique en ligne, alors que d'autres activités comme la participation à un débat, une présentation ne peuvent être réalisés qu'en présentiel. Il est intéressant de comprendre les facteurs qui réduisent **la total digitalisation** d'un module (ex: facteur technique, ou humain). L'object de ce package est de visualiser l'apport de digitaisation dans chaque cours à travers une  institution d'enseignements supérieurs comme l'université, les départements qui l'a composent et les enseignants qui y travaillent. Aussi, le public des cours en ligne étant plus large que son *public natif*, améliorer la digitalisation des cours peuvent améliorer leur popularité.

### Tag

Digitalisation, Ciblage

## Cas d’utilisation

### Orientés concepteurs

#### Identification des ressources exploitables

Parmi les cours proposés par les enseignants, de nombreuses ressources ne sont pas exploités à travers des cours en ligne. Un concepteur souhaite enrichir le contenu de son cours et améliorer la digitalisation de celui-ci. Il lui faut ainsi distinguer les ressources non exploitées et celles non exploitables.

#### Identification des niveaux de digitalisation

On cherche à identifier pour les durées de modules, la proportion de digitalisation de chacun. Des compréhensions possibles sont l'impossibilité de concevoir une grande digitalisation pour le module ou un manque d'implémation du module.

### Orientés administrateurs

#### Distinction au sein d'un groupe

La compréhension des niveaux de digitalisation peut se faire depuis de nombreux échellon (au seins de l'université, d'un département université, ou encore d'un individu) afin d'identifier les ressources qui peuvent être améliorer et possiblement implémenter dans des cours en ligne.

### Orientés chercheurs

Création d'une base de référents agrégés (ex: PRAGE/PRCE) et de leur niveau d'utilisation de ressources en ligne. On peut orienter l'analyse sur la catégorisation de ces référents/enseignants ou encore département, on pourra ainsi s'intéresser à la distinction entre différents cas: celui où l'enseignant utilise très peu de ressources en ligne, celui qui fournit autant de ressources en ligne que de cours magistraux et celui qui utilise plus de ressource en ligne que de cours magistraux. On pourra identifier le niveau de digitalisation des trois patternes respectifs comme «Faible», «Moyen» et «Fort».
Il est possible de chercher les référents avec la possibilité d'ajouter un plus grand nombre de ressources en ligne.

## Inputs

### Logdata

Définition des identifiants des départements universitaire, des référents (enseignants, PRAG/PRCE) et des cours et la temporalité

Departement_ID | Referent_ID  | Cours_ID | Année |
---------------|--------------|----------|-------|
Identifiant unique du département | Identifiant unique du réferent (enseignant) | Identifiant unique du cours | Année du cours |
1 | 10002 | 2035| 2019
1 | 10002 | 2036| 2019
1 | 10003 | 2037| 2019
2 | 10015 | 2520| 2019
3 | 10050 | 2540| 2019

### Niveau de digitalisation

L'analyste a besoin pour réaliser ce travail de connaître de manière exacte la durée de chaque cours/module et leur proporton d'implémentation en ligne. Un travail de nettoyage de la base de données peut avoir été réalisé en amont par l'analyste pour filtrer des cours, des référents ou départements précis ou encore une année. Par exemple, on peut retirer l'année 2020 qui a connu une augmentation inhabituel  de l'utilisation de cours en ligne afin de ne pas obtenir de résultats biaiser.

Base sur laquelle doit être réalisée l'analyse. Contient l'identifiant d'un cours, le temps d'un cours, la durée d'utilisation de cours en ligne et la durée des cours magistraux.

Cours_ID | Temps_Cours  | Temps_Cours_enLigne | Temps_Cours_Présentiel |
---------|--------------|-------------|---------------|
Identifiant unique du cours | Durée totale du cours (cours magistraux et cours en ligne inclut) | Durée totale des cours en ligne | Durée totale des cours magistraux en présentiel |
2030 | 35 | 5   | 30
2031 | 12 | 10  | 2
2032 | 50 | 40  | 10
2033 | 20 | 10  | 10
2034 | 90 | 60  | 30

## Outputs

### Ratio et pourcentage de digitalisation

Ratio compris entre 0 et 1 qui représente la durée totale d'utilisation des ressources en ligne par rapport à la durée totale du cours.
Pourcentage compris entre 0 et 100 qui représente la multiplication du ratio

Cours_ID | Digitalisation_Ratio | Digitalisation_Pourcentage
---------|----------------------|---------------------------|
Identifiant unique du cours | Ratio d'utilisation de ressources en ligne par rapport à la durée totale d'un cours | Pourcentage d'utilisation de ressources en ligne par rapport à la durée total d'un cours |
2030 | 0.14 | 14
2031 | 0.83 | 83
2032 | 0.80 | 80
2033 | 0.50 | 50
2034 | 0.67 | 67

### Niveau digitalisation

List de quatres valeurs représentant les quatres niveaux de digitalisation suivant: «Forte Digitalisation, «Moyenne-Forte Digitalisation, «Moyenne-Faible Digitalisation» et «Faible Digitalisation». Le niveau de digitalisation dépend du ratio/percentage décrit précèdemment.

Cours_ID | Digitalisation_Ratio | Digitalisation_Pourcentage| Niveau_Digitalisation
---------|----------------------|---------------------------|----------------------|
Identifiant unique du cours | Ratio d'utilisation de ressources en ligne par rapport à la durée totale d'un cours | Pourcentage d'utilisation de ressources en ligne par rapport à la durée total d'un cours | Niveau de digitalisation de chaque cours en fonction du ratio/pourcentage
2030 | 0.14 | 14 | Faible Digitalisation
2031 | 0.83 | 83 | Forte Digitalisation
2032 | 0.80 | 80 | Moyenne-Forte Digitalisation
2033 | 0.50 | 50 | Moyenne-Faible Digitalisation
2034 | 0.67 | 67 | Moyenne-Forte Digitalisation

## Indicateur recommandés

Indicateur 1: Proportion des cours avec moins de 20% d'utilisation de ressources en ligne

Indicateur 2: Proportion des cours avec plus de 80% d'utilisation de ressources en ligne

## Exemples

### Cas d'étude Factice

L'étude factice est divisé en trois partie.

1. Pourcentage de Digitalisation d'une Université en fonction de la durée de chaque cours sur une durée de huit années.
2. Pourcentage de Digitalisation de chaque Département d'une Université de 2017 à 2019.
3. Pourcentage de Digitalisation de chaque Enseignant des Départements respectifs; AGORA, LPTM et LT2D de 2017 à 2019.

#### Échelle Universitaire

La réalisation de cette partie peut être retrouver ci-dessous: \
[Factice Data Link](https://github.com/Dorian-rx/TeachingAnalytics/blob/706a491df81d3b6d986aa86a44203b7dfd7b25f8/Digitalization/Example/Data/Digitalization_perYear.csv) \
[Algorithme Python permettant de réaliser l'Étude](Digitalization\Example\University_Digitalization.py](https://github.com/Dorian-rx/TeachingAnalytics/blob/706a491df81d3b6d986aa86a44203b7dfd7b25f8/Digitalization/Example/University_Digitalization.py))

L'analyse du pourcentage de digitalisation de chaque cours à l'échelle universitaire nous permet d'obtenir la figure suivante:

![factice-data: Pourcentage de Digitalisation d'une Université en fonction de la durée de chaque cours](https://raw.githubusercontent.com/Dorian-rx/TeachingAnalytics/main/Digitalization/Example/Figures/Displot%20of%20the%20Digitalization%20per%20Interval%20of%20Course%20Duration.png)

Le graphique ci-dessus montre la fréquence des pourcentages de digitalisation de chaque cours en fonction de la durée de chaque cours. Cependant, cette analyse n'est pas assez ciblé n'offre que très peu d'interprétation.

#### Échelle Départementale

Un ciblage plus important sur chaque département d'une université est possible. La réalisation de cette partie peut être retrouver ci-dessous: \
[GitHub Factice Data Link](https://github.com/Dorian-rx/TeachingAnalytics/blob/706a491df81d3b6d986aa86a44203b7dfd7b25f8/Digitalization/Example/Data/Digitalization_perDepartment.csv) \
[Algorithme Python permettant de réaliser l'Étude](https://github.com/Dorian-rx/TeachingAnalytics/blob/706a491df81d3b6d986aa86a44203b7dfd7b25f8/Digitalization/Example/Departments_Digitalization.py)

L'analyse du pourcentage de digitalisation de chaque département d'une université nous permets d'obtenir la figure suivante:

![factice-data: Pourcentage de Digitalisation de chaque Département d'une Université de 2017 à 2019](https://raw.githubusercontent.com/Dorian-rx/TeachingAnalytics/main/Digitalization/Example/Figures/Barplots%20of%20the%20Digitalization%20per%20Department%20from%202017%20to%202019.png)

Le graphique ci-dessus montre le pourcentage de digitalisation de chaque département d'une université à travers trois ans (2017 à 2019). Nous pouvons observer une différence de digitalisation à travers les années de chaque départements. Cependant les pourcentages reste similaire à quelques départements, ansi, nous manquons encore d'information pour donner une interprétation intéressante.

#### Échelle Individuelle

Un ciblage encore plus important que précèdemment est un ciblage indivuduel concernant chaque enseignant d'un département. La réalisation de cette partie peut être retrouver ci-dessous: \
[GitHub Factice Data Link](https://github.com/Dorian-rx/TeachingAnalytics/blob/main/Digitalization/Example/Data/Digitalization_perDep_perTeacher.csv) \
[Algorithme Python permettant de réaliser l'Étude](https://github.com/Dorian-rx/TeachingAnalytics/blob/b771e09ab4099270463af3fd18035f9f7c2c228a/Digitalization/Example/Teacher_Digitalization.py)

L'analyse de la digitalisation de chaque enseignant d'un département nous permet d'obtenir la figure suivante:

factice-data: Hybridation par Enseignant
![factice-data: Pourcentage de Digitalisation de chaque Enseignant des Départements respectifs; AGORA, LPTM et LT2D de 2017 à 2019](https://raw.githubusercontent.com/Dorian-rx/TeachingAnalytics/main/Digitalization/Example/Figures/Barplots%20of%20the%20Digitalization%20per%20Teacher%of%20Department%20from%202017%20to%202019.png)

Le graphique ci-dessus montre l'évolution du pourcentage de digitalisation de chaque enseignant de trois départements universitaire (respectivement AGORA, LPTM, LT2D) de 2017 à 2019. Cette visualisation est la plus précise est nous permet de comprendre avec le graphique précèdent l'évolution au sein d'un département l'utilisation de ressources en ligne.

## Bibliographie
