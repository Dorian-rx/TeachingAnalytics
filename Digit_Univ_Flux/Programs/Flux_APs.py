########################
# Flux des Enseignants #        
########################

#Import the required packages.
import plotly.graph_objects as go
import os
import time


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



##################
# Visualizations #
##################

##################################################
# 1° - Sankey
# Flux des Enseignants dans les Appels à Projets #
##################################################

fig = go.Figure(data=[go.Sankey(
  valueformat = ".0f",
    node = dict(
      pad = 10,
      thickness = 9,
      label = ["Ensemble du corps enseignant", "Appel à Projet 1", "Appel à Projet 2", "Appel à Projet 3"],
      color="#FF4C6B",
      hovertemplate='%{label} <extra></extra>',
    ),
    link = dict(
        source = [0, 0, 0, 1, 1, 2],
        target = [1, 2, 3, 2, 3, 3],
        value =  [75, 25, 30, 40, 15, 50]
  ))])
 
fig.update_layout(title={
        'text': "Flux des Enseignants dans les Appels à Projets",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'}, font_size = 24)

fig.update_layout(
    font_family="Times New Roman",
    title_font_family="Times New Roman",
)

fig.write_html(path_figures + "Sankey - Flux APs.html")

#fig.show()
