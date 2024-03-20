import reflex as rx
from fitcloud import style
from fitcloud.state import FormState

def login() -> rx.Component:
    return rx.box( 
        rx.chakra.form(
            rx.chakra.form_control(
                rx.chakra.vstack(
                    rx.heading(
                        "Login into your Account", size="7", margin_bottom="2rem"
                    ),
                    rx.input(
                        placeholder="Enter userid",
                        id="userId",
                        style=style.input_style,
                    ),
                    rx.input(
                        placeholder="Enter password",
                        type="password",
                        id="password",
                        style=style.input_style
                    ),
                    rx.input(
                        placeholder="Enter MFA Code",
                        id="mfaCode",
                        style=style.input_style,
                    ),
                    rx.box(
                        rx.button(
                            "Submit",
                            color_scheme="blue",
                            type="submit",
                            style=style.button_style,
                            margin_top="15px",
                        ),
                    ),
                ),
            ),
            on_submit=FormState.handle_submit,
            reset_on_submit=True,
        ),
        padding="4rem 5rem",
        margin_top="15vh",
        margin_x="auto",
        border="1px solid gray"
    )

def auth():
    pass

def chat(prompt: str):
    pass

def index() -> rx.Component:
    return rx.center( 
            login(),
            align="center"
        )



app = rx.App()
app.add_page(index)
