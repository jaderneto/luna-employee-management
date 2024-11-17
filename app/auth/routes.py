from flask import Blueprint, render_template, flash, redirect, url_for, request


bp = Blueprint('main', __name__)


@bp.route('/', methods=['GET', 'post'])
def index():
    from app.auth.forms import LoginForm, RegisterForm
    login_form = LoginForm()
    register_form = RegisterForm()

    if request.method == 'POST':
        if login_form.form_type.data == 'login' and login_form.validate():
            username = login_form.login_username.data
            password = login_form.login_password.data

            if username == 'jader' and password == '12345':
                print('Login Done!!')
                return redirect(url_for('main.home'))
            else:
                flash('Credenciais incorretas, tente novamente.')
                print(f'Credenciais incorretas!! Login: {username} - Senha: {password}')
                return redirect(url_for('main.index'))

        elif register_form.form_type.data == 'register':
            if register_form.validate():
                username = register_form.register_username.data
                email = register_form.email.data
                password = register_form.register_password.data
                role = register_form.role.data

                print('Register Done!!')
                return redirect(url_for('main.index'))
            else:
                flash('Dados inputados estão incorretos.')

    return render_template('index/index.html',
                           login_form=login_form,
                           register_form=register_form)


@bp.route('/home')
def home():
    return render_template('index/home.html')


@bp.route('/auth')
def auth():
    return "You are in Auth page"


@bp.route('/auth/about')
def auth_about():
    return "You are in Auth About page"
