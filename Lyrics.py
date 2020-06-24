import urllib
import requests
from urllib import request

def pegarLetraMusica(artista, titulo):

    url = 'https://api.lyrics.ovh/v1/'+ artista +'/' + titulo
    # aqui ocorre a conexão com a API
    try:
        resposta = urllib.request.Request(url)
        # aqui a API é aberta com o response
        abrirApi = urllib.request.urlopen(resposta)
        conteudo = abrirApi.read().decode('unicode_escape')
    except request.HTTPError as err:
        #Caso haja um erro de conexão, irá mostrar aqui qual o código de
        #erro
        raise SystemError(err)

    return print(conteudo)

artista = input("Digite o nome do Artista: ")
artista = artista.replace(" ", "-")
titulo = input("Digite o nome da música: ")
titulo = titulo.replace(" ", "-")

pegarLetraMusica(artista,titulo)

fimDoCodigo = input("Aperte qualquer tecla para sair: ")
''' A linha de
código acima serve apenas para que o programa não feche sozinho após a
execução, caso você não esteja usando o Visual Studio Code. '''
