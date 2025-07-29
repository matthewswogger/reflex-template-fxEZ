# Welcome to Reflex! This file outlines the steps to create a basic app

import reflex as rx

from .pages import index
from .pages import health
from .pages import not_found

from .api import root

app = rx.App()

app.add_page(index)
app.add_page(health)
app.add_page(root, route="/api/")
