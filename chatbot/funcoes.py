
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

def buscar_contato(contato,driver):
    campo_pesquisa = driver.find_element_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    time.sleep(2)
    campo_pesquisa.click()
    time.sleep(1)
    campo_pesquisa.send_keys(contato)
    time.sleep(2)
    campo_pesquisa.send_keys(Keys.ENTER)

def enviar_mensagem(mensagem,driver):
    campo_mensagem = driver.find_elements_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    time.sleep(2)
    campo_mensagem[1].click()
    time.sleep(1)
    campo_mensagem[1].send_keys(mensagem)
    time.sleep(2)
    campo_mensagem[1].send_keys(Keys.ENTER)


def ler_arquivo(nome):
    try:
        a = open(nome,'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        lista=[]
        for linha in a:
            linha = linha.replace('\n','')
            lista.append(linha)
        return lista