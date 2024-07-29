import reflex as rx


class Post(rx.Model):
    """
    Represents a blog post.

    Attributes:
        id (int): The post's unique identifier.
        title (str): The post's title.
        text (str): The post's content.
        date (str): The post's publication date.
        category (str): The post's category.
        image (str): The post's image filename.
        qt_views (int): The number of views the post has.
    """
    id: int
    title: str
    text: str
    date: str
    category: str
    image: str
    qt_views: int
