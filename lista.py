from PySimpleGUI import PySimpleGUI as sg

sg.theme('DarkPuple4')
lista_convidados = []

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
            remove_nome_repetido = set(lista_convidados)
            lista_final = tuple(remove_nome_repetido)
            for i in range(len(lista_final)):
                print(lista_final[i])