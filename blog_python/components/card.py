import reflex as rx

from ..model import Post
from ..navigation import BLOG_POSTS_ROUTE
from ..state import State


def card_title(text: str) -> rx.Component:
    return rx.text(
        f"{text[0:30]}...",
        color="black",
        width="90%",
        height="3rem",
        text_align="center",
        padding_top="1rem",
        padding_left="1rem",
        padding_right="2rem",
        size="1.5rem",
    )


def card_photo(file_path: str) -> rx.Component:
    return rx.image(
        src=f"/images/{file_path}",
        width="250px",
        height="250px",
        background_color="black",
        margin="1.5rem",
        border_radius="10%",
    )


def card_text(text: str) -> rx.Component:
    return rx.text(
        f"{text[0:80]}...",
        color="black",
        margin="1.5rem",
        size="1rem",
    )


def card_foot(date: str, category: str, views: int) -> rx.Component:
    return rx.box(
        rx.table.root(
            rx.table.body(
                rx.table.row(
                    rx.table.cell(
                        date,
                        color="black",
                        width="33%",
                        text_align="center",
                        size=".8rem",
                    ),
                    rx.table.cell(
                        f"Categoria: {category}",
                        color="black",
                        width="33%",
                        text_align="center",
                        size=".8rem",
                    ),
                    rx.table.cell(
                        f"{views} views",
                        color="black",
                        width="33%",
                        text_align="center",
                        size=".8rem",
                    ),
                ),
                width="100%",
            ),
        ),
        width="100%",
    )


def card(post: Post, index: int) -> rx.Component:
    return rx.fragment(
        rx.link(
            rx.card(
                card_title(post.title),
                card_photo(post.image),
                card_text(post.text),
                card_foot(post.date, post.category, post.qt_views),
                display="block",
                border="2px",
                box_shadow="5px 5px gray",
                border_radius="5%",
                width="300px",
                min_width="300px",
                height="500px",
                class_name=post.category,
                margin="1rem",
                _hover={
                    "cursor": "pointer",
                    "background-color": "cadetblue",
                },
                # on_click=CardState.set_post_id(post.id),
            ),
            href=f"{BLOG_POSTS_ROUTE}{post.id}",
        ),
        key=index,
    )
