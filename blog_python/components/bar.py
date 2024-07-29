import reflex as rx

from ..state import State


def bar() -> rx.Component:
    """
    Return a bar component containing the application's logo and category selection.
    The logo is a clickable text that sets the category to an empty string.
    The category selection is a row of clickable texts that sets the category to the corresponding string.
    """
    # Logo text
    logo_text = rx.text(
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
    )

    # Category selection texts
    category_texts = [
        rx.text(
            category,
            _hover={
                "cursor": "pointer",
                "color": "lawngreen",
            },
            on_click=lambda: State.set_category(category),
        )
        for category in ["Branco", "Amarelo", "Azul", "Panorama", "Macro"]
    ]

    # Category selection row
    category_row = rx.hstack(
        *category_texts,
        justify_content="flex-end",
    )

    # Bar component
    return rx.hstack(
        rx.box(logo_text),  # Logo
        rx.box(
            category_row,  # Category selection
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
        width="100%",
        padding="0px",
        margin="0px",
    )
