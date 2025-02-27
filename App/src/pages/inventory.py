import flet as ft
from flet_route import Params, Basket


class Inventory:
    def view(self, page: ft.Page, params: Params, basket: Basket):
        page.title = "Инвентаризация"


        return ft.View(
            "/",
            controls=[
                ft.Text("Инвентаризация"),
                ft.ElevatedButton("Back", on_click=lambda _: page.go("/")),
            ],
        )