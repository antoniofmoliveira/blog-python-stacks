import reflex as rx


class Post(rx.Model):
    id: int
    title: str
    text: str
    date: str
    category: str
    image: str
    qt_views: int
