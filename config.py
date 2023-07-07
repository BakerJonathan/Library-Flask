import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config():
    """
        Set config variables for flask
        using environment where possible, then config variable
    """
    FLASK_APP = os.getenv('FLASK_APP')
    FLASK_ENV = os.getenv('FLASK_ENV')
    SECRET_KEY= os.environ.get('SECRET_KEY') or "Some filler here"
    SQLALCHEMY_DATABASE_URI= os.environ.get('DATABASE_URI') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_NOTIFICAITONS = False