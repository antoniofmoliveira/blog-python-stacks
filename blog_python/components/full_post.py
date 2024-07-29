import reflex as rx

from ..model.post_model import Post
from ..navigation.routes import BLOG_POSTS_ROUTE
from ..state.state import State
from ..components import cards


def full_post() -> rx.Component:
    """
    Returns a full post component with details of the selected post.
    If no post is selected, returns a cards component.
    """
    # Get the selected post from the state
    post = State.post

    # Return the full post component
    return rx.cond(
        post,
        # Box containing the post details
        rx.box(
            # Post title
            rx.text(
                post.title,
                font_size="2rem",
                padding="5px",
                width="100%",
                text_align="center",
            ),
            # Row with post details
            rx.hstack(
                # Post date
                rx.text(
                    post.date,
                    width="25%",
                    text_align="center",
                ),
                # Post category
                rx.text(
                    f"categoria: {post.category}",
                    width="25%",
                    text_align="center",
                ),
                # Post views
                rx.text(
                    f"{post.qt_views} views",
                    width="25%",
                    text_align="center",
                ),
                # Close button
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
            # Row with post image and text
            rx.hstack(
                # Post image
                rx.image(
                    src=f"/images/{post.image}",
                    padding="10px",
                    margin_top="15px",
                    width="250px",
                    height="250px",
                    cursor="zoom_in",
                ),
                # Post text
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
            # Set component properties
            width="85%",
            min_width="400px",
            height="95%",
            display="block",
        ),
        # Return cards component if no post is selected
        cards(),
    )
