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

        @self.route("/dashboard")
        def dashboard():
            return render_template("dashboard.html")

        @self.errorhandler(404)
        def page_not_found(error):
            return render_template('404.html'), 404

        self.run(debug=True)

if __name__ == '__main__':
    app = WebserverNyria()