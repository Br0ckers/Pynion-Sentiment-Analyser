import os
basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
SQLALCHEMY_ECHO = True

class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DATABASE_CONNECT_OPTIONS = {}
    CSRF_ENABLED     = True
    CSRF_SESSION_KEY = "secret"
    SECRET_KEY = "secret"
    DEBUG = True
    SQLALCHEMY_ECHO = True


    # export API_KEY=E1xqzPEiqjlduYikpKjAkNS0w &&
    # export API_SECRET_KEY=fJQVXAJNwR44wUUKrmi8Wf12O4wQ0YTmauEGSf3RITj5FzSVWh &&
    # export ACCESS_TOKEN=1074639447310954496-jTBLObfNnTb1JZrGBUYvPRikxLIyrU &&
    # export ACCESS_TOKEN_SECRET=2XZHahU34IwsL76KYX53nuKe3a74xoGIr9WgTIixf1qQF
