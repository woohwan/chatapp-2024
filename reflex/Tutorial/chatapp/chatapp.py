"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from chatapp import style
from chatapp.state import State

def qa(question: str, answer: str) -> rx.Component:
    return rx.chakra.box(
        rx.chakra.box(
            rx.chakra.text(question, style=style.question_style),
            text_align="right",
            ),
        rx.chakra.box(
            rx.chakra.text(answer, style=style.answer_style),
            text_align="left",
        ),
        margin_y="1em"
    )

def chat() -> rx.Component:
    return rx.chakra.box(
        rx.foreach(
            State.chat_history,
            lambda messages: qa(messages[0], messages[1])
        )
    )

def action_bar() -> rx.Component:
    return rx.chakra.hstack(
        rx.chakra.input(
            value=State.question,
            placeholder="Ask a question", 
            on_change=State.set_question,
            style=style.input_style),
        rx.chakra.button("Ask", 
                  on_click=State.answer,
                  style=style.button_style)
    )


def index() -> rx.Component:
    return rx.chakra.container(
        chat(),
        action_bar(),
        size='1',         # test container size: 1~4, default: 4
        )


app = rx.App()
app.add_page(index)
