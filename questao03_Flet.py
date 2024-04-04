import flet as ft

def main(page: ft.Page):
  a1 = ft.CircleAvatar(
      foreground_image_url="https://avatars.githubusercontent.com/u/142633846?s=400&u=c4f66a6167ec99165b54ca1598ba836c95ed4ae1&v=4",
      content=ft.Text("FF"),
      max_radius=100  
)
  nome_maquina = ft.TextField(
        label= ("Informe o nome da máquina: "),
        width=222,
        height=55,
    )

  tempo_uso = ft.TextField(
        label= ("Informe o tempo de uso: "),
        width=222,
        height=55,
    )

  ligado = ft.TextField(
        label= ("Informe se está ligado (Sim - Não): "),
        width=222,
        height=55,
    )

  msg1 = ft.Text("")
  msg2 = ft.Text("")
  msg3 = ft.Text("")
    
  def btn_click(e):
        msg1.value = nome_maquina.value
        nome_maquina.value = ""

        msg2.value = tempo_uso.value
        tempo_uso.value = ""

        msg3.value = ligado.value
        ligado.value = ""
        page.update()

  btn = ft.ElevatedButton(
        "ADICIONAR",
        width=222,
        height=55,
        on_click=btn_click
    )
  page.horizontal_alignment="CENTER"
  page.vertical_alignment="CENTER"

  page.add(a1, nome_maquina, tempo_uso, ligado, btn, msg1,msg2,msg3)

ft.app(target=main)