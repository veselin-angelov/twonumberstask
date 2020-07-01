from flask import Flask, render_template, request, redirect, url_for, Blueprint
from .numbers import Numbers

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        values = (
            None,
            request.form['number1'],
            request.form['number2'],
            request.form['string']
        )

        Numbers(*values).create()

        last_row = Numbers.get_last_record()

        return render_template('index.html', last_row=last_row)

    return render_template('index.html')


if __name__ == '__main__':
    main.app.run()