from flask import Blueprint         #세분화 한걸 연결시켜주는 게 Blueprint, / app.route, app.errorhandler를 대신해준다

main = Blueprint('main', __name__)

from . import views, errors