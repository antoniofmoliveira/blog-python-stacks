import reflex as rx

from ..components import cards
from ..navigation import BLOG_POSTS_ROUTE
from ..state import State
from .base import base_page


@rx.page(
    route=BLOG_POSTS_ROUTE,
    # on_load=State.load_posts,  # Load posts when the page is loaded
)
def grid_page() -> rx.Component:
    """
    Renders the grid page.

    Returns:
        The rendered component.
    """
    # Create and return the base page component with the cards component
    return base_page(cards())  # Create the base page component with the cards component
