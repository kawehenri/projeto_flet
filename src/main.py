import flet as ft


def main(page: ft.Page):
    counter = ft.Text("0", size=50, data=0, color="black") 

    def increment_click(e):
        counter.data += 1
        counter.value = str(counter.data)
        counter.update()

    # Alterando a cor do botão flutuante
    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.Icons.ADD,
        on_click=increment_click,
        bgcolor="green",  # Cor de fundo do botão
        color="white",    # Cor do ícone
    )
    
    page.add(
        ft.SafeArea(
            ft.Container(
                counter,
                alignment=ft.alignment.center,
            ),
            expand=True,
        )
    )


ft.app(main)

