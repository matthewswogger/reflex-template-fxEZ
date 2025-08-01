from rxconfig import config
import reflex as rx

docs_url = "https://reflex.dev/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"

# Add state and page to the app.

class State(rx.State):
    # The app state
    pass

def index() -> rx.Component:
    return rx.fragment(
        rx.vstack(
            rx.heading("Welcome to Reflex on Railway!", font_size="2em"),
            rx.box("Get started by editing ", rx.code(filename, font_size="1em")),
            rx.link(
                "Check out our docs!",
                href=docs_url,
                border="0.1em solid",
                padding="0.5em",
                border_radius="0.5em",
                _hover={
                    "color": rx.color_mode_cond(
                        light="rgb(107,99,246)",
                        dark="rgb(179, 175, 255)",
                    )
                },
            ),
            spacing="6",
            font_size="2em",
            padding_top="10%",
        ),
    )

def health() -> rx.Component:
    return rx.text("healthy")

def not_found(page_text) -> rx.Component:
    return rx.fragment(
        rx.vstack(
            rx.heading(page_text, font_size="2em"),
            spacing="6",
            padding_top="10%",
        ),
    )
