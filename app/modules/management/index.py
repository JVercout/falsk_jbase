from flask import render_template

from app.blueprints import management_console


@management_console.route('/')
def index():
    return render_template('index.html')


# @management_console.app_errorhandler(404)
# def handle_404(err):v
#     return render_template('400.html'), 404

