import flet as ft
from myRouter.router import MyRouter

def main(page: ft.Page):
    MyRouter(page)


if __name__ == "__main__":
    ft.app(target=main, assets_dir="assets")

