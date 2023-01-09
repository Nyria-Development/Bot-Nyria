from flask import Flask, render_template
import logging


class WebserverNyria(Flask):
    def __init__(self):
        super().__init__(__name__)
        self.log = logging.getLogger("werkzeug")
        self.log.setLevel(logging.ERROR)

        @self.route("/")
        def index():
            return render_template("index.html")

        self.run()
