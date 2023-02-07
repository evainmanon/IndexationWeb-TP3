import Fonction.tokenize as tokeniz

def dico_keys(dico):
    keys = []
    for key in dico.keys():
        keys.append(key)
    return keys

def search_num(num, list): 
    ind = -1 
    if list == []:
        return -1
    else:
        for i in range (0, len(list)):
            if list[i] == num:
                ind = i 
        return ind 

def crossing_list(list1, list2):
    list = []
    for num in list1:
        if search_num(num, list2) != -1:
            list.append(num)
    return list 

def search_document(token, index, nombre_document):
    list_ind_doc = [str(i) for i in range(0, nombre_document + 1)]
    for word in token : 
        try :
            list_doc = dico_keys(index[word])
            list_ind_doc = crossing_list(list_doc, list_ind_doc)
        except KeyError: 
            return "Aucun document ne comporte tous les tokens"
    if list_ind_doc == [ ]: 
        return "Aucun document ne comporte tous les tokens"
    else :
        return list_ind_doc
    
def print_title_doc(list_documents, liste_ind):
    liste_title = []
    for doc in list_documents:
        id = str(doc['id'])
        if tokeniz.search_word(id, liste_ind) != -1:
            liste_title.append({'url' : doc['url'], 'title' :doc['title']})
    return liste_title
