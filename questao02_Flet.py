import flet as ft

def main(page: ft.Page):
  a1 = ft.CircleAvatar(
      foreground_image_url="https://avatars.githubusercontent.com/u/142633846?s=400&u=c4f66a6167ec99165b54ca1598ba836c95ed4ae1&v=4",
      content=ft.Text("FF"),
      max_radius=100  
)
  page.update()
  texto = ft.TextField(label="Digite o nome da pessoa: ",width=250,height=40)
  msg = ft.Text("Nome maiúsculo = ")

  def converte(e):
    msg.value = texto.value.upper()

    texto.value = ""

    page.update()

  btn = ft.ElevatedButton("Converte para maísculo", width=250,on_click=converte)
  
  page.horizontal_alignment = "CENTER"
  page.vertical_alignment = "CENTER"

  page. update()
  page.add(a1,texto,btn, msg)
ft.app(target=main)

