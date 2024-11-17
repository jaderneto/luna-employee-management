from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, HiddenField, EmailField
from wtforms.validators import DataRequired, Email, Length, EqualTo


class LoginForm(FlaskForm):
    login_username = StringField('Username', validators=[DataRequired(), Length(min=4)])
    login_password = PasswordField('Password', validators=[DataRequired()])
    form_type = HiddenField(default='login')  # Campo oculto para identificar o tipo de formulário
    login_submit = SubmitField('Entrar')


class RegisterForm(FlaskForm):
    register_username = StringField('Username', validators=[DataRequired(), Length(min=2, max=150)])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    register_password = PasswordField('Password', validators=[DataRequired(),
                                                              Length(min=6),
                                                              EqualTo('confirm_password',
                                                                      message="Passwords must match")])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired()])
    role = SelectField('Role',
                       choices=[('normal', 'Normal'), ('admin', 'Admin'), ('manager', 'Manager')],
                       validators=[DataRequired()])
    form_type = HiddenField(default='register')  # Campo oculto para identificar o tipo de formulário
    register_submit = SubmitField('Create Account')
