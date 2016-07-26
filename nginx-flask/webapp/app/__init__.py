from flask import Flask

def create_app():
    # Instantiate Flask application
    app = Flask(__name__)

    @app.route('/')
    def home():
        return 'Hello World!'

    return app
