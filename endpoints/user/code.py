from flask import render_template, request, flash
from . import user
from ..code_storage import users_code



from RestrictedPython import compile_restricted
from RestrictedPython import safe_globals

def compile(code):
    byte_code = compile_restricted(code, '<string>', 'exec')
    return byte_code

@user.route('/code/<string:user>', methods=['GET', 'POST'])
def code(user):
    if user not in users_code:
        users_code[user] = ''

    error = None
    if request.method == 'POST':
        code = request.form['code']
        users_code[user] = code

        try:
            compile(users_code[user])
        except SyntaxError as e:
            # flash(f'Syntax error: {repr(e)}', 'danger')
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
