#from PySimpleGUI import PySilmpleGUI as sg
from PySimpleGUI import PySimpleGUI as sg

sg.theme('DarkAmber')
lista_convidados = []

layout = [
    [sg.Text('Insira o número de convidados'), sg.Input(key='convidado')], #layout
    [sg.Button('Confirmar')]
        #for i in range(1, convidado+1):
    ]

janela = sg.Window('Menu', layout)

while True:
    acao, valor = janela.read()
    if acao == sg.WINDOW_CLOSED:
        break
    if acao == 'Confirmar':
        # if valor['covidado'] == 'convidar':
        for i in range(1, valor['convidado']):       
            remove_nome_repetido = set(lista_convidados)
            lista_final = tuple(remove_nome_repetido)
            print("----- LISTA DE CONVIDADOS -----")
            for i in range(len(lista_final)):
                print(lista_final[i])