import flet as ft
from flet_route import Routing, path

from pages.mainPage import MainPage
from pages.order import Order

class MyRouter:
    def __init__(self, page: ft.Page):
        self.page = page
        self.app_routes = [
            path(url="/", clear=True, view=MainPage().view),
            path(url="/order", clear=False, view=Order().view),

        ]

        Routing(
            page=self.page,
            app_routes=self.app_routes
        )
        self.page.go(self.page.route)
