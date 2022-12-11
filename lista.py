from PySimpleGUI import PySilmpleGUI as sg


lista_convidados = []


layout = [
    [sg.Text('Insira o número de convidados'), sg.Input(key='convidado')]
]
x = int(input("Entre com o numero de convidados: "))
for i in range(1, x+1):

    nome = input(f"Insira o nome do convidado {i}: ")
    lista_convidados.append(nome)
remove_nome_repetido = set(lista_convidados)
lista_final = tuple(remove_nome_repetido)

print("A lista de convidados é: ")
for i in range(len(lista_final)):
    print(lista_final[i])
