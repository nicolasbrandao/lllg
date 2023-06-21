from sources import init_app as init_sources
from context import init_app as init_context
from vector_store import init_app as init_vector_store
from flask import Flask
import logging


def create_app():
    app = Flask(__name__)

    # Initialize all your modules
    init_sources(app)
    init_context(app)
    init_vector_store(app)
    app.logger.setLevel(logging.DEBUG)

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
