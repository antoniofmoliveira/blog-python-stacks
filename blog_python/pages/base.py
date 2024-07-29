import reflex as rx

from ..components import bar


def base_page(child: rx.Component, *args, **kwargs) -> rx.Component:
    """
    Create a base page component with a bar and a child component.

    Args:
        child (rx.Component): The child component.

    Returns:
        rx.Component: The base page component.
    """
    # Validate the child component
    if not isinstance(child, rx.Component):
        child = rx.heading("this is not a valid child element")

    # Create the base page component
    return rx.container(
        rx.vstack(
            bar(),  # Bar component
            child,  # Child component
            width="100%",  # Width of the component
            padding="0px",  # Padding of the component
            margin="0px"  # Margin of the component
        ),
        width="100%",  # Width of the component
        padding="0px",  # Padding of the component
        margin="0px",  # Margin of the component
        size="4",  # Size of the component
    )
