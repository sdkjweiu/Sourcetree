from flask import Flask, render_template, current_app
from . import mail
from flask_mail import Message



def send_email(to, subject, template, **kwargs):
    msg = Message(current_app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + subject,       #제목, 빼도 상관없음
                    sender=current_app.config['FLASKY_MAIL_SENDER'], recipients=[to])   #보내는 이  , recipients = 받는 사람
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    mail.send(msg)