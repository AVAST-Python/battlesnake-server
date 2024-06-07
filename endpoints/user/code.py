from flask import render_template, request
import json

from pygments import highlight
from pygments.lexers import JsonLexer
from pygments.formatters import HtmlFormatter

from . import user
from ..code_storage import users_code, users_compiled_function
from ..debug_storage import execution_results
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


    data = execution_results[user]
    formatter = HtmlFormatter(style="colorful", full=True, cssclass="source")
    highlighted_entries = []

    for i,entry in enumerate(data):
        result = entry['result']
        data_received = json.dumps(entry['data_received'], indent=4)
        highlighted_data_received = highlight(data_received, JsonLexer(), formatter)
        highlighted_entries.append({
            'index': i,
            'result': result,
            'data_received': highlighted_data_received
        })

    css_style = formatter.get_style_defs('.source')

    return render_template('code.html',
        code=users_code[user],
        error=error,
        results=execution_results.get(user, None),
        entries=highlighted_entries, css_style=css_style
    )
