import reflex as rx
from ..model.post_model import Post
from ..navigation.routes import BLOG_POSTS_ROUTE
from ..state.state import State


def full_post() -> rx.Component:
    post = State.post
    return rx.box(
        rx.text(
            post.title,
            font_size="2rem",
            padding="5px",
            width="100%",
            text_align="center",
        ),
        rx.hstack(
            rx.text(
                post.date,
                width="25%",
                text_align="center",
            ),
            rx.text(
                f"categoria: {post.category}",
                width="25%",
                text_align="center",
            ),
            rx.text(
                f"{post.qt_views} views",
                width="25%",
                text_align="center",
            ),
            rx.link(
                "Fechar",
                width="25%",
                text_align="center",
                color="blue",
                _hover={
                    "cursor": "pointer",
                    "color": "red",
                },
                href=BLOG_POSTS_ROUTE,
            ),
            display="flex",
            margin_top="20px",
            width="100%",
        ),
        rx.hstack(
            rx.image(
                src=f"/images/{post.image}",
                padding="10px",
                margin_top="15px",
                width="250px",
                height="250px",
                cursor="zoom_in",
            ),
            rx.text(
                post.text,
                display="flex",
                font_size="1.5rem",
                padding="50px",
                padding_top="10px",
                width="92%",
                text_align="justify",
            ),
        ),
        # position="absolute",
        width="85%",
        min_width="400px",
        height="95%",
        # top="100px",
        # left="100px",
        display="block",
    )
