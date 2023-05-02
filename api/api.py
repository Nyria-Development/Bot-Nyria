import logging
from fastapi import FastAPI


class Api(FastAPI):
    def __init__(self):
        super().__init__()

        @self.get("/")
        async def hello_world():
            return "Ich mag züge"
