# Hype-13 Teaching Analytics 

This project constitutes a report on the results and methodologies employed during an internship conducted in spring 2021 at IDHN, a research laboratory at the University of Cergy-Pontoise in France, for a project called "Hype-13"

## 1) Hype-13

In response to the urgency of the health crisis, universities had to adapt and implement fully remote or hybrid teaching to ensure pedagogical continuity. To support the success of teachers and students in these new techno-pedagogical setups, it is essential for universities to coordinate their efforts and pool their tools, resources, and scenarios to best meet the needs of users.

The HyPE-13 project (HYbridize and Share Teaching) led by a consortium of 12 French universities is among the winners of the call for proposals "Hybridization of Higher Education Training" under the Future Investment Program (PIA) of the National Research Agency (ANR). Edtech France and Anstia are also among the actors involved.

The consortium of establishments established within this project aims to work on the very question of hybridization to provide a common response to the needs of students and the educational community, while taking into account the coordination and production processes inherent in such setups (support for teachers, higher education pedagogical service, IT department, teacher repository).

## 2) Teaching Analytics

This repository is focused on the teaching analytics which refers to the process of collecting, analyzing, and interpreting data related to educational activities, particularly those involving teaching and learning. This data often includes information on student performance, engagement, learning outcomes, and interactions with instructional materials. Teaching analytics aims to provide insights into various aspects of teaching effectiveness, such as identifying areas where students may be struggling, assessing the impact of different instructional methods or interventions, and informing instructional decision-making to enhance learning outcomes. It often involves the use of technology platforms and data analysis tools to gather and analyze large volumes of data generated within educational settings. The ultimate goal of teaching analytics is to support educators in making data-informed decisions to improve the quality of teaching and learning experiences.

## 3) Structure
```bash
.
├── Connex_Teach
│   ├── Data
│   │   └── Ressources.csv
│   ├── Figures
│   │   ├── ConnexionsperJDS.png
│   │   ├── ConnexionsperPD-PDS.png
│   │   ├── ConnexionsperPDS.png
│   │   ├── TempsConnexionsperPD-PDS.png
│   │   └── TempsConnexionsperPDS.png
│   └── Programs
│       ├── Date_Teacher.py
│       └── clusterTram.rmd
├── Digit_Gend_Senrt_Uni
│   ├── Data
│   │   ├── Data-Names
│   │   │   └── French_Names_Lgh3378.csv
│   │   └── Digit_Gend_Senrt.csv
│   ├── Figures
│   │   ├── Barplots - Anciennete Departments Universite.png
│   │   ├── Barplots - Genre Departments Universite.png
│   │   ├── Barplots - Rprt Ancienneté Departments Universites.png
│   │   ├── Barplots - Rprt Ancienneté Universites.png
│   │   ├── Barplots - Rprt Digit Genre Departments Universite.png
│   │   ├── Barplots - Rprt Digit Genre Departments Universites.png
│   │   ├── Barplots - Rprt Digit Genre Universites.png
│   │   ├── Barplots - Rprt Genre Departments Universites.png
│   │   ├── Barplots - Rprt Genre Universites.png
│   │   ├── Barplots - Rprt RessDigit Universites.png
│   │   ├── Barplots - Rprt RessSeniority Universites.png
│   │   └── Heatmap - Prct Digit Départements Universités.png
│   └── Programs
│       ├── Digit_Gend_Senrt.py
│       └── Digit_Gend_Senrt_Viz.py
├── Digit_Ress_Seqs
│   ├── Data
│   │   ├── Data-Names
│   │   │   └── French_Names_Lgh3378.csv
│   │   ├── Prepared_Sequences.csv
│   │   ├── Resources.csv
│   │   ├── Resources_Digit_inClass.csv
│   │   └── Resources_Sequence.csv
│   ├── Figures
│   │   ├── Barplots - Prct Digit a Teacher Département Informatique 2016 à 2020.png
│   │   ├── Barplots - Rprt Prct Digit Teachers Département Informatique 2016 à 2020.png
│   │   ├── Boxplots - Rprt Pcrt Digit Département Informatique 2013 à 2020.png
│   │   ├── Heatmap - Prct Digit Département 2013 à 2020.png
│   │   ├── Sequences-Module_386-Teacher_VERDIN-Dept_History.png
│   │   ├── Sequences-Modules_11_41_80-Teacher_rspvly_GALLE_FAVRET_AMIRAULT-Dep_ComputerScience.png
│   │   └── Sequences-Modules_60_61_69-Teacher_Rogier-Dept_ComputerScience.png
│   └── Programs
│       ├── DigitRess_Viz.py
│       ├── Resources.py
│       ├── Seqs_Ress.rmd
│       └── Sequences.py
├── Digit_Réing
│   ├── Data
│   │   └── Quizzes.csv
│   ├── Figures
│   │   ├── Barplots - Rprt Slip and Guess per Type and Difficulty Level.png
│   │   ├── Heatmap - Prct Réussite Département 2015 à 2020.png
│   │   ├── Heatmap - Prct Réussite Département Mathématiques 2015 à 2020.png
│   │   ├── Seq-PR-Chap_2-Mod_3-Dep_Informatique-2015_2020.png
│   │   ├── Seq-PR_A-Chap_2-Mod_3-Dep_Informatique-2015_2020.png
│   │   ├── Seq-PR_T-Chap_2-Mod_3-Dep_Informatique-2015_2020.png
│   │   ├── Seq-P_R-Chap_2-Mod_3-Dep_Informatique-2015_2020.png
│   │   ├── Seq-P_R_A-Chap_2-Mod_3-Dep_Informatique-2015_2020.png
│   │   ├── Seq-P_R_PR-Chap_2-Mod_3-Dep_Informatique-2015_2020.png
│   │   ├── Seq-P_R_T-Chap_2-Mod_3-Dep_Informatique-2015_2020.png
│   │   └── Seq-P_R_T_A-Chap_2-Mod_3-Dep_Informatique-2015_2020.png
│   └── Programs
│       ├── Quizz.py
│       ├── Quizz_Viz.py
│       └── Seqs_Quizz.rmd
└── Digit_Univ_Flux
    ├── Figures
    │   ├── Flux_Ress_Uni_T.html
    │   ├── Flux_Ress_Uni_T.png
    │   ├── Heatmap - Prct Digit Universités 2013 à 2020.png
    │   ├── Sankey - Flux APs.html
    │   └── Sankey - Flux APs.png
    └── Programs
        ├── Chord.Rmd
        ├── Digit_Ress_Uni.py
        └── Flux_APs.py
```

