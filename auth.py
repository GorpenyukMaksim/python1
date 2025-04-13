from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, login_required, logout_user

import main
from . import db
from werkzeug.security import generate_password_hash, check_password_hash

from models import User

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password):
        flash('Пожалуйста, проверьте свои данные для входа и повторите попытку.')
        return redirect(url_for('auth.login'))
    login_user(user, remember=remember)
    return redirect(url_for('main.profile'))

@auth.route('/signup')
def signup_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first() # если адрес электронной почты уже существует в базе данных

    if user: # если пользователь найден, перманравляем обратно на страницу регистрации
        return redirect(url_for('auth.signup'))

    # создание нового пользователя. Хемирование пароля.
    new_user = User(email=email, name=name, password=generate_password_hash(password, method='pbkdf2:sha256'))

    # добавить нового пользователя в базу данных
    db.session.add(new_user)
    db.session.commit()
    # ход для проверки и добавления пользователя в базу данных
    return redirect(url_for('auth.login'))

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))

    if user:
        flash('Такой адрес уже существует')
        return redirect(url_for('auth.signup'))