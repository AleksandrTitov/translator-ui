from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, Form, validators
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class TrForm(FlaskForm):
    text = TextAreaField('Text to translate', validators=[DataRequired()])
    submit = SubmitField('Translate it')
    submit2 = SubmitField('Analyze it')


class TranslateForm(Form):
    text = TextAreaField('Text to translate', validators=[validators.required()])
    translate = SubmitField('Translate')


class AnalyseForm(Form):
    text = TextAreaField('Text to analyse', validators=[validators.required()])
    analyse = SubmitField('Analyse')