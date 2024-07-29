import reflex as rx

from ..components import full_post
from ..navigation import BLOG_POST_DETAIL_ROUTE
from ..state import State
from .base import base_page



@rx.page(
    # Route for the blog post detail page
    route=BLOG_POST_DETAIL_ROUTE,
    # Call State.update_post when the page is loaded
    on_load=State.update_post,
)
def post_page() -> rx.Component:
    """
    Returns a page component with the full post details.

    Returns:
        A base page component with the full post component.
    """
    # Return the base page component with the full post component
    return base_page(full_post())
