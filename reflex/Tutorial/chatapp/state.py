import reflex as rx
import openai
from openai import OpenAI
import os

openai.api_key = os.environ["OPENAI_API_KEY"]

class State(rx.State):
    # The current question being asked
    question: str

    # Keep track of the chat history as a list of (question, answer) tuples.
    chat_history: list[tuple[str, str]]

    def answer(self):
        client = OpenAI()
        session = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": self.question}
            ],
            stop=None,
            temperature=0.7,
            stream=True
        )

        # Add to the answer as the chatbo responds.
        answer = ""
        self.chat_history.append((self.question, answer))

        # Clear the question input:
        self.question = ""

        # Yield her to claer the frontend input before continuing
        yield

        for item in session:
            if hasattr(item.choices[0].delta, "content"):
                if item.choices[0].delta.content is None:
                    # presense of 'None' indicate the end of the response
                    break
                answer += item.choices[0].delta.content
                self.chat_history[-1] = (self.chat_history[-1][0], answer)
                yield