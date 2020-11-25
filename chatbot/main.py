#Execute no terminal
#pip install selenium
#pip install webdriver_manager

from selenium import webdriver
import time
import funcoes
   
"""
#Executar no Google Chrome
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
"""

#Executar no Microsoft Edge
from webdriver_manager.microsoft import EdgeChromiumDriverManager
driver = webdriver.Edge(EdgeChromiumDriverManager().install())

arq_contato = 'lista_alunos.txt'
arq_mensagem = 'mensagem.txt'



#Abre whatsappweb no navegador
driver.get('https://web.whatsapp.com/')

#Espera a leitura manual do QRCODE
time.sleep(20)
while True:
    continua = input("Aguardando leitura do QR CODE, digite 'S' ao realizar.")
    if continua == 'S':
        break

#Lista de contatos onde a mensagem será enviada
contatos =  funcoes.ler_arquivo(arq_contato)
mensagem = funcoes.ler_arquivo(arq_mensagem)


for aluno in contatos:
    funcoes.buscar_contato(aluno,driver)
    for texto in mensagem:
        funcoes.enviar_mensagem(texto,driver)

