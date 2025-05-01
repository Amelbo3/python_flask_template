from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms.widgets import html5
from wtforms import FloatField, StringField, IntegerField, SelectField, PasswordField, SubmitField, BooleanField, TextAreaField, DecimalField, DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Mot de Passe', validators=[DataRequired()])
    remember = BooleanField('Se souvenir de moi!')
    submit = SubmitField('Se connecter')