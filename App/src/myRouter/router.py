import flet as ft
from flet_route import Routing, path

from pages.mainPage import MainPage
from pages.order import Order, OrdersTest
from pages.inventory import Inventory
from pages.entrance import Entrance

class MyRouter:
    def __init__(self, page: ft.Page):
        self.page = page
        self.app_routes = [
            path(url="/", clear=True, view=MainPage().view),
            path(url="/order", clear=False, view=Order().view),
            path(url="/inventory", clear=False, view=Inventory().view),
            path(url="/entrance", clear=False, view=Entrance().view),
            path(url="/orders", clear=False, view=OrdersTest(page=self.page).view),
        ]

        Routing(
            page=self.page,
            app_routes=self.app_routes
        )
        self.page.go(self.page.route)

