import flet as ft
from flet_route import Params, Basket


class MainPage:
    def view(self, page: ft.Page, params: Params, basket: Basket):
        page.title = "Main Page"


        return ft.View(
            "/",
            controls=[
                ft.Container(
                    expand=True,
                    bgcolor="#EC811CFF",
                    content=ft.Column(
                        # expand=True,
                        controls=[
                            ft.Text("Main Page"),
                            ft.ElevatedButton("Заказ", on_click=lambda _: page.go("/order")),
                            ft.ElevatedButton("Инвентаризация", on_click=lambda _: page.go("/inventory")),
                            ft.ElevatedButton("Поступление", on_click=lambda _: page.go("/entrance")),
                        ]
                    )
                ),

            ],
        )