# Importando as bibliotecas
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys


# Entrando no navagador e pesquisando o site
navegador = webdriver.Chrome()
navegador.get('https://web.whatsapp.com')
time.sleep(30)
contatos = [ 'Manu', 'Gleiton', 'Piriquitosvalda']
mensagem = 'Olá, sou um bot e estou em fase de testes. Não se preocupe! Fui criado pelo Kaio Victor e estou em fase de desenvolvimento!'

    # automação de buscar o contato e entrar na conversa 


def buscar_contato(contato):
    buscar_contato = navegador.find_element_by_xpath('//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]').click()
    navegador.find_element_by_xpath('//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]').send_keys(contato)
    time.sleep(1)
    navegador.find_element_by_xpath('//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]').send_keys(Keys.ENTER)

    # automação de enviar mensagem 
def enviar_mensagem(mensagem):
    navegador.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p').click()
    time.sleep(3)
    navegador.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p').send_keys(mensagem)
    time.sleep(3)
    navegador.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p').send_keys(Keys.ENTER)

    #loop 
for contato in contatos:

    buscar_contato(contato)

    enviar_mensagem(mensagem)


