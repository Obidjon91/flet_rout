import flet as ft

class Header(ft.Container):
    def __init__(self, page: ft.Page, text: str, btn_icon: ft.icons, btn_on_click=None):
        super().__init__(self)
        self.page = page
        self.btn_icon = btn_icon
        self.btn_on_click = btn_on_click
        self.bgcolor = "blue"
        self.padding = ft.padding.only(left=10, right=10, top=0, bottom=0)
        self.content = ft.Row(
            controls=[
                ft.Container(
                    expand=True,
                    content=ft.Text(text, size=16, weight="bold", color="white")
                ),
                ft.Container(
                    expand=False,
                    content=ft.IconButton(
                        icon=self.btn_icon,
                        icon_color="white",
                        on_click=self.btn_on_click,
                    )
                ),
            ]
        )