""" Reflex login UI """

import reflex as rx
from fitcloud import styles
from fitcloud.utils import loginform

def index() -> rx.Component:
    # We'll start by creating the main container where all other  UI conrols are stored
    login_form = loginform()

    # main stack to return
    _main = rx.chakra.container(
        login_form,
        # stack settings,
        style=styles.main_container_style,
        center_content=True,
    )

    return _main
    
app = rx.App()
app.add_page(index)
