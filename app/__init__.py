from flask import Flask, make_response

def create_app():
    app = Flask(__name__)

    @app.route('/', methods=['GET'])
    def index():
        return make_response([], 200)

    return app
