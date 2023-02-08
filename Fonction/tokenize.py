#Function which take a word and return this word with all his caracter lower
def lower_word(word) :
    new_word = ''
    for i in word :
        new_word = new_word + i.lower()
    return new_word

#Function which take a request and return a list with the word in the request
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

#Function which take a list and return the same list with all the word lower
def lower_list_word(list):
    new_list = []
    for word in list :
        new_list.append(lower_word(word))
    return new_list

#Function which search a word in a list.
#If the word is in the list, we return the place of the word in the list, else, we return -1
def search_word(word, list): 
    ind = -1 
    if list == []:
        return -1
    else:
        for i in range (0, len(list)):
            if list[i] == word:
                ind = i 
        return ind 

#Function which take a request and return the token of this request
def token_request(request):
    list_token = []
    list_word_request = lower_list_word(list_word(request))
    for word in list_word_request : 
        if search_word(word, list_token)==-1:
            list_token.append(word)
    return list_token