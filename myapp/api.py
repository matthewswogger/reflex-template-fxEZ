import reflex as rx
import json

def root():
    data = {"message": "hello from reflex"}
    return rx.text(json.dumps(data, indent=2), font_family="monospace")
