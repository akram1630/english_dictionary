from django.shortcuts import render
from PyDictionary import PyDictionary
################################
from rest_framework.decorators import api_view 
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
def index(request):
    return render(request, 'index.html')

def word(request):
    #from the <form> <input type="text" name="mySearch"................
    search = request.GET.get('mySearch') #String
    dictionary = PyDictionary()
    #meaning = dictionary.meaning(search)
    # synonyms = dictionary.synonym(search)
    # antonyms = dictionary.antonym(search)
    context = {
        #html file will take the key as a value:
       # 'meaning': meaning['Noun'][0],
        'synonyms': 'synonyms', 
        'antonyms': 'antonyms'
    }
    return render(request, 'word.html', context)
#########################################################
@api_view(['GET'])
def wordApi(request):
    data = request.data
    context = {
        #html file will take the key as a value:
       # 'meaning': meaning['Noun'][0],
        'synonyms': 'synonyms_API', 
        'antonyms': 'antonyms_API'
    }
    return Response({"definition":context})
    
   