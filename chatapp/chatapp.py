"""Welcome to Reflex! This file outlines the steps to create a basic app."""

from rxconfig import config

import reflex as rx
from chatapp import style

docs_url = "https://reflex.dev/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"


class State(rx.State):
    """The app state."""


def qa(question: str, answer: str) -> rx.Component:
    return rx.box(
        rx.box(
            rx.text(question, style=style.question_style),
            text_align="right",
            ),
        rx.box(
            rx.text(answer, style=style.answer_style),
            text_align="left",
        ),
        margin_y="1em"
    )

def chat() -> rx.Component:
    qa_pairs = [
        (
            "What is Reflex",
            "A way to build web apps pure Python!",
        ),
        (
            "What can I make with it?",
            "Anything from a simple website to a complex web app!",
        ),
    ]
    return rx.box(
        *[qa(question, answer) for question, answer in qa_pairs]
    )

def action_bar() -> rx.Component:
    return rx.hstack(
        rx.chakra.input(placeholder="Ask a question", style=style.input_style),
        rx.button("Ask", style=style.button_style)
    )


def index() -> rx.Component:
    return rx.container(
        chat(),
        action_bar())


app = rx.App()
app.add_page(index)
