from flask import Flask, render_template, abort, session, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required


class NameForm(FlaskForm):      #FlaskForm 상속
    name = StringField('What is your name?', validators=[Required()]) #validators=[Required()] -> 필드에 데이터가 있는지 검증
    submit = SubmitField('Submit')