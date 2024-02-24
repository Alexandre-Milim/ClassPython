import flet as ft


def main(page):
    field = ft.TextField(
        label="Enter your PhoneNumber:",
    )
    page.add(field)

ft.app(main)