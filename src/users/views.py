import json
import requests
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    url = "http://homologacao.plataformatelessaude.ufrgs.br/graphql/"
    query = '''query{
        usuarioEspecifico(usuarioId:"1"){
          nome
          password
          email
        }
    }'''
    r = requests.post(url, json={'query': query})
    json_data = json.loads(r.text)
    data_dict = json_data['data']
    return HttpResponse(str(data_dict))
