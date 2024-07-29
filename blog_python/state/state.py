from typing import Optional
import reflex as rx

from ..model import Post
from ..data import all_posts
from blog_python import navigation


class State(rx.State):
    """
    This class definition defines a State class that represents the state of a blog application.
    """

    # A list of all posts
    posts: list[Post] = all_posts
    # The currently selected post, or None if no post is selected
    post: Optional[Post] = None
    # The category of the posts to be displayed. If empty, all posts are displayed
    category: str = ""
    """
    A list of all posts.

    This attribute is a list of Post objects representing all the posts in the blog.
    """
    """
    The currently selected post.

    This attribute is an optional Post object representing the currently selected post.
    It is None if no post is selected.
    """
    """
    The category of the posts to be displayed.

    This attribute is a string representing the category of the posts to be displayed.
    If it is an empty string, all posts are displayed.
    """

    def set_category(self, category: str):
        """
        Sets the category of the posts to be displayed.

        Args:
            category (str): The category of the posts.

        Returns:
            None
        """
        # Set the category of the posts to be displayed
        self.category = category

        # Update the state to reflect the new category
        self.updateState()

    def test_post_category(self, post: Post):
        """
        Checks if the given post's category matches the current category.

        Args:
            post (Post): The post to check.

        Returns:
            bool: True if the categories match, False otherwise.
        """
        # Check if the given post's category matches the current category
        return post.get("category") == self.category

    def test_post_id(self, post: Post):
        """
        Checks if the given post's id matches the current post id.

        Args:
            post (Post): The post to check.

        Returns:
            bool: True if the ids match, False otherwise.
        """
        # Check if the given post's id matches the current post id
        return post.get("id") == self.post_id

    def updateState(self):
        """
        Updates the state to reflect the current category and posts.

        If the category is empty, all posts are displayed. Otherwise, only posts with
        the matching category are displayed. The current post is set to None.

        Returns:
            None
        """
        # Set the current post to None
        self.post = None
        # If the category is empty, display all posts
        if self.category == "":
            self.posts = all_posts
        # Otherwise, display only posts with the matching category
        else:
            # Filter the posts based on the category
            tmp_posts = filter(self.test_post_category, all_posts)
            # Convert the filtered posts to a list
            self.posts = list(tmp_posts)



    @rx.var
    def post_id(self) -> str:
        """
        Retrieve the post id from the router's page parameters.

        Returns:
            str: The post id if it exists in the page parameters, otherwise "-1".
        """
        # Retrieve the post id from the router's page parameters
        # If the post id is not present, default to "-1"
        return self.router.page.params.get("post_id", "-1")
        # The line above gets the value associated with the key "post_id" from the
        # router's page parameters. If that key is not present, it returns the second
        # argument, "-1" in this case.

    def update_post(self):
        """
        Updates the post based on the current post id.

        If the post id is not "-1", it filters the posts list to find the post with
        the matching id and assigns it to the post attribute.

        Returns:
            None
        """
        # Check if the post id is not "-1"
        if self.post_id != "-1":
            # Filter the posts list to find the post with the matching id
            tmp_posts = filter(self.test_post_id, self.posts)
            # Convert the filtered posts to a list and assign it to the post attribute
            # The list should contain only one post, since we are filtering by id
            self.post = list(tmp_posts)[0]
