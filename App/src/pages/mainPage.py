import flet as ft
from flet_route import Params, Basket


class MainPage:
    def view(self, page: ft.Page, params: Params, basket: Basket):
        page.title = "Main Page"


        return ft.View(
            "/",
            controls=[
                ft.Text("Main Page"),
                ft.ElevatedButton("Order", on_click=lambda _: page.go("/order")),
            ],
        )