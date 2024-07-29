import reflex as rx
from ..state import State

def bar() -> rx.Component:
    return rx.hstack(
        rx.box(
            rx.text(
                "Flora",
                font_size="3rem",
                padding=".5rem",
                color="gold",
                _hover={
                    "cursor": "pointer",
                    "color": "yellowgreen",
                },
                on_click=lambda: State.set_category(""),
                width="10rem",
            ),
        ),
        rx.box(
            rx.hstack(
                rx.text(
                    "Branco",
                    _hover={
                        "cursor": "pointer",
                        "color": "lawngreen",
                    },
                    on_click=lambda: State.set_category("branco"),
                ),
                rx.text(
                    "Amarelo",
                    _hover={
                        "cursor": "pointer",
                        "color": "lawngreen",
                    },
                    on_click=lambda: State.set_category("amarelo"),
                ),
                rx.text(
                    "Azul",
                    _hover={
                        "cursor": "pointer",
                        "color": "lawngreen",
                    },
                    on_click=lambda: State.set_category("azul"),
                ),
                rx.text(
                    "Panorama",
                    _hover={
                        "cursor": "pointer",
                        "color": "lawngreen",
                    },
                    on_click=lambda: State.set_category("panorama"),
                ),
                rx.text(
                    "Macro",
                    _hover={
                        "cursor": "pointer",
                        "color": "lawngreen",
                    },
                    on_click=lambda: State.set_category("macro"),
                ),
                justify_content="flex-end",
            ),
            align_item="flex-end",
            font_size="1.5rem",
            padding="1rem",
            padding_top="1.5rem",
            color="lightblue",
            margin_right="1.5rem",
        ),
        background_color="green",
        height="5rem",
        display="flex",
        grid_template_columns="5rem 80%",
        justify_content="space-between",
        width='100%',
        padding="0px",
        margin='0px'
    )
