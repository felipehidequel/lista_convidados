#from PySimpleGUI import PySilmpleGUI as sg
from PySimpleGUI import PySimpleGUI as sg

sg.theme('DarkAmber')
lista_convidados = []


layout = [
    [sg.Text('Insira o número de convidados'), sg.Input(key='convidado')], #layout
    [sg.Button('Confirmar')]
        #for i in range(1, convidado+1):
    ]
# #x = int(input("Entre com o numero de convidados: "))
# for i in range(1, convidado+1):

#     nome = input(f"Insira o nome do convidado {i}: ")
#     lista_convidados.append(nome)
# remove_nome_repetido = set(lista_convidados)
# lista_final = tuple(remove_nome_repetido)

# print("A lista de convidados é: ")
# for i in range(len(lista_final)):
#     print(lista_final[i])

janela = sg.Window('Menu', layout) # layout que define o nome na janela

while True:
    acao, valor = janela.read()
    if acao == sg.WINDOW_CLOSED: #fechamento da janela caso o usuario não queira insirir umvalor
        break
    if acao == 'Confirmar':
        #for i in range(1, valor['convidado'] + 1):
        for i in range(1, valor['convidado']+1):       
            remove_nome_repetido = set(lista_convidados)
            lista_final = tuple(remove_nome_repetido)
            print("----- LISTA DE CONVIDADOS -----")
            for i in range(len(lista_final)):
                print(lista_final[i])