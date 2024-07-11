import reflex as rx

from ..components import full_post
from ..navigation import BLOG_POST_DETAIL_ROUTE
from ..state import State
from .base import base_page

@rx.page(
    route=BLOG_POST_DETAIL_ROUTE,
    on_load=State.update_post,
)
def post_page() -> rx.Component:
    return base_page(full_post())
