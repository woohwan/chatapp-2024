""" Reflex login UI """

import reflex as rx
from fitcloud import style


# return custom text input field
def get_input_field(icon: str, placeholder: str, _type: str):
    return rx.chakra.container(
        # I'll be displaying a icon side by side so we need to stack horizontally.
        rx.chakra.hstack(
            rx.chakra.icon(
                tag=icon,   # we pass this in when we call the func.
                color="white",
                fontSize="11px"
            ),
            rx.chakra.input(
                placeholder=placeholder,    # pass in when called
                border="0px",
                focus_border_color="None",
                color="white",
                fontWeight="semibold",
                fontSize="11px",
                type_=_type,
            ),
        ),
        # container settings
        borderBottom="0.1px solid grey",
        width="300px",
        height="45px",

    )

def index() -> rx.Component:
    # We'll start by creating the main container where all other  UI conrols are stored
    login_container = rx.chakra.container(
        rx.chakra.vstack(
            # we'll store the inputs and buttons in here vertically
            # some padding at the top
            rx.chakra.container(height="65px"),
            rx.chakra.container(
                rx.chakra.text(
                    "Sign In",
                    fontSize="28px",
                    color="white",
                    fontWeight="bold",
                    letterSpacing="2px",
                ),
                # text settngs
                width='250px',
                center_content=True,
            ),
            rx.chakra.container(
                rx.chakra.text(
                    "Reflex UI Concept With Python",
                    fontSize="12px",
                    color="white",
                    fontWeight="#eeeeee",
                    letterSpacing="0.25px",
                ),
                # text settngs
                width='250px',
                center_content=True,
            ),
            # some more padding
            rx.chakra.container(height="50px"),
            # we'll create a function that returns a custom text field in order to minimize code cluttering
            get_input_field("email", "Email", "email"),
            rx.chakra.container(height="5px"),
            get_input_field("lock", "Password", "password"),
            rx.chakra.container(height="5px"),
            rx.chakra.container(
                rx.chakra.text(
                    "Forgot Password?",
                    color="white",
                    fontSize="11px",
                    textAlign="end",
                )
            ),
            rx.chakra.container(height="55px"),
            # form button
            rx.chakra.container(
                rx.chakra.button(
                    rx.chakra.text(
                        "Sign In",
                        color="white",
                        fontSize="11px",
                        fontWeight="bold"
                    ),
                    # button settings
                    width="300px",
                    height="45px",
                    color_scheme="blue"
                )
            )

        ),
        # container settings
        center_content=True,
        width="400px",
        height="75vh",
        bg="#1D2330",
        borderRadius="15px",
        boxShadow="41px -41px 82px #0d0f15, -41px 41px 82px #2d374b",
    )

    # main stack to return
    _main = rx.chakra.container(
        login_container,
        # stack settings,
        center_content=True,
        justifyContent="center",
        maxWidth="auto",
        height='100vh',
        bg="#1D2330"
    )

    return _main
    
app = rx.App()
app.add_page(index)
