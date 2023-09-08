from flask import Flask
from config import Config
from flask_cors import CORS

def init_app():
    app = Flask(__name__, static_folder=Config.STATIC_FOLDER, template_folder=Config.TEMPLATE_FOLDER)
    CORS(app, supports_credentials=True)
    app.config.from_object(Config)
    return app