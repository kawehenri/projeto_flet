import flet as ft

def main(page: ft.Page):
    page.title = ' Configurção de pagina'
    #page.bgcolor = ft.Colors.BLACK
    page.theme_mode = ft.ThemeMode.DARK

    #tamanho da janela
    page.window.width = 500
    page.window.height = 500

    #alinhamento
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    #page.padding = ft.padding.all(100)
    page.padding = ft.padding.only(top=10, left=20, right=50, bottom=10)
    page.spacing = 50
    page.window.always_on_top = False #coloca em primeiro ou em segundo plano
    page.window.title_bar_hidden = False # tira a barra de configuração de pagina
    page.window.full_screen = False # abrir em tela cheia

    def janela_evento(e):
        match e.data:
            case 'moved':
                print('Moveu a página')
            case 'resized':
                print('Redirecionou a página')
            case ' minimize':
                print( 'Minimizar a página')
            case '':
                print('Outra ação')

    page.window.on_event = janela_evento

    #limitando o tamanho da tela
    page.window.max_height = 600 
    page.window.min_height = 600
    page.window.max_height = 600 
    page.window.min_height = 600

    page.window.resizable = True

    def alterar_tema (e):
        if page.theme_mode == ft.ThemeMode.DARK:
            page.theme_mode = ft.ThemeMode.LIGHT
            btn_tema.icon = ft.icons.NIGHTS_STAY_OUTLINED
            btn_tema.tooltip = 'Alterar para tema escuro'
            page.bgcolor = ft.Colors.WHITE
            t.bgcolor = ft.colors.BLACK
            t.color = ft.colors.WHITE


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



#bloco de texto
    t = ft.Text(
        value='Kawê Henrique', # para passar o texto
        size=120, # para aumentar o tamanho do texto
        color=ft.Colors.WHITE, #para mudar a cor
        italic=True, #deixar o texto em italico
        weight= 'bold', #preencher o texto
        bgcolor= ft.Colors.BLACK, #mudar o fundo do app
        font_family= 'Calibri'
        )
    
    elementos = [
        ft.Text(value='Flamengo ', size=50, bgcolor=ft.colors.BLACK, font_family='Calibri'),
        ft.Text(value='Fifa ', size=50, bgcolor=ft.colors.BLACK, font_family='Calibri'),
        ft.Text(value='Neymar ', size=50, bgcolor=ft.colors.BLACK, font_family='Calibri'),
        ft.Text(value='Familia ', size=50, bgcolor=ft.colors.BLACK, font_family='Calibri')
    ]

    page.update() #atualizar a pagina
    page.add(ft.Text(value='Senai 2025', size=50, weight=30))
    page.add(t, btn_tema, *elementos) #adicionar 

ft.app(main)