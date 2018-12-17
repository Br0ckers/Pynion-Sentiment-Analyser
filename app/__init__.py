from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
from flask import request, jsonify, Flask, flash, redirect, render_template, session, abort, url_for

import numpy as np
import pandas as pd
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

app = Flask(__name__)
app.config.from_object(Config)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
db = SQLAlchemy(app)
db.create_all()

engine = create_engine('sqlite:////tmp/test.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    import app.models
    Base.metadata.create_all(bind=engine)

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404
