import Fonction.search_document as search

liste_titre_essai = ["Titre","Titre numero", "Essai", "Coucou Coucou Aurel", "Essai"]

def list_word(request) : 
    liste_word = []
    i = 0
    list_esp = [0]
    for i in range (0, len(request)): 
        if request[i] == " ":
            list_esp.append(i)
    list_esp.append(len(request))
    liste_word.append(request[list_esp[0]:list_esp[1]])
    for k in range(1, len(list_esp)-1): 
        if request[list_esp[k]+1:list_esp[k+1]] != '':
            liste_word.append(request[list_esp[k]+1:list_esp[k+1]])
    return liste_word

def search_word(word, list): 
    ind = -1 
    if list == []:
        return -1
    else:
        for i in range (0, len(list)):
            if list[i] == word:
                ind = i 
        return ind 

def token_request(request):
    list_token = []
    list_word_request = list_word(request)
    for word in list_word_request : 
        if search_word(word, list_token)==-1:
            list_token.append(word)
    return list_token

def token_title(title):
    list_token = []
    list_word_title = list_word(title)
    for word in list_word_title : 
        if search_word(word, list_token)==-1:
            list_token.append([word, 1])
        else:
            list_token[search_word(word, list_token)][1] += 1
    return list_token

def list_ind(title, word):
    liste_ind = []
    liste_word = list_word(title)
    for i in range(0, len(liste_word)): 
        if liste_word[i] == word:
            liste_ind.append(i)
    return liste_ind

def index_documents(liste_document):
    index = {}
    for document in liste_document:
        token_titre = token_title(document['title'])
        liste_cle = search.dico_keys(index)
        for token_word in token_titre:
            word = token_word[0]
            liste_indice = list_ind(document['title'], word)
            if search_word(word, liste_cle) == -1:
                index[word] = {}
                index[word][str(document['id'])] = liste_indice
            else :
                index[word][str(document['id'])] = liste_indice
    return index
