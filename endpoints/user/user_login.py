from flask import Blueprint, render_template, request, redirect, url_for, flash

user_login = Blueprint('user_login', __name__)

@user_login.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        if not username:
            flash('Username cannot be blank', 'danger')
            return redirect(url_for('user.user_login.login'))
        return redirect(url_for('user.user_login.user_code', user=username))
    return render_template('login.html')

@user_login.route('/<string:user>/code')
def user_code(user):
    return f'Welcome, {user}! Here is your code page.'
