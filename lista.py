from PySimpleGUI import PySimpleGUI as sg

sg.theme('DarkGrey')


layout = [
    [sg.Text('Insira o número de convidados'), sg.Input(key='convidado', size=(10, 3))], #layout
    [sg.Button('Confirmar')]
]

janela = sg.Window('Menu', layout)

acao, valor = janela.read()
numero = int(valor['convidado'])
contador = 0
lista = []
while contador < numero:    
    if acao == sg.WINDOW_CLOSED:
        break
    if acao == 'Confirmar':        
        for i in range(1, numero+1):
            nomes = input(f'nome do convidado {i}: ')
            lista.append(nomes)      
    print("----- LISTA DE CONVIDADOS -----")
    for x in lista:            
        print(x)
        contador += 1
    break        
    