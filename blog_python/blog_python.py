import reflex as rx

from rxconfig import config

from .pages import grid_page, post_page


def index() -> rx.Component:
    """
    The index page component.

    Returns:
        The rendered component of the index page.
    """
    # This function returns the grid page component
    # which is the main page of the application.
    return grid_page()


style = {
    "*": {
        "padding": "0",
        "margin": "0",
        "vertical-align": "baseline",
        "list-style": "none",
        "border": "0",
    },
    "font_family": '"Franklin Gothic Medium", "Arial Narrow", Arial, sans-serif',
    ".branco": {"background_color": "whitesmoke"},
    ".amarelo": {"background_color": "lightyellow"},
    ".azul": {"background_color": "lightblue"},
    ".panorama": {"background_color": "lightgreen"},
    ".macro": {"background_color": "lightcyan"},
}

app = rx.App(style=style)
app.add_page(index)
