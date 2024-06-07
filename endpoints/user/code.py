from flask import render_template, request
from . import user
from ..code_storage import users_code

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
