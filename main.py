import Fonction.read_json as read
import Fonction.search_document as search
import Fonction.tokenize as tokeniz

file_json_url = "documents.json"
number_of_doc = 5
filtre = "ET"

list_of_doc = read.part_list(read.read_json(file_json_url), number_of_doc)
index_document = tokeniz.index_documents(list_of_doc)
list_document = search.search_document(tokeniz.token_request("Wikipédia"), index_document, len(list_of_doc))
liste_titre = search.print_title_doc(list_of_doc, list_document)

read.create_json(liste_titre, "results.json")