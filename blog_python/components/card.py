import reflex as rx

from ..model import Post
from ..navigation import BLOG_POSTS_ROUTE
from ..state import State


def card_title(text: str) -> rx.Component:
    """
    Creates a card title component.

    Args:
        text (str): The text for the title.

    Returns:
        rx.Component: The card title component.
    """
    # Create the card title component with the specified text
    return rx.text(
        # Truncate the text to 30 characters and add ellipsis if longer
        f"{text[0:30]}...",
        # Set the text color to black
        color="black",
        # Set the width to 90% of the container
        width="90%",
        # Set the height to 3rem
        height="3rem",
        # Set the text alignment to center
        text_align="center",
        # Set the top padding to 1rem
        padding_top="1rem",
        # Set the left padding to 1rem
        padding_left="1rem",
        # Set the right padding to 2rem
        padding_right="2rem",
        # Set the font size to 1.5rem
        size="1.5rem",
    )


def card_photo(file_path: str) -> rx.Component:
    """
    Creates a card photo component.

    Args:
        file_path (str): The file path of the image.

    Returns:
        rx.Component: The card photo component.
    """
    # Create the card photo component with the specified file path
    return rx.image(
        # Set the source of the image to the specified file path
        src=f"/images/{file_path}",
        # Set the width to 250 pixels
        width="250px",
        # Set the height to 250 pixels
        height="250px",
        # Set the background color to black
        background_color="black",
        # Set the margin to 1.5rem
        margin="1.5rem",
        # Set the border radius to 10%
        border_radius="10%",
    )


def card_text(text: str) -> rx.Component:
    """
    Creates a card text component.

    Args:
        text (str): The text for the card.

    Returns:
        rx.Component: The card text component.
    """
    # Truncate the text to 80 characters and add ellipsis if longer
    # Set the text color to black
    # Set the margin to 1.5rem
    # Set the font size to 1rem
    return rx.text(
        f"{text[0:80]}...",
        color="black",
        margin="1.5rem",
        size="1rem",
    )


def card_foot(date: str, category: str, views: int) -> rx.Component:
    """
    Creates a card foot component.

    Args:
        date (str): The date for the card.
        category (str): The category for the card.
        views (int): The number of views for the card.

    Returns:
        rx.Component: The card foot component.
    """
    # Create the card foot component with the specified date, category, and views
    return rx.box(
        # Create a table with the specified rows and width
        rx.table.root(
            rx.table.body(
                rx.table.row(
                    # Create a table cell with the specified date, width, and text alignment
                    rx.table.cell(
                        date,
                        color="black",
                        width="33%",
                        text_align="center",
                        size=".8rem",
                    ),
                    # Create a table cell with the specified category, width, and text alignment
                    rx.table.cell(
                        f"Categoria: {category}",
                        color="black",
                        width="33%",
                        text_align="center",
                        size=".8rem",
                    ),
                    # Create a table cell with the specified views, width, and text alignment
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
        # Set the width of the box to 100%
        width="100%",
    )


def card(post: Post, index: int) -> rx.Component:
    """
    Creates a card component with the specified post and index.

    Args:
        post (Post): The post to display in the card.
        index (int): The index of the card.

    Returns:
        rx.Component: The card component.
    """
    # Create a card component with the specified post details
    return rx.fragment(
        rx.link(
            rx.card(
                card_title(post.title),  # Create the card title component
                card_photo(post.image),  # Create the card photo component
                card_text(post.text),  # Create the card text component
                card_foot(
                    post.date, post.category, post.qt_views
                ),  # Create the card foot component
                display="block",  # Set the display to block
                border="2px",  # Set the border to 2px
                box_shadow="5px 5px gray",  # Set the box shadow to 5px 5px gray
                border_radius="5%",  # Set the border radius to 5%
                width="300px",  # Set the width to 300px
                min_width="300px",  # Set the min width to 300px
                height="500px",  # Set the height to 500px
                class_name=post.category,  # Set the class name to the post's category
                margin="1rem",  # Set the margin to 1rem
                _hover={  # Set the hover styles
                    "cursor": "pointer",
                    "background-color": "cadetblue",
                },
                # on_click=CardState.set_post_id(post.id),  # Set the on click event to set the post id
            ),
            href=f"{BLOG_POSTS_ROUTE}{post.id}",  # Set the link to the post detail route with the post id
        ),
        key=index,  # Set the key to the index
    )
