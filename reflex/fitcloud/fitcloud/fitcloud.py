import reflex as rx
from fitcloud import style
from fitcloud.state import FormState

def login() -> rx.Component:
    return rx.chakra.form(
            rx.chakra.form_control(
                rx.chakra.vstack(
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
                    rx.button(
                        "Submit",
                        color_scheme="blue",
                        type="submit",
                    ),
                ),
            ),
            on_submit=FormState.handle_submit,
            reset_on_submit=True,  
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
