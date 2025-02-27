import flet as ft
from flet_route import Params, Basket


class Order:
    def view(self, page: ft.Page, params: Params, basket: Basket):
        page.title = "Orders"


        return ft.View(
            "/orders",
            controls=[
                ft.Text("Orders"),
                ft.ElevatedButton("Back", on_click=lambda _: page.go("/")),
            ],
        )