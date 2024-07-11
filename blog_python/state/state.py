from typing import Optional
import reflex as rx

from ..model import Post
from ..data import all_posts


class State(rx.State):
    """The app state."""

    posts: list[Post] = all_posts
    post: Optional[Post] = None

    @rx.var
    def post_id(self) -> str:
        return self.router.page.params.get("post_id", "0")

    def update_post(self):
        self.post = self.posts[int(self.post_id)]
