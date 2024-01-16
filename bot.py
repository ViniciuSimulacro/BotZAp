import pywhatkit
import keyboard
import time
import win32clipboard
from lista import *

from datetime import datetime

import openpyxl

book = openpyxl.load_workbook('contatos.xlsx')
contacts = book['Contatos']
send_list = []
for rows in contacts.iter_rows(min_row=2):
    send_list.append([rows[0].value,rows[1].value])


contatos = []

for item in send_list:
    contatos.append(item)


msg_imagem = 'Olá, eu sou o Vinicius, muito prazer! Vi que vocês estão recrutando pessoas e gostaria de enviar meu currículo. Já trabalhei com atendimento ao cliente, bartender, copeiro, garçom, entre outras coisas que você pode ver no currículo. Estou a disposição para freelances aos fins de semana ou cobertura de folgas dos fixos, mas também busco uma vaga fixa. Caso haja interesse aguardo o contato para conversar. Obrigado pela atenção e tenha um ótimo dia de trabalho!'   
imagem = 'Vinicius Teixeira de Oliveira de Lucca - Curriculo.jpg'

while len(contatos)>= 1:
    telefone = contatos[0][0]
    #mensagem = f'Teste feito pelo Simulacro Web, gostou {contatos[0][1]}?'
    pywhatkit.sendwhats_image(contatos[0][0], imagem , msg_imagem,45)
    time.sleep(15)
    keyboard.press_and_release('ctrl + W')
    del contatos[0]

print('Missão completa!')