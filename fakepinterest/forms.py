# criar os formulários do site
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from sqlalchemy.testing.pickleable import User
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError

from fakepinterest.models import Usuario


class FormLogin(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired()])
    botao_confirmacao = SubmitField('Fazer Login')


class FormCriarConta(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Nome de usuário', validators=[DataRequired()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(6, 20)])
    confirmacao_senha = PasswordField('Confirmação de Senha', validators=[DataRequired(), EqualTo("senha")])
    botao_confirmacao = SubmitField('Criar Conta')

    def validate_email(self, email_field):
        usuario = Usuario.query.filter_by(email=email_field.data).first()
        if usuario:
            return ValidationError("Email já cadastrado! Faça o login para continuar.")


class FormFoto(FlaskForm):
    foto = FileField('Foto', validators=[DataRequired(), FileAllowed(['jpg', 'png'])])
    botao_confirmacao = SubmitField('Enviar')

