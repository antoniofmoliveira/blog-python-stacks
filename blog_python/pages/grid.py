import reflex as rx

from ..components import cards
from ..navigation import BLOG_POSTS_ROUTE
from ..state import State
from .base import base_page


@rx.page(
    route=BLOG_POSTS_ROUTE,
    # on_load=State.load_posts,
)
def grid_page() -> rx.Component:
    return base_page(cards())
