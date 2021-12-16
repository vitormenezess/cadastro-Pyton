from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep


lista = list()
arq = 'vitorbarbosademenezes.txt'
if arquivoExiste(arq):
    print('arquivo existe')
else:
    print('Arquivo não encontrado')
    criaarArquivo(arq)
while True:
    resposta = menu()
    if resposta == 2:
       print('cadastro')
    elif resposta == 1:
        lerArquivo(arq)
    elif resposta == 3:
        break

