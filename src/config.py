import flet as ft

def configuracao(page: ft.Page):
    page.title = ' Configurção de pagina'
    page.theme_mode = ft.ThemeMode.DARK
    page.window.width = 500
    page.window.height = 500
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window.resizable = True