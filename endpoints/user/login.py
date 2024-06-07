from flask import render_template, request, redirect, url_for, flash
from . import user

@user.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        if not username:
            flash('Username cannot be blank', 'danger')
            return redirect(url_for('user.login'))
        return redirect(url_for('user.code', user=username))
    return render_template('login.html')
