from PySimpleGUI import PySimpleGUI as sg

sg.theme('DarkPuple4')


layout = [
    [sg.Text('Insira o número de convidados'), sg.Input(key='convidado', size=(10, 3))], #layout
    [sg.Button('Confirmar')]
]

janela = sg.Window('Menu', layout)

while True:
    acao, valor = janela.read()
    numero = valor['convidado']
    if acao == sg.WINDOW_CLOSED:
        break
    if acao == 'Confirmar':
        print("----- LISTA DE CONVIDADOS -----")
        for i in range(1, int(numero)+1):
            nomes = input('nome do convidado: ')