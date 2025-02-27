import flet as ft
from flet_route import Params, Basket


class Entrance:
    def view(self, page: ft.Page, params: Params, basket: Basket):
        page.title = "Поступление"

        return ft.View(
            "/",
            controls=[
                ft.Text("Поступление"),
                ft.ElevatedButton("Back", on_click=lambda _: page.go("/")),
            ],
        )