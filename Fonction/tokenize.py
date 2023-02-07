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

print(token_request("Karine Lacombe Lacombe"))
