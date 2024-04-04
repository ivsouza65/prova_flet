import flet as ft

def main(page: ft.Page):
    # Cria uma lista para armazenar os elementos da tupla
    elementos = ("Eu", "Tu", "Ele")

    # Cria um Text para cada elemento da tupla
    for elemento in elementos:
        page.add(ft.Text(elemento))

ft.app(target=main)

#Essa tupla pode ser modificada? #NOTE Não, pois qualquer alteração da erro na tupla. 