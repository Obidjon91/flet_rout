import flet as ft
from flet_route import Params, Basket

from utils.header import Header

class MainPage:
    def view(self, page: ft.Page, params: Params, basket: Basket):
        page.title = "Main Page"


        return ft.View(
            "/",
            bgcolor="#E2DBD5FF",
            padding=0,
            controls=[
                Header(page=page, vizable=False, text="Main Page", btn_icon=ft.icons.MENU, btn_on_click=lambda _: page.go("/")),
                ft.Container(
                    alignment=ft.alignment.Alignment(0.0, 0.0),
                    expand=True,
                    padding=10,
                    bgcolor="#888582FF",
                    content=ft.Column(
                        # expand=True,
                        controls=[
                            ft.ElevatedButton(
                                text="Заказ", 
                                expand=True, 
                                expand_loose=True,
                                on_click=lambda _: page.go("/orders")
                                ),
                            ft.ElevatedButton("Инвентаризация", on_click=lambda _: page.go("/inventory")),
                            ft.ElevatedButton("Поступление", on_click=lambda _: page.go("/entrance")),
                        ]
                    )
                ),

            ],
        )