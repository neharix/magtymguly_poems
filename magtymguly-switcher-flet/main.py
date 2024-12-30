import flet as ft
from flet import (
    Column,
    FloatingActionButton,
    Icon,
    NavigationRail,
    NavigationRailDestination,
    Page,
    Row,
    Text,
    VerticalDivider,
    icons,
)

names = (
    "Gürgeniň",
    "Gerekdir",
    "Ýaşymyz",
    "Öňi-ardy bilinmez",
    "Gökleň",
    "Reýgan eýledi",
    "Pukaraýam",
    "Türkmen binasy",
    "Türkmeniň",
    "Depe nedir, düz nedir",
)


class Poem:
    def __init__(self, index: int):
        self.name = names[index]
        with open(f"poems/{index + 1}.txt", "r", encoding="utf-8") as file:
            self.content = file.read()

    def __str__(self):
        return self.name


poems = [Poem(index) for index in range(10)]


def main(page: Page):

    text_content = Text("Select poem")

    def select_poem(e):
        text_content.value = poems[e.control.selected_index].content
        page.update()

    rail = NavigationRail(
        selected_index=0,
        label_type="all",
        extended=True,
        min_width=100,
        min_extended_width=400,
        group_alignment=-0.9,
        destinations=[
            NavigationRailDestination(
                icon=icons.LIST_ALT_OUTLINED,
                selected_icon_content=Icon(icons.LIST_ALT_SHARP),
                label_content=Text(poems[i].name),
            )
            for i in range(10)
        ],
        on_change=select_poem,
    )

    page.title = "Magtymguly poetry"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.add(
        Row(
            [
                rail,
                VerticalDivider(width=1),
                Column([text_content], alignment="start", expand=True),
            ],
            expand=True,
        )
    )


ft.app(target=main)
