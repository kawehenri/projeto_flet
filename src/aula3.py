import config 
import flet as ft

def main(page:ft.Page):
    def adicionar(e):

        if not nova_tarefa.value:
            nova_tarefa.error_text = 'Por favor, digite seu nome!'
            page.update()

        else:
            nova_tarefa.error_text = None

        tarefa = ft.Row([])
        checkbox = ft.Checkbox(label=nova_tarefa.value)



        botao_remover = ft.IconButton(
            icon=ft.icons.DELETE_OUTLINED,
            tooltip= 'Remover tarefa',
            on_click=lambda e: remover_tarefa(tarefa)
        )

        tarefa.controls.extend((checkbox, botao_remover))
        
        page.add(tarefa)
        nova_tarefa.value = ''
        nova_tarefa.focus()
        nova_tarefa.update()




    def remover_tarefa(tarefa):
            page.controls.remove(tarefa)
            page.update()

            


    def saudacao(e):
        if not txt_nome.value:
            txt_nome.error_text = 'Por favor, digite seu nome'
            page.update()
        else:
            nome = txt_nome.value
            page.clean()
            page.add(ft.Text(f'Olá {nome}! '))

    txt_nome = ft.TextField(label='Seu nome?')
    page.add(ft.Row(
        [
            txt_nome, ft.ElevatedButton('Diga olá!', on_click=saudacao)
        ]
    ))

    nova_tarefa = ft.TextField(label='O que você deseja adicionar? ', width=300)
    page.add(ft.Row(
        [
            nova_tarefa,
            ft.ElevatedButton('Adicionar', on_click=adicionar)
        ]
    ))


    def clicar(e):
        ...
    saida_texto = ft.Text()
    btn_submit = ft.ElevatedButton(text='Enviar', on_click=clicar)
    cor_dropdown = ft.Dropdown(
        width=200,
        options=[
            ft.dropdown.Option('Red'),
            ft.dropdown.Option('Green'),
            ft.dropdown.Option('Blue'),
            ft.dropdown.Option('Minha opção')
        ]
    )

    page.add(saida_texto, btn_submit, cor_dropdown)

    def alterar_tema (e):
            if page.theme_mode == ft.ThemeMode.DARK:
                page.theme_mode = ft.ThemeMode.LIGHT
                btn_tema.icon = ft.icons.NIGHTS_STAY_OUTLINED
                btn_tema.tooltip = 'Alterar para tema escuro'
                page.bgcolor = ft.Colors.WHITE
            

            else:
                page.theme_mode = ft.ThemeMode.DARK
                btn_tema.icon = ft.icons.WB_SUNNY_OUTLINED
                btn_tema.tooltip = 'Alterar para tema claro'
                page.bgcolor = ft.Colors.BLACK
            page.update()

    btn_tema = ft.IconButton(
            icon=ft.icons.WB_SUNNY_OUTLINED,
            tooltip='Alterar o tema',
            on_click=alterar_tema
        )
    page.add(btn_tema)
ft.app(main)