from flask import render_template, request, flash
from . import user
from ..code_storage import users_code, users_compiled_function
from ..code_runner import compile, DEFAULT_CODE

@user.route('/code/<string:user>', methods=['GET', 'POST'])
def code(user):
    if user not in users_code:
        users_code[user] = DEFAULT_CODE

    error = None
    if request.method == 'POST':
        code = request.form['code']
        users_code[user] = code

        try:
            user_function = compile(users_code[user])
            users_compiled_function[user] = user_function
        except SyntaxError as e:
            error = e.msg

        # render_template('code.html', code=users_code[user])

    return render_template('code.html', code=users_code[user], error=error)


@user.route('/code_old/<string:user>', methods=['GET', 'POST'])
def code_old(user):
    if user not in users_code:
        users_code[user] = ''

    if request.method == 'POST':
        code = request.form['code']
        users_code[user] = code
        render_template('code_old.html', code=users_code[user])

    return render_template('code_old.html', code=users_code[user])
