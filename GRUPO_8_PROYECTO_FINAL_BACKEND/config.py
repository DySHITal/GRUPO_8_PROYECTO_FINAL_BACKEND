from dotenv import dotenv_values

class Config:
    config = dotenv_values('.env')

    SECRET_KEY = config['SECRET_KEY']
    SERVER_NAME = "127.0.0.1:5000"
    DEBUG = True

    DATABASE_USERNAME = config['DATABSE_USERNAME']
    DATABASE_PASSWORD = config['DATABSE_PASSWORD']
    DATABASE_HOST = config['DATABSE_HOST']
    DATABASE_PORT = config['DATABSE_PORT']

    TEMPLATE_FOLDER = "templates/"
    STATIC_FOLDER = "static/"