import reflex as rx

from ..components import bar


def base_page(child: rx.Component, *args, **kwargs) -> rx.Component:
    if not isinstance(child, rx.Component):
        child = rx.heading("this is not a valid child element")

    return rx.container(
        rx.vstack(bar(), child, width="100%", padding="0px", margin="0px"),
        width="100%",
        padding="0px",
        margin="0px",
        size="4",
    )
