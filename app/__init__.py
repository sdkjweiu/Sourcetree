from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required
import pymysql
from flask_mail import Mail, Message
from config import config           #파이썬 파일 자체가 모듈이다

bootstrap = Bootstrap()         #불러오고
mail = Mail()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)     #초기화
    mail.init_app(app)

    from .main import main as main_blueprint        # main을 썼을 때는 app 폴더가 있는 위치(SourceTree)에서 main을 찾게 된다
    app.register_blueprint(main_blueprint)          # .main을 써서 app 폴더 안에 있는 main을 찾게 해준다

    return app

