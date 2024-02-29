import reflex as rx
import requests
from fitcloud import styles
import fitcloud.globalvars as gv
from fitcloud.states import FormState

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

# 인증
def authenticate(username, password, mfa_code):
    # Prepare data for authentication
    data = {"userId": username, "password": password, "mfaCode": mfa_code}

    # Make a POST login request to the Dev FitCloud
    response = requests.post(gv.fitcloud_url+"/login", json=data)

    # Check the response status
    if response.status_code == 200:
        # Parse the JSON response
        json_data = response.json()

        # Check if the authentication was successful
        if json_data.get("result", {}).get("validLogin", False):
            # Return the session ID along with the success flag
            return True, json_data.get("session_id", "")
        else:
            # Return failure with an empty session ID
            return False, ""
    else:
        # Return failure with an empty session ID
        return False, ""

# return login form
def loginform() -> rx.Component:
    # We'll start by creating the main container where all other  UI conrols are stored
    login_form = rx.chakra.container(
        rx.chakra.form(
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
                rx.chakra.container(height="30px"),
                # we'll create a function that returns a custom text field in order to minimize code cluttering
                get_input_field("email", "Email", "email"),
                rx.chakra.container(height="5px"),
                get_input_field("lock", "Password", "password"),
                rx.chakra.container(height="5px"),
                get_input_field("lock", "MFA Code", "number"),
                rx.chakra.container(height="5px"),
                rx.chakra.container(height="55px"),
                # form submit button
                rx.chakra.button(
                    rx.chakra.text(
                        "Sign in",
                        type="submit",
                        color="white",
                        fontSize="11px",
                        fontWeight="bold"
                    ),
                    # button settings
                    width="300px",
                    height="45px",
                    color_scheme="blue",
                ),
            ),
            on_submit=FormState.handle_submit,
            reset_on_submit=True,
            # container settings
            center_content=True,
            style=styles.login_container_style,
        )
    )
    return login_form