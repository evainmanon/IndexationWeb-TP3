# TP 3 - Expansion de requête et ranking
EVAIN Manon 

## Éxecuter le code permettant d'enregistrer le fichier avec les url visités. 

#### 1. Cloner le dépot Git
Dans l'éditeur de code de votre choix, ouvrez le dossier dans lequel vous souhaitez enregistrer les fichiers pour le TP.  
Ouvrez par la suite un terminal. 

Vous pouvez alors écrire la ligne de code suivante :  

``git clone https://github.com/evainmanon/IndexationWeb-TP3.git``

#### 2. Exécuter le fichier main
Afin d'exécuter le fichier, c'est à dire d'obtenir un fichier texte comportant la liste des 50 sites trouvés grâce au crawler.  

Pour cela, vous pouvez écrire dans le terminal la ligne de code suivante : 

``python3 main.py``

*Les changements de paramètres* 
Afin d'exécuter ce crawler, vous pouvez faire le choix de changer deux paramètres. Ces derniers se trouvent dans le fichier main.py.   
- *file_documents* : Ce paramètre permet de donner le nom du fichier json contenant les différents documents à parcourir parmis lesquels vous souhaitez chercher lorsque vous rentrez une requête. Afin que l'éxécution du fichier **main.py** fonctionne, vous devez déposer le fichier .json dans le dossier du projet auparavant.   
- *number_of_docs* : Ce paramètre permet de déterminer le nombre de documents parmi lesquels vous souhaitez chercher lors de la requête. Si vous souhaitez avoir N documents, la recherche se fera sur les N premiers documents du fichier .json. Si le fichier possède moins de N documents, l'exécution du fichier **main.py** vous indiquera un message d'erreur contenant le nombre d'urls contenues dans le fichier.json.  
- *filtre* : Le paramètre *filtre* va permettre de choisir si vous souhaitez faire une recherche "ET" ou "OU". Si vous choisissez un filtre "ET", l'exécution du fichier **main.py** vous retournera la liste des documents qui contiennent l'ensemble des mots de la requête. En revanche, si vous choisissz un filtre "OU", l'exécution du fichier **main.py** vous retournera la liste des documents qui contiennent au moins un mot de la requête.  
- *request* : Ce paramètre permet à l'utilisateur de choisir la requête pour laquelle il souhaite chercher des documents. 

## Explication du code

#### 1. Architecture du code 
Le code est divisé en deux dossiers. un dossier *Index* qui contient l'ensemble des fichiers relatifs au fonctions permet de créer l'index. Le second dossier est le dossier *Tests*. Il permet de tester les fonctions présentent dans le fichier *Index*

#### 2. Explication des choix réalisés
Lors de l'exécution du fichier **main.py**, vous allez avoir dans votre dossier l'apparition d'un nouveau fichier .json. Ce fichier, **results.json**, comporte l'ensemble des documents qui ont survécu à la requête sous la forme :

``[{'url' : "url1", "title": "title1"}, {'url' : "url2", "title": "title2"}]``

Un exemple de ce fichier est présent dans ce projet, on le retrouve dans le document **results.json**, il a été excécuté pour les paramètres suivants :   
- *file_documents* = "documents.json"
- *number_of_doc* = 500
- *filtre* = "OU"
- *request* = "Karine wikipéDia"