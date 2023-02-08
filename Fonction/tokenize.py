def lower_word(word) :
    new_word = ''
    for i in word :
        new_word = new_word + i.lower()
    return new_word

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

def lower_list_word(list):
    new_list = []
    for word in list :
        new_list.append(lower_word(word))
    return new_list

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
    list_word_request = lower_list_word(list_word(request))
    for word in list_word_request : 
        if search_word(word, list_token)==-1:
            list_token.append(word)
    return list_token