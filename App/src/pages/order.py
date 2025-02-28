import flet as ft
from flet_route import Params, Basket

from utils.header import Header

class Order:
    def view(self, page: ft.Page, params: Params, basket: Basket):
        page.title = "Orders"

        return ft.View(
            "/orders",
            bgcolor="#E2DBD5FF",
            padding=0,
            controls=[
                Header(page=page, text="Orders", btn_icon=ft.icons.BACK_HAND, btn_on_click=lambda _: page.go("/")),
                ft.Text("Orders"),
                ft.ElevatedButton("Back", on_click=lambda _: page.go("/")),
            ],
        )
    


class OrdersTest(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__(route="/orders")
        self.page = page
        self.page.title = "Test"
        self.padding = 0
        self.bgcolor = "#E2DBD5FF"
        self.controls = [
            Header(page=self.page, text="Test", btn_icon=ft.icons.BACK_HAND, btn_on_click=lambda _: page.go("/")),
        ]

    def view(self, page: ft.Page, params: Params, basket: Basket):
        return self