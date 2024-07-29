import reflex as rx

from ..state import State
from .card import card


def cards() -> rx.Component:
    """
    Render a list of blog cards.

    Returns:
        The rendered component.
    """
    # Create a horizontal stack of cards.
    # The cards are generated from State.posts using the card function.
    # The cards are displayed in a row, with wrapping and no padding.
    # The width is set to 100%.
    return rx.hstack(
        rx.foreach(
            State.posts,  # The list of posts to generate cards from.
            lambda post, index: card(post, index),  # The function to generate a card.
        ),
        display="flex",  # Display the cards in a row.
        flex_wrap="wrap",  # Allow the cards to wrap to the next line.
        flex_direction="row",  # Display the cards in a row.
        # padding="1rem",  # Uncomment this line to add padding to the cards.
        width="100%",  # Set the width of the cards to 100%.
    )
