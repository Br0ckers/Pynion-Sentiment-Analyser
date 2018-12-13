from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import request, jsonify, Flask, flash, redirect, render_template, session, abort, url_for

#from models import Query

app = Flask(__name__)
app.config.from_object(Config)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
db = SQLAlchemy(app)
db.create_all()

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404
