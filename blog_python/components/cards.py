import reflex as rx


from ..state import State
from .card import card


def cards() -> rx.Component:
    return rx.hstack(
        rx.foreach(State.posts, lambda post, index: card(post, index)),
        display="flex",
        flex_wrap="wrap",
        flex_direction="row",
        # padding="1rem",
        width="100%",
    )
