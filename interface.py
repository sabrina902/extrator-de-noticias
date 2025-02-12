import flet as ft
from banco import obter_titulos

def main(page: ft.Page):
    page.title = "Notícias Extraídas"
    page.scroll = "adaptive"

    titulos = obter_titulos()
    
    lista = ft.ListView(
        controls=[ft.Text(titulo) for titulo in titulos],
        expand=True
    )

    page.add(lista)
    page.update()

ft.app(target=main)
