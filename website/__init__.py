from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET KEY'] = '123456asd'

    return app