from flask import Flask, render_template
from flask.helpers import url_for
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
    app.config.from_object(config[config_name])     # key : value 의 형태인 클래스들을 app.config 에 적용한다
    config[config_name].init_app(app)

    bootstrap.init_app(app)     #초기화
    mail.init_app(app)

    from .main import main as main_blueprint        # main을 썼을 때는 app 폴더가 있는 위치(SourceTree)에서 main을 찾게 된다  / .main을 써서 app 폴더 안에 있는 main을 찾게 해준다
    app.register_blueprint(main_blueprint)          # bluprint에서 합친 걸 app에 적용

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')      # url_prefix : 블루프린트에서 정의된 모든 라우트에 접두어를 붙여 등록, 개발속도 단축용

    return app