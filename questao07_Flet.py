"""import flet as ft

def main(page: ft.Page):
    # Cria um campo de texto para o nome do carro
    nome_tf = ft.TextField(label="Nome do carro:", max_lines=1)

    # Cria um campo de texto para a marca do carro
    marca_tf = ft.TextField(label="Marca do carro:", max_lines=1)

    # Cria um Text para exibir o carro criado
    page.update()

    # Adiciona os widgets à página
    page.add(nome_tf, marca_tf)

ft.app(target=main)"""

class Carro:
    def __init__(self, nome, marca):
        self.nome = nome
        self.marca = marca

    def __repr__(self):
        return f"Carro de Nome: {self.nome}, da Marca: {self.marca})"

