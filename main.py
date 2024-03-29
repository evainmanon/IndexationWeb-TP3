import Fonction.read_json as read
import Fonction.search_document as search
import Fonction.tokenize as tokeniz

file_documents = "documents.json"
number_of_doc = 500
filtre = "OU"
request = "Karine wikipéDia"

list_of_doc = read.part_list(read.read_json(file_documents), number_of_doc)
index_document = read.read_json("index.json")
list_document = search.search_document(tokeniz.token_request(request), index_document, len(list_of_doc), filtre)

liste_titre = search.print_title_doc(list_of_doc, list_document)

read.create_json(search.sort_list_dico(liste_titre, request),  "results.json")