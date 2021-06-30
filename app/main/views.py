from flask import render_template, session, redirect, url_for, current_app
import pymysql
from . import main              #from . --> 여기서 점은 해당 폴더 안에 __init__.py 를 의미한다
from .forms import NameForm
from ..email import send_email

@main.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        conn = pymysql.connect(host='192.168.182.128', port=3306, user=current_app.config['DB_USER'], passwd=current_app.config['DB_PASSWD'], database='flasky')
        cur = conn.cursor()
        cur.execute('select username from user where username="%s"' %(form.name.data))
        user = cur.fetchone()  #fetchone() 결과값 보여줌=리턴
        if user is None:
            cur.execute('insert into user (username) value ("%s")' %(form.name.data))
            conn.commit()       #DML에서는 커밋을 해야함, 저장
            session['known'] = False
            send_email ('sdkjweiu@nate.com', 'New User', 'mail/new_user')       #send_email(to, subject, template, **kwargs): 순서로
            
        else:
            session['known'] = True
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('.index'))
    return render_template('index.html', form=form, name=session.get('name'), know=session.get('known', False))