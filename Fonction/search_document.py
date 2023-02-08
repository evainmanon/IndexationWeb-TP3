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

def search_document_word(word, index):
    try :
        list_doc = dico_keys(index[word])
    except KeyError:
        list_doc = []
    return list_doc

def sort_list(list, nb_document):
    new_list = [] 
    for i in list : 
        if i not in new_list: 
            if int(i) <= nb_document :
                new_list.append(i) 
    return new_list

def search_document(token, index, nombre_document, filtre):
    if filtre == "ET":
        list_ind_doc = [str(i) for i in range(0, nombre_document + 1)]
        for word in token :
            list_doc = search_document_word(word, index)
            list_ind_doc = crossing_list(list_doc, list_ind_doc)
        list_ind_doc = sort_list(list_ind_doc, nombre_document)
    elif filtre == "OU":
        list_ind_doc = []
        for word in token :
            list_doc = search_document_word(word, index)
            list_ind_doc += list_doc
        list_ind_doc = sort_list(list_ind_doc, nombre_document)
    else : 
        print("Le filtre affiché n'est pas correcte")
        list_ind_doc = []
    return list_ind_doc
    
def print_title_doc(list_documents, liste_ind):
    liste_title = []
    for doc in list_documents:
        id = str(doc['id'])
        if tokeniz.search_word(id, liste_ind) != -1:
            liste_title.append({'url' : doc['url'], 'title' :doc['title']})
    return liste_title
