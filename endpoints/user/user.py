from flask import Blueprint, render_template, request, redirect, url_for, flash
from ..code_storage import users_code

user = Blueprint('user', __name__)

@user.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        if not username:
            flash('Username cannot be blank', 'danger')
            return redirect(url_for('user.login'))
        return redirect(url_for('user.code', user=username))
    return render_template('login.html')

# @user_login.route('/code/<string:user>')
# def user_code(user):
#     return f'Welcome, {user}! Here is your code page.'


@user.route('/code/<string:user>', methods=['GET', 'POST'])
def code(user):
    if user not in users_code:
        users_code[user] = ''

    if request.method == 'POST':
        code = request.form['code']
        users_code[user] = code
        render_template('code.html', code=users_code[user])

    return render_template('code.html', code=users_code[user])


@user.route('/code_old/<string:user>', methods=['GET', 'POST'])
def code_old(user):
    if user not in users_code:
        users_code[user] = ''

    if request.method == 'POST':
        code = request.form['code']
        users_code[user] = code
        render_template('code_old.html', code=users_code[user])

    return render_template('code_old.html', code=users_code[user])
