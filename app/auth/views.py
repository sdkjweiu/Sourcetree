from app.email import send_email
from flask import render_template, redirect, request, url_for, flash, session, current_app
import pymysql
from . import auth
from .forms import LoginForm, RigistrationForm
from werkzeug.security import check_password_hash, generate_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        conn = pymysql.connect(host='192.168.182.128', port=3306, user=current_app.config['DB_USER'], passwd=current_app.config['DB_PASSWD'], database='flasky')
        cur = conn.cursor()
        cur.execute('select email, password_hash, username from user where email="%s"' %(form.email.data))
        user = cur.fetchone()
        cur.close()
        conn.close()
        if user is not None and check_password_hash(user[1], form.passowrd.data):
            session['id'] = user[0]
            session['name'] = user[2]
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('Invalid username or password.')
    return render_template('auth/login.html', form=form)

@auth.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out.')
    return redirect(url_for('main.index'))

@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RigistrationForm()
    if form.validate_on_submit():
        pwd = generate_password_hash("%s" %form.password.data)
        conn = pymysql.connect(host='192.168.182.128', port=3306, user=current_app.config['DB_USER'], passwd=current_app.config['DB_PASSWD'], database='flasky')
        cur = conn.cursor()
        cur.execute('insert into user (email, username, password_hash) values ("%s", "%s", "%s")' %(form.email.data, form.username.data, pwd))
        conn.commit()
        cur.execute('select id from user where="%s"' %(form.email.data))
        id = cur.fetchone()
        cur.close()
        conn.close()
        s = Serializer(current_app.config['SECRET_KEY'], expiration=3600)
        token = s.dumps({'confirm':id[0]})
        send_email("%s"%(form.email.data), 'Confirm Your Account', 'auth/email/confirm', user=(form.email.data,form.username.data,pwd), token=token)
        flash('A confirmation email has been sent to you by email.')
        return redirect(url_for('main.index'))
    return render_template('auth/register.html', form=form)

@auth.route('/confirm/<token>')
@login_required
def confirm(token):
    conn = pymysql.connect(host='192.168.182.128', port=3306, user=current_app.config['DB_USER'], passwd=current_app.config['DB_PASSWD'], database='flasky')
    cur = conn.cursor()
    if cur.execute('select confirmed from user where email=''):
        return redirect(url_for('main.index'))
    if token:
        flash('You have confirmed your account. Thanks!')
    else:
        flash('The confirmation link is invalid or has expired.')
    return redirect(url_for('main.index'))