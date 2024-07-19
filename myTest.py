from PyDictionary import PyDictionary
 
search = 'ok'
dictionary = PyDictionary()
#meaning = dictionary.meaning(search)# not working
synonyms = dictionary.synonym(search)
antonyms = dictionary.antonym(search)
print(search)