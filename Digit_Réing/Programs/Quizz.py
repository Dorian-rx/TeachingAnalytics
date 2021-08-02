########################
# Réingénierie de Quiz #        
########################

#Import the required packages.
import numpy as np
from numpy.lib.arraysetops import unique
import pandas as pd
import random
import time
import os
from math import *


#Set the initial time of the program
start_time = time.time()


#Define the path
keywords = ['Data', 'Data-Names', 'Figures', 'Programs'] #Define the name of each subfolder of the global directory path.
path_dir = os.path.dirname(__file__) #Find the directory path.
path_glob = os.path.dirname(path_dir) #Find the global directory path.

path_data = path_glob + '/' + keywords[0] + '/' 
path_data_names = path_data + keywords[1] + '/' 
path_figures = path_glob + '/' + keywords[2] + '/' 
path_programs = path_glob + '/' + keywords[3] + '/' 


#Initialize a pseudorandom number generator (seed) to preserve the same values randomly obtained after any execution
random.seed( 2021 ) #The seed does not need to be randomize.


######################
# Class and Function #
######################

#Function that return the type of the current quiz.
def Type_Quiz(prev_typequiz):
    rand_type = random.random()
    rand_choice = random.random()
    main_condition_type = [rand_type <= 0.75, rand_type >= 0.75]
    scnd_condition_type = [prev_typequiz == 'QCU' and 0 <= rand_choice < 0.40 or prev_typequiz == 'QCM' and 0.40 <= rand_choice < 0.80 or prev_typequiz == 'QROC' and 0.95 <= rand_choice or prev_typequiz == 'QO' and 0.95 <= rand_choice,
                           prev_typequiz == 'QCU' and 0.40 <= rand_choice <= 0.80 or prev_typequiz == 'QCM' and 0 <= rand_choice < 0.40 or  prev_typequiz == 'QROC' and 0.80 <= rand_choice < 0.95 or prev_typequiz == 'QO' and 0.80 <= rand_choice < 0.95,
                           prev_typequiz == 'QCU' and 0.80 <= rand_choice < 0.95 or prev_typequiz == 'QCM' and 0.80 <= rand_choice < 0.95 or prev_typequiz == 'QROC' and 0 <= rand_choice <= 0.40 or  prev_typequiz == 'QO' and 0.40 <= rand_choice < 0.80,
                           prev_typequiz == 'QCU' and 0.95 <= rand_choice or prev_typequiz == 'QCM' and 0.95 <= rand_choice or prev_typequiz == 'QROC' and 0.40 <= rand_choice <= 0.80 or  prev_typequiz == 'QO' and 0 <= rand_choice < 0.40]  
    scnd_choice_type = ['QCU', 'QCM', 'QROC', 'QO']
    choice_type = [prev_typequiz, np.select(scnd_condition_type, scnd_choice_type)]
    quizz_type = np.select(main_condition_type, choice_type)
    return quizz_type

#Function that return some variables related to the type, level and number of attempts of the quiz (such as the succes percentage, ect.).
def Level_Percent(type, level, success_ratio, attempts):
    #Define some conditions and associated values to determine the minimum amount of learners per Quiz.
    conditions_learners = [type == 'QCU', type == 'QCM', type == 'QROC', type == 'QO'] #Define the conditions that are the type of the quiz.
    choices_learners = [ceil(attempts/3), ceil(attempts/4), ceil(attempts/2.5), ceil(attempts/2)] #Define the values corresponding to the connditions.
    learners_verif = np.select(conditions_learners, choices_learners) #Select a value representing the minimum amount of learners and depending on the above conditions and values.

    #Define the attempts related variables.
    success_attempts = round((success_ratio * attempts)) #The number of successful attempts.
    failure_attempts = attempts - success_attempts #The number of unsuccessful attempts.
    true_prct = round(success_ratio * 100, 2) #The percentage of success (from the ratio defined above).
    
    #Define the number of learners and associated variables.
    verif = False  #Set the variable "verif" to False.
    learners = round(random.uniform(success_attempts, attempts)) #The number of learners between the number of successful attempts and the total number of attempts.
    while verif == False: #Loop to verify a condition.
        if learners >= learners_verif: #Check that the defined number of learners is above or equal to the minimum number of learners (defined above).
            verif = True
            avg_learners_attempts = round( attempts / learners, 2) #The average number of attempts per Learners.
            learners_success = success_attempts #The number of successful learners.
            learners_failure = learners - learners_success #The number of unsuccessful learners.
            learners_success_prct = round((learners_success / learners) * 100, 2) #The percentage of successful learners. (do not take into account all the attempts done per user to succed).
        else:
            learners = round(random.uniform(success_attempts, attempts)) #Redetermine the number of learners if the conditions was not verified.

   #Define some conditions and associated values to determine the slip, guess per Quiz
    conditions_sgb = [type == 'QCU' and level == 'Facile', type == 'QCU' and level == 'Moyen', type == 'QCU' and level == 'Difficile',
                      type == 'QCM' and level == 'Facile', type == 'QCM' and level == 'Moyen', type == 'QCM' and  level == 'Difficile',
                      type == 'QROC' and level == 'Facile', type == 'QROC' and level == 'Moyen', type == 'QROC' and  level == 'Difficile',
                      type == 'QO' and level == 'Facile', type == 'QO' and level == 'Moyen', type == 'QO' and  level == 'Difficile']
    choice_sgb = [ [round(random.uniform(0, 0.20), 2), round(random.uniform(0.75, 1), 2)], [round(random.uniform(0.20, 0.40), 2), round(random.uniform(0.40, 0.75), 2)], [round(random.uniform(0.40, 0.75), 2), round(random.uniform(0.20, 0.40), 2)],
                   [round(random.uniform(0, 0.20), 2), round(random.uniform(0.70, 1), 2)], [round(random.uniform(0.20, 0.50), 2), round(random.uniform(0.30, 0.70), 2)], [round(random.uniform(0.50, 0.80), 2), round(random.uniform(0.15, 0.30), 2)],
                   [round(random.uniform(0, 0.20), 2), round(random.uniform(0.40, 1), 2)], [round(random.uniform(0.20, 0.60), 2), round(random.uniform(0.25, 0.40), 2)], [round(random.uniform(0.60, 1), 2), round(random.uniform(0, 0.25), 2)],
                   [round(random.uniform(0, 0.20), 2), round(random.uniform(0.30, 1), 2)], [round(random.uniform(0.20, 0.75), 2), round(random.uniform(0.15, 0.30), 2)], [round(random.uniform(0.75, 1), 2), round(random.uniform(0, 0.15), 2)]]
    slip, guess,  = np.select(conditions_sgb, choice_sgb)
    b = np.nan #Define the difficulty (b) of the quiz

    #Return all the defined variables related to both learners and attempts.
    return learners, avg_learners_attempts, learners_success, learners_failure, learners_success_prct, success_attempts, failure_attempts, true_prct, slip, guess, b


#Function that return the predicted level of difficulty and correct level of difficulty of the Quiz. (for each type)
def TyLvL_PrdCct(dep):    
    level_choice = ['Difficile', 'Moyen', 'Facile'] #Define the values corresponding to the level.
    predict_successratio = random.random()

    if dep == 'Mathématiques':
        correct_successratio = round(random.uniform(0, 0.65), 2)
    else:
        correct_successratio = random.random()


    conditions_predict = [0 <= predict_successratio <= 0.35, 0.35 < predict_successratio < 0.65, 0.65 <= predict_successratio <= 1] #Define the conditions.
    conditions_correct = [0 <= correct_successratio <= 0.35, 0.35 < correct_successratio < 0.65, 0.65 <= correct_successratio <= 1] #Define the conditions.
    
    predict_level = np.select(conditions_predict, level_choice) #Select a value depending on the above conditions and values.
    correct_level = np.select(conditions_correct, level_choice) #Select a value depending on the above conditions and values.

    condition_score = [
        predict_level == 'Facile' and correct_level == 'Difficile',
        predict_level == 'Facile' and correct_level == 'Moyen' or predict_level == 'Moyen' and correct_level == 'Difficile', 
        predict_level == correct_level,
        predict_level == 'Difficile' and correct_level == 'Moyen' or predict_level == 'Moyen' and correct_level == 'Facile',
        predict_level == 'Difficile' and correct_level == 'Facile']
    choices_score = [-2, -1, 0, 1, 2]
    choices_string = ['Beaucoup plus Difficile', 'Plus Difficile', 'Meme Difficulté', 'Plus Facile', 'Beaucoup plus Facile']
    score, score_string = np.select(condition_score, choices_score), np.select(condition_score, choices_string),

    #Return the predicted level of difficulty, the correct level of difficulty, the score of the predicted/correct and associated string.
    return predict_level, correct_level, correct_successratio, score, score_string


#Function that execute the associated function to return the predict, correct level of difficulty and learners, attempts variables.
def TyLvl_ScsFlr(dep, type, attempts):
    #Execute the predict, correct level of difficulty function.
    predict_level, correct_level, success_ratio, score, score_string = TyLvL_PrdCct(dep)

    #Execute the learners, attempts function.
    learners, avg_learners_attempts, learners_success, learners_failure, learners_success_prct, success_attempts, failure_attempts, true_prct, slip, guess, b  = Level_Percent(type, correct_level, success_ratio, attempts)

    #Find if the quiz difficulty is correct or not
    adapte = 'Adapte' if 0.60 <= success_ratio <= 0.75 else 'Pas Adapte'
    
    #Return all the variables defined through the two previous functions
    return predict_level, correct_level, adapte, success_ratio, score, score_string, learners, avg_learners_attempts, learners_success, learners_failure, learners_success_prct, success_attempts, failure_attempts, true_prct, slip, guess, b


##################
# Build the Data #
##################

#Define the list of years
temp_Years = [year for year in range(2015, 2021)] #Append in a list, each year.
print('List of Years:', temp_Years) #Display the list of Years.

#Define the number of quizzes
number_Quizzes = random.randint(100, 1000) #Create a variable to represent the number of Quizzes.
print('Number of Quizzes:', number_Quizzes) #Display the number of Quizzes.

#Define the list of departements and their modules
depts_type = ['Droit', 'Économie', 'Marketing', 'Informatique', 'Mathématiques', 'Philosophie', 'Sociologie'] #Define a list of Departements
modules = [
    ["Histoire du Droit", "Introduction Historique au Droit", "Relations Internationales", "Proces et Institution Juridictionnelles", "Constitution de la Cinquieme Republique"], #Droit
    ["L'Economie et son Domaine", "La Representation de l'Activite Economique: Le Circuit Economique", "La Production", "Le Travail", "Le Capital et le Progres Technique"], #Economie
    ["Introduction a l'Etude du Langage", "Grammaire Lexicale Fonctionnelle", "Grammaire et Syntaxe", "Neologie", "Construction Morphologique"], #Marketing
    ["Generalites sur les Systeme Informatiques", "Les Logiciels", "Algorithme et Programmation", "Reseaux et Internet"], #Informatique
    ["L'Algèbre Linéaire", "Le Calcul d'Intégrale", "La Dérivation", "Les Séries Numériques", "La Géométrie Analytique"], #Mathematique
    ["Introduction a la Philosophie", "La Notion de Logique", "La Notion d'Ethique", "La Culture"], #Philosophie
    ["Les Differentes Approches de l'Economie", "Histoire de la Pensee Economique", "Travail, Emploi, Chomage", "Notions de Sociologie", "Sociologie Generale"],] #Sociologie

chapters = [
    [   ["La Grèce", "L'Italie"],
        ["L'Ancien Regime", "La Contestation du Regime Feodal", "La Crise de l'Ancien Regime", "La Revolution Francaise, l'Affirmation du Liberalisme", "L'Amenagement du Liberalisme"],
        ["Introduction", "Les Acteurs des Relations Internationales", "Les Grands Principes regissant les Relations Internationales"],
        ["Introduction", "La Trame de la Scene Judiciaire", "Le Theatre de la Scene Judiciaire"],
        ["La Cinquieme Republique, une Conception du Pouvoir", "Le Pouvoir Gouvernant", "Le Pouvoir Legislatif", "Le Controle de Constitutionnalite"],
    ], #Droit
    [   ["L'Objet de la Science Economique", "Les Grands Courants de la Pensee Economique", "Modele d'Organisation de la Societe et Systeme Economique"],
        ["Les Agents Economiques et leurs Operations", "Le Circuit Economique dans le Cadre National", "Les Interdependances Economiques entre les Nations"],
        ["La Notion de Production", "L'Importance de la Production Marchande et de la Production Non-Marchande", "Valeur Ajouee et Mesure de la Richesse", "Les Limites de la Mesure de la Production"],
        ["Les Aspects Quantitatifs et Qualitatifs du Travail", "La Productivite du Travail et la Notion de Capital Humain"],
        ["Le Capital et l'Investissement", "Le Capital: Aspect Physiques et Financiers", "Les Differents Types d'Investissement et le Poids de l'Investissement Immateriel", "Le Progres Technique - Nature et Role"],
    ], #Economie
    [
        ["La Nature du Langage", "La Semiotique", "La Morphologie", "La Phonetique", "La Phonologie", "La Syntaxe", "Le Developpement du Langage", "L'Apprentissage de la Langue Seconde", "La Sociolinguistique et la Dialectologie", "L'Amenagement Linguistique"],
        ["Les Traits Syntaxiques", "Les Fonctions", "Ecrire une Grammaire Lexicale Fonctionnelle", "Diversite des Fonctions Grammaticales"],
        ["Les Subordonnees", "La Coordination", "Le Statut des Pronoms"],
        ["Les Innovations Lexicales", "La Motivation Neologique", "La Creation Neologique", "Les Accidents Lexicaux"],
        ["Alterations", "Transferts", "Sens Predictible et Atteste"]  
    ], #Marketing
    [
        ["Definitions et Vocabulaire de Base", "Structure de l'Ordinateur", "Logiciels et Domaines d'Applicationd de l'Informatique"],
        ["Systeme d'Exploitation", "Traitement de Texte", "Les Tableurs"],
        ["Notion d'Algorithme", "Instruction de Base", "Les Langagues de Programmation"],
        ["Notion de Reseau Informatique"],
    ], #Informatique
    [   ["Sommes de Sous Espaces", "Sous Espaces Supplementaires", "Theoreme du Rang", "Projecteurs et Symetries", "Determination et Construction d'Applications Lineaires", "Calcul de Dimensions et Construction de Bases, utilisant de la Dualite"], 
        ["Les Divers Types d'Integrale", "Les Methodes Generales d'Integration", "Integration des Fractions Rationnelles", "Fonction Trigonometriques", "Integrales Abeliennes", "Quelques Exemples en Maple"],
        ["Derivee en un Point", "Derivee Globale", "Theroeme de Rolle et des Accroissements Finis", "La Fonction Exponentielle Complexe", "Derivees d'Ordres Superieurs", "Classe Cn par Morceaux", "Fonctions Reciproques", "Quelques Techniques de Calcul"],
        ["Espaces Prehilbertiens Reel ou Complexes", "Espaces Euclidiens", "Rappels et Complements sur le Groupe Orthogonal d'un Espace Euclidien", "Complement sur les Endomorphismes Autoadjoints d'un Espace Euclidien et les Matrices Symetriques"],
        ["Sur l'Utilisation de Maple", "Methodes Generales pour aborder un probleme de Geometrie Analytique", "Geometrie Plane"],
    ], #Mathematique
    [
         ["La Nature", "La Technique", "L'Oeuvre d'Art", "L'Histoire", "Le Droit", "La Raison", "La Verite", "La Conscience", "La Liberte"],
         ["Les Lois Logiques", "Les Raisonnements Valides", "Les Paradoxes", "La Notion du Modele", "Le Calcul des Sequents", "Le Theoreme de Completude"],
         ["La Recherche d'Ethique", "Libre Arbitre et Determinisme", "Ethique du Devoir et Ethique Religieuse"],
         ["Sentiments Croyance et Cultes Religieux", "Croyances Religieuses et Verite", "Religion et Morale"],
    ], #Philosophie
    [
        ["Comment l'Activite et la Science Economiques se detachent-elles de la Morale et de la Politique?", "Les Auteurs Classiques", "Les Auteurs Neoclassiques", "L'Analyse Marxiste", "La Pensee Economique de Keynes", "Les Insuffisances d'une Pensee purement Economique"],
        ["Introduction", "La Formation de la Pensee Economique jusqu'a Adam Smith", "La Conception Liberale de l'Economie", "L'Analyse Marxiste", "La Revolution Keynesienne"],
        ["Caracteristiques de l'Emploi et du Chomage", "Fonctionnement du Marche du Chomage dans les Theories Economiques", "Les Actions pour l'Emploi", "La Question du Travail"],
        ["Les Modernites", "Structure et Classes Sociales", "Organisation et Institution", "La Socialisation", "Au-dela de l'Idee de Societe"],
        ["Le Sociologue, la Sociologie et la Vie Sociale", "La Theorie Sociologique", "La Condition Moderne", "Les Debats Sociologiques Contemporains"],
    ],] #Sociologie

print('Number of Departement(s):', len(depts_type)) #Display the number of Departements.
print('List of Departements:', depts_type) #Display the list of Departements.

#Define the number of Quizzes per Departement
avg_quiz = round(number_Quizzes/len(depts_type)) #Find the average number of quizzes per Departement.
print('Average Number of Quizzes per Departement:', avg_quiz) #Display the average.

lst_quizz_depts = [] #Create a list representing the number of Quizzes per Departement.
temp_quizz = number_Quizzes #Create a temporal variable.
while sum(lst_quizz_depts) != number_Quizzes: #Create a loop that will continue until the sum of the quizzes per departement is the same as the number of quizzes
    for len_dep in range(0, len(depts_type)): #Create another loop to iterate the number of quizzes to each Departements.
        numb = round(random.uniform(avg_quiz*0.90, avg_quiz*1.1)) #Select to 10% of difference from the average.
        lst_quizz_depts.append(numb) #Append the number of quizzes into the list
    if sum(lst_quizz_depts) != number_Quizzes: #Verify if the sum of the list is different from the number of quizzes previously defined.
        lst_quizz_depts.clear() #Clear the list
print('List of Number of Quizzes per Departement:', lst_quizz_depts) #Display the number of Quizzes per Departement.


########################################
# Build and Implement the set of Lists #
########################################

#Define a multiple lists that correspond to information related to each quiz.
lst_year, lst_depts, lst_module_ID, lst_module_name, lst_chapter_ID, lst_chapter_title, lst_quiz_chapt, lst_quiz_ID, lst_quiz_type, lst_rank = [], [], [], [], [], [], [], [], [], []
lst_attempts, lst_success_attempts, lst_failure_attempts, lst_truepercent = [], [], [], []
lst_learners, lst_learners_success, lst_learners_failure, lst_learners_successprct, lst_avg_attempts, lst_success_ratio = [], [], [], [], [], []
lst_levelpredict, lst_levelcorrect, lst_adapte, lst_levelpc, lst_score, lst_levelstrng = [], [], [], [], [], []
lst_slip, lst_guess, lst_b = [], [], []

#Define some arrays of choices.
chap_percent = [1] * 4 + [2] * 5 + [3] * 5 + [4] * 5 + [5] * 8 + [6] * 10 + [7] * 15 + [8] * 10 + [9] * 10 + [10] * 8 + [11] * 5 + [12] * 5 + [13] * 5 + [14] * 4 #Array of Choice to determine the number of Quiz per chapter
quiztype_percent = ['QCU'] * 45 + ['QCM'] * 35 + ['QROC'] * 15 + ['QO'] * 5 #Array of Choice to determine the type of the Quiz
pred_level = ['Trop Facile'] + ['Facile']  + ['Adapte']  + ['Difficile'] +  ['Trop Difficile']  #Array of choice to determine the level of the Quiz
choices_score = [-2, -1, 0, 1, 2]
choices_string = ['Beaucoup plus Difficile', 'Plus Difficile', 'Meme Difficulté', 'Plus Facile', 'Beaucoup plus Facile']


#Define the number of Quizzes per Chapter and their ID.
for year in temp_Years: #Iterate for each year from the "temp_Years" list
    quiz_ID = 1 #Define the initial state of the Quizz ID (= 1)
    for dep, num_dep in zip(depts_type, range(len(depts_type))):
        module_ID = 1
        for module_name, num_module in zip(modules[num_dep], range(len(modules))):
            chapter_ID = 1
            for chapter_name in chapters[num_dep][num_module]:
                ins_chap = [quiz for quiz in range(0, len(lst_quiz_ID)) if lst_quiz_ID[quiz] == quiz_ID] if quiz_ID in lst_quiz_ID else []
                chapter_quiz = lst_quiz_chapt[ins_chap[-1]] if quiz_ID in lst_quiz_ID else random.choice(chap_percent)
                for rank_quiz in range(chapter_quiz):
                    ins = [quiz for quiz in range(0, len(lst_quiz_ID)) if lst_quiz_ID[quiz] == quiz_ID] if quiz_ID in lst_quiz_ID else []
                    #chapter_ID = lst_chapt_ID[ins_chap[-1]] if quiz_ID in lst_quiz_ID else chapter_ID

                    num_attempts = random.choice(list(range(round(lst_attempts[ins[-1]]*0.85), round(lst_attempts[ins[-1]]*1.15)+1))) if quiz_ID in lst_quiz_ID else  random.randint(5, 100)

                    if quiz_ID in lst_quiz_ID:
                        type_quiz = Type_Quiz(lst_quiz_type[ins[-1]])
                        if lst_adapte[ins[-1]] == "Adapte":
                            condition_score = [lst_adapte[ins[-1]] != "Adapte", lst_adapte[ins[-1]] != "Adapte", lst_adapte[ins[-1]] == "Adapte", lst_adapte[ins[-1]] != "Adapte", lst_adapte[ins[-1]] != "Adapte"]
                            correct_level = lst_levelcorrect[ins[-1]]
                            predict_level = lst_levelcorrect[ins[-1]]
                            score, score_string = np.select(condition_score, choices_score), np.select(condition_score, choices_string),
                            adapte = lst_adapte[ins[-1]]
                            success_ratio = lst_success_ratio[ins[-1]]
                            learners, avg_learners_attempts, learners_success, learners_failure, learners_success_prct, success_attempts, failure_attempts, true_prct, slip, guess, b  = Level_Percent(type_quiz, correct_level, success_ratio, num_attempts)    
                        else:
                            predict_level, correct_level, adapte, success_ratio, score, score_string, learners, avg_learners_attempts, learners_success, learners_failure, learners_success_prct, success_attempts, failure_attempts, true_prct, slip, guess, b = TyLvl_ScsFlr(dep, type_quiz, num_attempts)                     
                    else:
                        type_quiz = random.choice(quiztype_percent)
                        predict_level, correct_level, adapte, success_ratio, score, score_string, learners, avg_learners_attempts, learners_success, learners_failure, learners_success_prct, success_attempts, failure_attempts, true_prct, slip, guess, b = TyLvl_ScsFlr(dep, type_quiz, num_attempts)                     
                    pred_crct_level = str(predict_level) + ' / ' + str(correct_level)
                    
                    #Append the Lists
                    lst_quiz_ID.append(quiz_ID)
                    lst_year.append(year)
                    lst_depts.append(dep)
                    lst_module_ID.append(module_ID)
                    lst_module_name.append(module_name)
                    lst_chapter_ID.append(chapter_ID)
                    lst_chapter_title.append(chapter_name)
                    lst_quiz_chapt.append(chapter_quiz)
                    lst_quiz_type.append(type_quiz)
                    lst_attempts.append(num_attempts)
                    lst_learners.append(learners)
                    lst_avg_attempts.append(avg_learners_attempts)
                    lst_learners_success.append(learners_success)
                    lst_learners_failure.append(learners_failure)
                    lst_learners_successprct.append(learners_success_prct)
                    lst_success_attempts.append(success_attempts)
                    lst_failure_attempts.append(failure_attempts)
                    lst_truepercent.append(true_prct)
                    lst_levelpredict.append(predict_level)
                    lst_levelcorrect.append(correct_level)
                    lst_adapte.append(adapte)
                    lst_levelpc.append(pred_crct_level)
                    lst_success_ratio.append(success_ratio)
                    lst_score.append(score)
                    lst_levelstrng.append(score_string)
                    lst_slip.append(slip)
                    lst_guess.append(guess)
                    lst_b.append(b)
                    lst_rank.append(rank_quiz + 1)

                    quiz_ID += 1
                chapter_ID += 1
            module_ID += 1


#######################
# Build the DataFrame #
#######################



#Define the First DataFrame
Quizzes_db = pd.DataFrame({ 'Year': lst_year,
                            'Departement': lst_depts,
                            'Module_ID': lst_module_ID,
                            'Module': lst_module_name,
                            'Chapter_ID': lst_chapter_ID,
                            'Chapter': lst_chapter_title,
                            'Quiz_perChapter': lst_quiz_chapt,
                            'Quizz_ID': lst_quiz_ID,
                            'Rank_onChapter': lst_rank,
                            'Quizz_Type': lst_quiz_type, 
                            'Slip': lst_slip,
                            'Guess': lst_guess,
                            'Success_Prct': lst_truepercent,
                            'Success_Attempts': lst_success_attempts,
                            'Failure_Attempts': lst_failure_attempts,
                            'Number_Attempts': lst_attempts,
                            'UniQ_Learner': lst_learners,
                            'Sucessful_Learners': lst_learners_success,
                            'Unsucessful_Learners': lst_learners_failure,
                            'Avg_Attempts': lst_avg_attempts,
                            'Percent_Learners_Success': lst_learners_successprct,
                            'Predict_Difficulty': lst_levelpredict,
                            'Correct_Difficulty': lst_levelcorrect,
                            'Score': lst_score,
                            'Difficulty_String': lst_levelstrng,
                            'Difficulty': lst_adapte,

}).sort_values(by = ['Quizz_ID', 'Year'], ascending = True)

Quizzes_db['Department'] = Quizzes_db['Departement'].replace(
                            ['Droit', 'Économie', 'Marketing', 'Informatique', 'Mathématiques', 'Philosophie', 'Sociologie'],
                            ['Law', 'Economy', 'Marketing', 'Computer Science', 'Mathematics', 'Philosophy', 'Sociology'])


print(Quizzes_db.head(5)) #Display the DataFrame.


#############
# Save Data #
#############

#Save the Quizzes DataFrame into a CSV File using the correct path.
Quizzes_db.to_csv(path_data + 'Quizzes.csv')


#####################
# Data Quizzes DONE #
#####################

Total_Time = round(time.time() - start_time)
print("Program Execution Time: %s seconds" % (Total_Time))